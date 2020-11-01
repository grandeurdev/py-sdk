# This class uses the handlers to provide
# an easy to use api to end users

class device:

    # Constructor of the class
    def __init__(self, handlers, deviceID):
        # Get reference to the duplex handler
        self.duplex = handlers["duplex"]

        # Store device id
        self.deviceID = deviceID


    # Function to get the device summary from server
    def getSummary(self, callback):
        # Form the request packet
        packet = {
            "header": {
                "task": "/device/summary/get"
            },
            "payload": {
                "deviceID": self.deviceID
            }
        }

        # Send the packet using duplex
        self.duplex.send(packet, callback)