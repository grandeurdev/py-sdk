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
    def get(self, path: str, callback: Callable[[str, dict], None]) -> None:
        # Form the request packet
        payload = {
            "deviceID": self.deviceID,
            "path": path
        }

        # Send the packet using duplex
        self.duplex.send("/device/data/get", payload, callback)

    # Function to set the device data on server

    def set(self, *args):
        # Check the number of arguments
        if len(args) > 2:
            if len(args) % 2 == 0:
                # Multiple paths and data
                paths = []
                data_arr = []

                # Extract paths and data into separate arrays
                for i in range(0, len(args), 2):
                    paths.append(args[i])
                    data_arr.append(args[i + 1])

                # Setup payload
                payload = {
                    "deviceID": self.deviceID,
                    "path": paths,
                    "data": data_arr
                }

                # Place request
                return self.duplex.send("/device/data/set", payload)
        else:
            # Single path and data
            path = args[0]
            data = args[1]

            # Setup payload
            payload = {
                "deviceID": self.deviceID,
                "path": path,
                "data": data
            }

            # Place request
            return self.duplex.send("/device/data/set", payload)

    def log(self, path: str, data: dict, callback: Callable[[str, dict], None]) -> None:
        # Form the request packet
        payload = {
            "deviceID": self.deviceID,
            "path": path,
            "data": data
        }

        # Send the packet using duplex
        self.duplex.send("/device/data/log", payload, callback)

    # Function to attach listener on data updates
    def on(self, path: str, callback: Callable[[str, dict], None]) -> Subscriber:
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
