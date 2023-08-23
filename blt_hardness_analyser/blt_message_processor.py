""" Communication with LTE devices. Messages are added to the command queue as jsons
Here are some examples with keys meaning:
{
    "WHO": "TPC-7PRO #91", # Name of the device that is connected, also used as 
                           # a periodic health check to see if device is still connected
    "DEVICES": [
        {
            "NAME": "TPC-7 #89", # Device name
            "UUID": "04:91:62:A5:0B:43", # Device uuid used for connection
        },
        {
            "NAME": "", # Broadcasting device with unknown name
            "UUID": "04:66:62:A2:1B:44", # Device uuid used for connection
        }
    ] # List of the devices available for connection",
}

"""

import asyncio
from bleak import BleakScanner, BleakClient

STOP_BLT_COMMUNICATION_MESSAGE = "Connection Stopped"
EMF_MESSAGE_START = b"RECALC"
EMF_MESSAGE_END = b"EMF_DATA_SENT"
TPC_NAME_PREFIX = "TPC-7"
HEALTH_CHECK_INTERVAL = 12

TPC_7_89_MAC = "04:91:62:A5:0B:43"
TPC_NAMES = ["TPC-7 #89", "TPC-7PRO #91"]
TPC_RTX = "49535343-1e4d-4bd9-ba61-23c647249616"
TPC_TX = "49535343-8841-43f4-a8d4-ecbe34729bb3"
TBluetoothUUID = "49535343-FE7D-4AE5-8FA9-9FAFD205E455"

# Add ABS class with interface

# TODO normalize interfacess

class BltMessageProcessor:
    def process_received_message(self,):
        pass





class BltMessageProcessorSimulation:
    def __init__(self, command_queue: asyncio.Queue):
        self.command_queue = command_queue
        self.message = [
            b'WHO=TPC-7PRO #91\rK0Text=CT\rK1Text=Al\rK2Text=Ni\rK3Text=--\r',
            b'B=N_CHRG\r', b'SCALE=HRc\r', b'CALIB=CT\r', b'B=72\r',
            b'B=N_CHRG\r', b'SCALE=HB\r', b'CALIB=CT\r', b'B=72\r',
            b'RECALC\r', b'K=0.531\r', b'H=345\r',
            b'E=01845\rE=01845\rE=01845\rE=01845\rE=01845\rE=01845\rE=01845\rE=01846\rE=01846\rE=01846\rE=01847\rE=01847\rE=01847\rE=01848\rE=01848\rE=01848\rE=01848\rE=01848\rE=01848\rE=0',
            b'1849\rE=01849\rE=01849\rE=01849\rE=01849\rE=01849\rE=01849\rE=01849\rE=01849\rE=01849\rE=01849\rE=01848\rE=01848\rE=01848\rE=01848\rE=01848\rE=01848\rE=01848\rE=01848\rE=01848\r',
            b'R=0.000600\r', b'V=0.629000\r', b'EMF_DATA_SENT\r',
        ]*3

    def message_generator(self):
        for bit in self.message:
            yield bit

    def process_command(self, command: str) -> dict:
        processed_command = {}
        for message in command.split("\r"):
            if "=" not in message:
                continue

            key, value = message.split("=")
            if processed_command.get(key) is None:
                processed_command[key] = []
            processed_command[key].append(value)
        return processed_command

    async def scan_tpc_devices(self):
        await asyncio.sleep(1)
        self._tpc_devices = {"name": "test_tpc"}
        await self.command_queue.put(self._tpc_devices)

    async def run_client_for_device(self, device_name: str):
        print(f"connect to device {self._tpc_devices}")
        print(f"requested for {device_name}")
        await self.simulate_callback_handler()

    async def simulate_callback_handler(self):
        message_gen = self.message_generator()
        total_message = None
        while True: # TODO make sure that health check does not spoil emf gathering
            try:
                received_message = next(message_gen)

                if EMF_MESSAGE_START in received_message and total_message is None:
                    total_message = []

                elif EMF_MESSAGE_END in received_message:
                    total_command_message = "".join(total_message)
                    command = self.process_command(total_command_message)
                    await self.command_queue.put(command)
                    total_message = None

                elif total_message is None: # this spoils emf
                    command = self.process_command(received_message.decode("utf-8"))
                    await self.command_queue.put(command)

                elif total_message is not None:
                    total_message.append(received_message.decode("utf-8"))
                    print("gathering emf")

            except StopIteration as e:
                print('Stopped receiving messages from LTE device', e)
                await self.command_queue.put(STOP_BLT_COMMUNICATION_MESSAGE)
                break
            await asyncio.sleep(0.35)


