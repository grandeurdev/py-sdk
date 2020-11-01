# We use this class to build an interface
# over the websockets to provide an easy
# to use api for other classes

# Import libraries
import websocket
import threading
from types import SimpleNamespace
from pyee import BaseEventEmitter
import json   
import time

class duplex:

    # Constructor of the class
    def __init__(self, config):
        # Setup the connection url
        self.node = config["node"] + "?type=device&apiKey=" + config["apiKey"]

        # Save token in the context
        self.token = config["token"]

        # Set status variable
        self.status = "CONNECTING"

        # Create variable to store tasks
        self.tasks = BaseEventEmitter()

        # Variable for connection callback
        self.cConnection = None

        # Variable to keep track of ping
        self.ping = None

        # Queue to store packets temporarily
        self.queue = []

    # Function to init the connection
    def init(self):
        # Setup authorization header
        auth = "Authorization: " + self.token

        # Define evnet handlers
        # Function to handle on open event of ws
        def onopen(ws):
            # Connection has been opened so change the status variable
            self.status = "CONNECTED"

            # Generate event
            if (self.cConnection):
                self.cConnection("CONNECTED")

            # Start sending ping on 25sec interval
            self.ping = threading.Timer(25, self.__ping) 
            self.ping.start() 

            # Handle queued packets
            self.__handle()

        # Function to handle on close event of ws
        def onclose(ws):
            # Connectin has been closed so change the status variable
            self.status = "CONNECTING"

            # Generate event
            if (self.cConnection):
                self.cConnection("DISCONNECTED")

            # Try to reconnect
            self.__reconnect()

            # Stop ping
            self.ping.cancel()

        # Function to handle on message event of ws
        def onmessage(ws, message):
            # Convert the message into json
            data = json.loads(message)
            
            # Emit event and send payload
            self.tasks.emit(data["header"]["id"], data["payload"])

        # Then init the connection
        ws = websocket.WebSocketApp(self.node, on_open = onopen, on_message = onmessage, on_close = onclose, header = [auth])

        # Store ws into the class context
        self.ws = ws

        # Run the connection forever in a new thread
        wst = threading.Thread(target=ws.run_forever)
        wst.daemon = True
        wst.start()

    # Function to enable users to subscribe to connection updates
    def onConnection(self, callback):
        # Store the callback in context
        self.cConnection = callback

        # Create a new namespace
        res = SimpleNamespace()

        # Define clear function
        def clear(): 
            # This will clear the callback
            self.cConnection = None

        # Append a lambda on close key
        res.clear = clear

        # Return the object
        return res

    # Private function to help reconnect to server on connection close
    def __reconnect(self):
        # We will start a timer for five second
        # and then we will trigger init again
        timer = threading.Timer(5, self.init) 
        timer.start() 

    # Private function to handle ping
    def __ping(self):
        # Send a ping packet to the server
        packet = {
            "header": {
                "id": "ping",
                "task": "ping"
            },
            "payload": {

            }
        }

        # Send packet to server
        self.ws.send(json.dumps(packet))

        # Start timer again
        self.ping = threading.Timer(25, self.__ping) 
        self.ping.start() 
    
    # Function to send queued tasks to the server
    def __handle(self):
        # Loop over the queue elements
        for packet in self.queue:
            # Send the packet to the server
            self.ws.send(json.dumps(packet))

        # Clear list
        self.queue.clear()

    # Function to send a packet to the server
    def send(self, packet, callback):
        # Start with generating a new id
        id = time.time()

        # Then append it to the packet
        packet["header"]["id"] = id

        # Add event handler
        self.tasks.once(id, callback)

        # Then if the sdk is connected to the server
        if self.status == "CONNECTED":
            # Then send the packet to the server
            self.ws.send(json.dumps(packet))

        else:
            # or otherwise queue it
            self.queue.append(packet)
