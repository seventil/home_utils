import asyncio
from bleak import BleakScanner,BleakClient


TPC_7_89_MAC = "04:91:62:A5:0B:43"
TPC_7_89_NAME = "TPC-7 #89"
TPC_GENERIC_ACCESS_PROFILE = "00001800-0000-1000-8000-00805f9b34fb"
TPC_GENERIC_ATTRIBUTE_PROFILE = "00001801-0000-1000-8000-00805f9b34fb"
TPC_DEVICE_INFORMATION = "0000180a-0000-1000-8000-00805f9b34fb"
TPC_UNKNOWN_SERVICE = "49535343-fe7d-4ae5-8fa9-9fafd205e455"

async def main():
    hardness_tester = None
    devices = await BleakScanner.discover()
    for d in devices:
        if d.name == TPC_7_89_NAME:
            hardness_tester = d
            print(f"found device <{d.name}> at <{d.address}>")

    async with BleakClient(hardness_tester.address) as client:
        svcs = await client.get_services()
        print("Services:")
        for service in svcs:
            print(service)
        device_info = await client.read_gatt_char(TPC_UNKNOWN_SERVICE)
        print(str.from_bytes(device_info,byteorder='big'))




if __name__ == "__main__":
    asyncio.run(main())