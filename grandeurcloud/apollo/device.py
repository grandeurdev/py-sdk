# Grandeur Cloud Device SDK
# This package has been designed for developers
# building facinating IoT projects with python
# system on chips like Respberry Pi. Developers
# can use this SDK to write hardware side code.

# Import handlers
from grandeurcloud.apollo.handlers.device import duplex as duplex

# Import libraries
from types import SimpleNamespace

# Define the endpoint url
config = {
    "node": "wss://api.grandeur.tech"
}

# Function to init the SDK
def init(apiKey, token): 
    # Returns an object to supported classes
    # like for devices and datastore
    apolloConfig = {
        "apiKey": apiKey,
        "token": token
    }

    # Append the url to the configuration
    apolloConfig.update(config)

    # Create a new duplex handler
    duplexHandler = duplex(apolloConfig)

    # Store handlers in an object
    handlers = {
        "duplex": duplexHandler
    }

    # Init the duplex connection with server
    duplexHandler.init()

    # Create a new namespace 
    res = SimpleNamespace()

    # Function to place listener on connection event
    def onConnection(callback):
        # Use the duplex connection handler to place the listener
        duplexHandler.onConnection(callback)

    # Add onConnection event handler to namespace
    res.onConnection = onConnection

    # and return
    return res