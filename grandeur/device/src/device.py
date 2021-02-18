# This class uses the handlers to provide
# an easy to use api to end users

# Import libraries
from typing import TypeVar
from typing import Callable

# Define subscriber type
Subscriber = TypeVar('Subscriber')
Data = TypeVar('Data')

class data:

    # Constructor of the class
    def __init__(self, handlers: dict, deviceID: str):
        # Get reference to the duplex handler
        self.duplex = handlers["duplex"]

        # Store device id
        self.deviceID = deviceID

    # Function to get the device data from server
    def get(self, path: str, callback: Callable[[dict], None]) -> None:
        # Form the request packet
        payload = {
            "deviceID": self.deviceID,
            "path": path
        }

        # Send the packet using duplex
        self.duplex.send("/device/data/get", payload, callback)

    # Function to set the device data on server
    def set(self, path: str, data: dict, callback: Callable[[dict], None]) ->  None:
        # Form the request packet
        payload = {
            "deviceID": self.deviceID,
            "path": path,
            "data": data
        }

        # Send the packet using duplex
        self.duplex.send("/device/data/set", payload, callback)

    # Function to attach listener on data updates
    def on(self, path: str, callback: Callable[[dict], None]) -> Subscriber:
        # Form the request packet
        payload = {
            "deviceID": self.deviceID,
            "path": path,
            "event": "data"
        }

        # Use duplex to subscribe to event
        return self.duplex.subscribe("data", payload, callback)

class device:

    # Constructor of the class
    def __init__(self, handlers: dict, deviceID: str):
        # Get reference to the duplex handler
        self.handlers = handlers

        # Store device id
        self.deviceID = deviceID

    # Function get reference to device data
    def data(self) -> Data:
        # Return new data object
        return data(self.handlers, self.deviceID)