class BltMessageProcessorBleak:
    
    def __init__(self, command_queue):
        self._tpc_devices = None
        self._device_client = None
        self.command_queue = command_queue
        self._health_check_task = None
    
    async def scan_tpc_devices(self): # TODO crashes when no devices, should just send command with empty list of devices

        nearby_lte_devices = await BleakScanner().discover()
        if nearby_lte_devices is None:
            raise LookupError(f"No LTE devices were not found")

        tpc_devices = {}

        for device in nearby_lte_devices:
            name = device.name
            if name is None:
                continue
            if TPC_NAME_PREFIX in name:
                tpc_devices[device.name] = device
        if len(tpc_devices.keys()) > 0:
            print(f"found the following lte devices: {tpc_devices}")
            self._tpc_devices = tpc_devices
        else:
            raise LookupError(f"{TPC_NAME_PREFIX} were not found in broadcasting LTE devices")
        print("finished scan")

    async def run_client_for_device(self, device_name: str): # TODO crashes when device is turned off, # TODO cancel error on app exit # TODO run client should be device agnostic
        print("function run client for device started")
        if self._device_client is not None:
            await self.stop_client_for_device()
        if self._tpc_devices is None:
            raise RuntimeError(f"Devices were not scanned, nothing to connect to")
        device = self._tpc_devices.get(device_name) # TODO get from None throuws exepction
        if device is None:
            raise RuntimeError(f"Device {device_name} was not available in scanned devices")

        self._device_client = BleakClient(device)
        await self._device_client.connect()
        await self._device_client.start_notify(TPC_RTX, self.callback_handler)

        # loop = asyncio.get_event_loop()
        # self._health_check_task = loop.create_task(self.health_check())
        # await self._health_check_task

    async def callback_handler(self, _, data): # TODO rewrite using simulation callback
        # TODO add healthcheck reset
        await self.command_queue.put(data)

    async def stop_client_for_device(self):
        print("stopping client")
        if self._device_client is not None:
            await self._device_client.stop_notify(TPC_RTX)
            await self._device_client.disconnect()
            await self.command_queue.put(STOP_BLT_COMMUNICATION_MESSAGE)
            self._device_client = None
            print("Client stopped")
        else:
            raise RuntimeError("No device client to stop assigned")
        if self._health_check_task is not None:
            self._health_check_task.cancel()
            self._health_check_task = None

    async def health_check(self):
        while True: # TODO better have some kind of counter, that resets on a received message in callback handler
            await asyncio.sleep(HEALTH_CHECK_INTERVAL)
            print("Implement healthcheck already") 


class BLT_interface:
    """ It should scan until stop. If scan is required - scan and get devices back.
    if device is selected - select device and connect to IT automatically.
    if another device is selected - change the device and connecto to new one.
    Run callback

    """
    async def client_agnostic_blt_interface():
        while True:
            print("Scan if there is a command to scan")
            print("If device is selected - connect to it and run callback")
            print("If disconnect - stop")


        pass

##################################################################################
### simultaion code starts here
##################################################################################
async def run_queue_consumer(queue: asyncio.Queue):

    while True:
        # Use await asyncio.wait_for(queue.get(), timeout=1.0) if you want a timeout for getting data.
        data = await queue.get()
        if data == STOP_BLT_COMMUNICATION_MESSAGE:
            print(
                "Got message from client about disconnection. Exiting consumer loop..."
            )
            break
        else:
            print("Received callback data via async queue: ",  data)

async def run_wrapper(blt_client_task):
            await asyncio.sleep(10.0)
            print('App done')
            blt_client_task.cancel()

async def main_simulate():

    # test this out
    blt_command_queue = asyncio.Queue()
    decoder = BltMessageProcessorSimulation()
    client_task = decoder.simulate_callback_handler(blt_command_queue)
    consumer_task = run_queue_consumer(blt_command_queue)
    results = await asyncio.gather(client_task, consumer_task)
    print("Finished app, {results}")


async def main_bleak():
    #test_tpc_device = "TPC-7 #89"
    test_tpc_device = "kekus"

    blt_command_queue = asyncio.Queue()
    decoder = BltMessageProcessorBleak(blt_command_queue)

    await decoder.scan_tpc_devices()
    blt_client_task = asyncio.ensure_future(
            decoder.run_client_for_device(test_tpc_device)
        )

    consumer_task = asyncio.ensure_future(
        run_queue_consumer(blt_command_queue)
    )

    results = await asyncio.gather(run_wrapper(blt_client_task), blt_client_task, consumer_task)
    print("Finished app, {results}")

if __name__ == "__main__":
    asyncio.run(main_bleak())