# We use this class to build an interface
# over the websockets to provide an easy
# to use api for other classes

# Import libraries
import websocket
import threading
import json   
import time
from types import SimpleNamespace
from pyee import BaseEventEmitter
from typing import TypeVar
from typing import Callable

# Define subscriber type
Subscriber = TypeVar('Subscriber')

class duplex:

    # Constructor of the class
    def __init__(self, config: dict):
        # Setup the connection url
        self.node = config["node"] + "?type=device&apiKey=" + config["apiKey"]

        # Save token in the context
        self.token = config["token"]

        # Set status variable
        self.status = "CONNECTING"

        # Create variable to store tasks
        self.tasks = BaseEventEmitter()

        # Create event register for subscriptions
        self.subscriptions = BaseEventEmitter()

        # Variable for connection callback
        self.cConnection = None

        # Variable to keep track of ping
        self.ping = None

        # Queue to store packets temporarily
        self.queue = []

        # Variable to store valid event names
        self.events = ["deviceSummary", "deviceParms"]

    # Function to init the connection
    def init(self) -> None:
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

            # Check message type
            if data["header"]["task"] == "update":
                # Then instead emit to subscriptions
                self.subscriptions.emit(data["payload"]["event"] + "/" + data["payload"]["deviceID"], data["payload"]["update"])

            else:
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
    def onConnection(self, callback: Callable[[dict], None]) -> Subscriber:
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
    def send(self, packet: dict, callback: Callable[[dict], None]) -> None:
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
    
    # Function to subscribe to an event
    def subscribe(self, event: str, deviceID: str, callback: Callable[[dict], None]) -> Subscriber:
        # We will start with validating the event
        try:
            # Check if event exists in the list
            self.events.index(event)
    
        except:
            # Return topic invalid error through callback
            callback({
                "code": "TOPIC-INVALID"
            })

            return

        # Form the packet
        packet = {
            "header": {
                "task": "/topic/subscribe"
            },
            "payload": {
                "event": event,
                "deviceID": deviceID
            }
        }

        # Function to handle response of the packet
        def response(data):
            # We will then add an event listener
            self.subscriptions.on(event + "/" + deviceID, callback)

        # Send the data to the server
        self.send(packet, response)

        # Create a new namespace
        res = SimpleNamespace()

        # Define clear function
        def clear(c: Callable[[dict], None]) -> None: 
            # Create the packet
            packet = {
                "header": {
                    "task": "/topic/unsubscribe"
                },
                "payload": {
                    "event": event,
                    "deviceID": deviceID
                }
            }

            # Remove the listener
            self.subscriptions.remove_listener(event + "/" + deviceID, callback)

            # Send to server
            self.send(packet, c)

        # Append a lambda on close key
        res.clear = clear

        # Return the object
        return res