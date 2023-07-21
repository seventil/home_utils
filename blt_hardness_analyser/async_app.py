'''Example shows the recommended way of how to run Kivy with the Python built
in asyncio event loop as just another async coroutine.
'''
import asyncio

from kivy.app import App
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock

from blt_message_processor import BltMessageProcessorSimulation, STOP_BLT_COMMUNICATION_MESSAGE, BltMessageProcessorBleak


ASYNC_APP_UI_TEMPLATE_FILE = "async_app.kv"
COMMAND_QUEUE_CHECKUP_INTERVAL = 0.2



class MenuScreen(Screen):
    pass

class MainScreen(Screen):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__()
        self.loop_thread = None

    def on_enter(self):
        self.loop_thread = Clock.schedule_interval(self.callback_to_loop, 1)

    def on_leave(self):  
        Clock.unschedule(self.loop_thread)

    def callback_to_loop(self, dt):
        try:
            current = int(self.ids.label_print.text)
        except:
            current = 0

        self.ids.label_print.text = str(current+1)

    def start_scan(self):
        self.ids.label.text = "Scanning blt"
        scan_devices = App.get_running_app().blt_processor.scan_tpc_devices
        App.get_running_app().command_queue.append((scan_devices,[]))

    def stop_client(self):
        print("pressed to stop client")
        self.ids.label.text = "Stopping client"
        stop_client = App.get_running_app().blt_processor.stop_client_for_device
        App.get_running_app().command_queue.append((stop_client,[]))
        print("stop client command added to queue")
        print(App.get_running_app().command_queue)

        
    def sleeping_callback(self):
        self.ids.label.text = "Connecting client"
        command_to_send = App.get_running_app().blt_processor.run_client_for_device
        args = ["TPC-7 #89"] # TODO delete hardcode, implement choice from UI
        App.get_running_app().command_queue.append((command_to_send, args))


class AsyncApp(App):
    blt_client_task = None

    def build(self): # used to build interface, but also i use it as a substitute for init. Every method is init method if you're brave enough
        self.lte_tasks = []
        return Builder.load_file(ASYNC_APP_UI_TEMPLATE_FILE)

    async def app_run_with_externals(self):
        '''This will run both methods asynchronously and then block until they
        are finished
        '''
        self.command_queue = []
        blt_messages_queue = asyncio.Queue()
        self.blt_processor = BltMessageProcessorBleak(blt_messages_queue)

        self.blt_message_consumer_task = asyncio.ensure_future(
            self.process_lte_messages(blt_messages_queue) # TODO should not end with the end message, should always work, connecting/disconnecting to devices should be inside
        )

        self.command_q_processor = asyncio.ensure_future(
            self.process_commands_from_ui()
        )

        async def run_wrapper():
            await self.async_run(async_lib='asyncio')
            self.stop_lte_client()
            self.command_q_processor.cancel()
            self.blt_message_consumer_task.cancel()
        try:
            await asyncio.gather(run_wrapper(), self.blt_message_consumer_task, self.command_q_processor)
        except asyncio.exceptions.CancelledError:
            print(f"App coroutins finished")
        except Exception as e:
            print("Unexpected runtime exepction {e}")
            raise e

    async def process_commands_from_ui(self):
        while True:
            if len(self.command_queue) > 0:
                print("Command queue received a message")
                command, args = self.command_queue.pop(0)
                print(f"command {command} args P{args}")
                loop = asyncio.get_event_loop()
                new_task = loop.create_task(command(*args))
                self.lte_tasks.append(new_task)
                print(f"Got command to execute task {new_task}")
                try:
                    await new_task
                except Exception as exc:
                    print(exc) # TODO make as a pop-up

            await asyncio.sleep(COMMAND_QUEUE_CHECKUP_INTERVAL)

    def stop_lte_client(self,):
        for task in self.lte_tasks:
            task.cancel()
        self.lte_tasks = []




    async def process_lte_messages(self, blt_messages_queue):
        while True:
            data = await blt_messages_queue.get() # TODO implement health check - if nothing comes ping
            if data == STOP_BLT_COMMUNICATION_MESSAGE:
                print(
                    "Got message from client about disconnection. Exiting consumer loop..."
                )
                break
            print("Received callback data via async queue: ",  data)
            if self.root is not None: #Self root is ScreenManager object
                current_screen = self.root.get_screen(self.root.current)
                current_screen.ids.blt_message.text = str(data)


if __name__ == '__main__':
    
    asyncio.run(
        AsyncApp().app_run_with_externals()
    )