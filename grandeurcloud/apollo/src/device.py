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

    # Function to get the device parms from server
    def getParms(self, callback):
        # Form the request packet
        packet = {
            "header": {
                "task": "/device/parms/get"
            },
            "payload": {
                "deviceID": self.deviceID
            }
        }

        # Send the packet using duplex
        self.duplex.send(packet, callback)

    # Function to set the device summary from server
    def setSummary(self, summary, callback):
        # Form the request packet
        packet = {
            "header": {
                "task": "/device/summary/set"
            },
            "payload": {
                "deviceID": self.deviceID,
                "summary": summary
            }
        }

        # Send the packet using duplex
        self.duplex.send(packet, callback)

    # Function to set the device parms from server
    def setParms(self, parms, callback):
        # Form the request packet
        packet = {
            "header": {
                "task": "/device/parms/set"
            },
            "payload": {
                "deviceID": self.deviceID,
                "parms": parms
            }
        }

        # Send the packet using duplex
        self.duplex.send(packet, callback)

    # Function to attach listener on summary updates
    def onSummary(self, callback):
        # Use duplex to subscribe to event
        return self.duplex.subscribe("deviceSummary", self.deviceID, callback)

    # Function to attach listener on parms updates
    def onParms(self, callback):
        # Use duplex to subscribe to event
        return self.duplex.subscribe("deviceParms", self.deviceID, callback)