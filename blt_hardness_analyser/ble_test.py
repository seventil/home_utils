import asyncio
from bleak import BleakScanner,BleakClient, BleakGATTCharacteristic
import time
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        #logging.FileHandler("debug.log"),
        logging.StreamHandler()
    ]
)

TPC_7_89_MAC = "04:91:62:A5:0B:43"
TPC_NAMES = ["TPC-7 #89", "TPC-7PRO #91"]
TPC_RTX = "49535343-1e4d-4bd9-ba61-23c647249616"
TPC_TX = "49535343-8841-43f4-a8d4-ecbe34729bb3"
TBluetoothUUID = "49535343-FE7D-4AE5-8FA9-9FAFD205E455"
#   TPC7_UART_SERVICE: TBluetoothUUID = '{49535343-FE7D-4AE5-8FA9-9FAFD205E455}';
#   TPC7_UART_TX_CHARACTERISTIC: TBluetoothUUID  = '{49535343-1E4D-4BD9-BA61-23C647249616}';
#   TPC7_UART_RX_CHARACTERISTIC: TBluetoothUUID  = '{49535343-8841-43F4-A8D4-ECBE34729BB3}';


async def get_all_characteristics():
    devices = await BleakScanner.discover()
    for d in devices:
        if d.name in TPC_NAMES:
            hardness_tester = d
            print(f"found device <{d.name}> at <{d.address}>")
        print(d.name)
        print(d)
    async with BleakClient(hardness_tester.address) as client:
        print("Services:")
        for service in client.services:
            print("-------------------------------------------------------service")
            print(service)
            for characteristic in service.characteristics:
                print(characteristic.handle)
                print(characteristic.uuid)
                print(characteristic.properties)
                print(characteristic.descriptors)
            print("---xxx")


async def run_ble_client(queue: asyncio.Queue):
    hardness_tester = None
    devices = await BleakScanner.discover()
    for d in devices:
        if d.name in TPC_NAMES:
            hardness_tester = d
            print(f"found device <{d.name}> at <{d.address}>")
    
    async def callback_handler(_, data):
        await queue.put((time.time(), data))
    
    async with BleakClient(hardness_tester) as client:
        logger.info("connected")
        await client.start_notify(TPC_RTX, callback_handler)

        await asyncio.sleep(10.0)
        await client.stop_notify(TPC_RTX)
        # Send an "exit command to the consumer"
        await queue.put((time.time(), None))
            # print("Devimnfo: {0}".format("".join(map(chr, device_info))))


async def run_queue_consumer(queue: asyncio.Queue):
    logger.info("Starting queue consumer")

    while True:
        # Use await asyncio.wait_for(queue.get(), timeout=1.0) if you want a timeout for getting data.
        epoch, data = await queue.get()
        if data is None:
            logger.info(
                "Got message from client about disconnection. Exiting consumer loop..."
            )
            break
        else:
            logger.info("Received callback data via async queue at %s: %r", epoch, data)

async def main():
    queue = asyncio.Queue()
    client_task = run_ble_client(queue)
    consumer_task = run_queue_consumer(queue)
    # await get_all_characteristics()
    try:
        await asyncio.gather(client_task, consumer_task)
    except Exception as e:
        logger.info(f"e {e}")



    logger.info("Main method done.")

if __name__ == "__main__":
    asyncio.run(main())