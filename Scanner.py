from bluepy.btle import BTLEDisconnectError, BTLEException, DefaultDelegate, Peripheral, Scanner
import logging
import sys

_LOGGER = logging.getLogger(__name__)

class cDelegate(DefaultDelegate):
    def __init__(self):
        DefaultDelegate.__init__(self)

    def handleDiscovery(self, device, isNewDev, isNewData):
        if isNewDev:
            print("Discovered device", device.addr)
        elif isNewData:
            print("Received new data from", device.addr)
    

class Discovery():
    def __init__(self):
        scanner = Scanner().withDelegate(cDelegate())
        self.devices = scanner.scan(10.0)

    def getDevices(self, address = None):
        if address is None:
            for device in self.devices:
                self.printInfo(device)
                #self.getPeripherals(device)
        else:
            self.printInfo(device)
        
        return self.devices
    
    def printInfo(self, device):
        print("Device %s (%s), RSSI=%d dB, CONNECTABLE: %s" % (device.addr, device.addrType, device.rssi, device.connectable))

    def getPeripherals(self, device):
        try:
            self.peripheral = Peripheral(device.addr.upper()).withDelegate(cDelegate())
            for service in self.peripheral.getServices():
                print("   UUID: %s" % (service.uuid))
        except BTLEDisconnectError as e:
            _LOGGER.error("Disconected: %s", e)
        except BTLEException as e:
            _LOGGER.error("Error: %s", e)
        except Exception as e:
            print(e)

class Device():
    def __init__(self, macAddress):
        self.addr = macAddress

    def getPeripherals(self):
        print("Getting peripherals for %s" % (self.addr))
        try:
            p = Peripheral(self.addr.upper()).withDelegate(cDelegate())
            self.services = p.getServices()
            for service in self.services:
                print("UUID: %s" % (service.uuid))
                for characteristic in service.getCharacteristics():
                    print("  Properties: %s, UUID: %s, Handle: %s" % (characteristic.propertiesToString(), characteristic.uuid, characteristic.getHandle()))

        except BTLEDisconnectError as e:
            _LOGGER.error("Disconected: %s", e)
        except BTLEException as e:
            _LOGGER.error("Error: %s", e)

class BleScanner(DefaultDelegate):
    def __init__(self):
        super().__init__()
        print("Bluetooth scanner")
        discover = Discovery()
        self.devices = discover.getDevices()

        print("Found %d devices." % (len(self.devices)))
        
        return

if len(sys.argv) > 1:
    macAddress = sys.argv[1]
    Device(macAddress).getPeripherals()
else:
    BleScanner()