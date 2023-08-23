'''Example shows the recommended way of how to run Kivy with the Python built
in asyncio event loop as just another async coroutine.
'''
import asyncio

from kivy.app import App
from kivy.lang.builder import Builder
from kivy.clock import Clock
from blt_message_processor import BltMessageProcessorSimulation, STOP_BLT_COMMUNICATION_MESSAGE, BltMessageProcessorBleak
from kivy.uix.screenmanager import ScreenManager, Screen
from screens import MainScreen, MenuScreen
from kivy.garden.matplotlib import FigureCanvasKivyAgg
import matplotlib.pyplot as plt
import numpy as np


ASYNC_APP_UI_TEMPLATE_FILE = "async_app.kv"
COMMAND_QUEUE_CHECKUP_INTERVAL = 0.2
BLT_PROCESSOR = BltMessageProcessorSimulation


class HardnessTesterData:
    """Class containing curent data received form ht"""
    def __init__(self):
        self.who = None
        self.b = None
        self.scale = None
        self.calib = None
        self.k = None
        self.h = None
        self.e = None
        self.name = None

        self.data = []

    def update_data(self, data: dict):
        for key, value in data.items():
            setattr(self, key.lower(), value)


class AsyncApp(App):
    blt_client_task = None

    def build(self): # used to build interface, but also i use it as a substitute for init. Every method is init method if you're brave enough
        self.lte_tasks = []
        self.hardness_tester = HardnessTesterData()
        self.plt_obj = None
        return Builder.load_file(ASYNC_APP_UI_TEMPLATE_FILE)

    async def app_run_with_externals(self):
        '''This will run both methods asynchronously and then block until they
        are finished
        '''
        self.command_queue = []
        blt_messages_queue = asyncio.Queue()
        self.blt_processor = BLT_PROCESSOR(blt_messages_queue)

        self.blt_message_consumer_task = asyncio.ensure_future(
            self.process_lte_messages(blt_messages_queue) # TODO should not end with the end message, should always work, connecting/disconnecting to devices should be inside
        )

        self.command_q_processor = asyncio.ensure_future(
            self.process_commands_from_ui()
        )

        async def run_wrapper():
            await self.async_run(async_lib='asyncio')
            for task in self.lte_tasks:
                task.cancel()
            self.lte_tasks = []
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
                self.hardness_tester.update_data(data)
                self.redraw_hardness_tester_data()

    def redraw_hardness_tester_data(self):
        current_screen = self.root.get_screen(self.root.current)

        current_screen.ids.blt_message.text = str(self.hardness_tester.data)
        current_screen.ids.blt_b.text = str(self.hardness_tester.b)
        current_screen.ids.blt_e.text = str(self.hardness_tester.e)

        if self.hardness_tester.e: #subscribe to updates
            plt.plot(self.hardness_tester.e)
            if  self.plt_obj:
                current_screen.ids.pltbox.remove_widget(self.plt_obj)
            self.plt_obj = FigureCanvasKivyAgg(plt.gcf())
            current_screen.ids.pltbox.add_widget(self.plt_obj)

        


if __name__ == '__main__':
    asyncio.run(
        AsyncApp().app_run_with_externals()
    )