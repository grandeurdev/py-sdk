# Grandeur Cloud Device SDK
# This package has been designed for developers
# building facinating IoT projects with python
# system on chips like Respberry Pi. Developers
# can use this SDK to write hardware side code.

# Import handlers
from .handlers import duplex as Duplex

# Import the inteface classes
from .src import device as Device

# Import libraries
from types import SimpleNamespace
from typing import TypeVar
from typing import Callable

# Define the endpoint url
config = {
    "node": "wss://api.grandeur.tech"
}

# Define grandeur type
Project = TypeVar('Project')

# Function to init the SDK
def init(apiKey: str, token: str) -> Project : 
    # Returns an object to supported classes
    # like for devices and datastore
    grandeurConfig = {
        "apiKey": apiKey,
        "token": token
    }

    # Append the url to the configuration
    grandeurConfig.update(config)

    # Create a new duplex handler
    duplex = Duplex(grandeurConfig)

    # Store handlers in an object
    handlers = {
        "duplex": duplex
    }

    # Init the duplex connection with server
    duplex.init()

    # Create a new namespace 
    res = SimpleNamespace()

    # Function to return the connection status
    def isConnected() ->  bool:
        # Check the status
        if duplex.status == "CONNECTED":
            # Return true if the sdk is connected
            return True
        else:
            # Otherwise return a false
            return False

    # Function to place listener on connection event
    def onConnection(callback: Callable[[str], None]) -> None:
        # Use the duplex connection handler to place the listener
        duplex.onConnection(callback)

    # Function to get reference to device class
    def device(deviceID: str) -> Device:
        # We will create a new device class reference and will return it
        return Device(handlers, deviceID)

    # Add onConnection event handler to namespace
    res.onConnection = onConnection

    # Add isConnected function
    res.isConnected = isConnected

    # Add device function
    res.device = device

    # and return
    return res