# We use this class to build an interface
# over the websockets to provide an easy
# to use api for other classes

# Import libraries
import websocket
import threading
import json   
import time
import re
from types import SimpleNamespace
from pyee import BaseEventEmitter
from typing import TypeVar
from typing import Callable

# Define subscriber type
Subscriber = TypeVar('Subscriber')

# Extend event emitter class by pyee
class EventEmitter(BaseEventEmitter):

    # Function to get event names
    def eventNames(self) -> dict:
        # Return keys of events
        return self._events.keys()

# Object to store the events 
class buffer():

    # Constructor of buffer
    def __init__(self):
        # Init the list where we will store packets
        self.list = dict()

    # Function to push a packet to the queue
    def push(self, id: str, packet: str):
        # Push it to the list
        self.list[id] = packet

    # Function to loop over each packet in queue
    def forEach(self, callback: Callable[[str], None]):
        # Loop over list
        for key in self.list:
            # Send packet to callback
            callback(self.list[key])

    # Remove packet from list
    def remove(self, id: str):
        # Delet the key
        del self.list[id]

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
        self.tasks = EventEmitter()

        # Create event register for subscriptions
        self.subscriptions = EventEmitter()

        # Variable for connection callback
        self.cConnection = None

        # Variable to keep track of ping
        self.ping = None

        # Buffer to store packets temporarily
        self.buffer = buffer()

        # Variable to store valid event names
        self.events = ["data"]

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
                # Backward compatibility
                if data["payload"]["event"] == "deviceParms" or data["payload"]["event"] == "deviceSummary":
                    # Change the event name
                    data["payload"]["event"] = "data"

                # Formulate topic string
                topic = f'{data["payload"]["event"]}/{data["payload"]["path"]}'

                # When the event is data type then use regex method
                # Loop over list of topics
                for sub in self.subscriptions.eventNames():
                    # Event emit where there is a possible match
                    if re.match(sub, topic):
                        # Found a match so emit 
                        self.subscriptions.emit(sub, data["payload"]["update"], data["payload"]["path"])

            else:
                # Emit event and send payload
                self.tasks.emit(data["header"]["id"], data["payload"])

                # Since we have recieved the response so we can now remove
                # the packet from buffer
                if (data["header"]["task"] != "/topic/subscribe"):
                    # If it is not the subscribe packet because we want to keep it
                    self.buffer.remove(data["header"]["id"])

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
        # Loop over packets
        def send(packet):
            # and send to server
            self.ws.send(json.dumps(packet))

        # Call buffer to loop over packets
        self.buffer.forEach(send)

    # Function to send a packet to the server
    def send(self, event: str, payload: dict, callback: Callable[[dict], None]) -> None:
        # Start with generating a new id
        id = time.time()

        # Formulate the packet
        packet = {
            "header": {
                "id": id,
                "task": event
            },
            "payload": payload
        }

        # Add event handler
        self.tasks.once(id, callback)

        # Then if the sdk is connected to the server
        if self.status == "CONNECTED":
            # Then send the packet to the server
            self.ws.send(json.dumps(packet))

        else:
            # or otherwise queue it
            self.buffer.push(id, packet)
    
    # Function to subscribe to an event
    def subscribe(self, event: str, payload: str, callback: Callable[[dict], None]) -> Subscriber:
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

        # Function to handle response of the packet
        def response(data):
            # Place event listener only after getting a response
            self.subscriptions.on(f"{payload['event']}/{payload['path']}", callback)

        # Send the data to the server
        # Start with generating a new id
        id = time.time()

        # Form the packet
        packet = {
            "header": {
                "id": id,
                "task": "/topic/subscribe"
            },
            "payload": payload
        }

        # Add event handler
        self.tasks.once(id, response)

        # Push the packet to queue
        self.buffer.push(id, packet)

        # Then if the sdk is connected to the server
        if self.status == "CONNECTED":
            # Then send the packet to the server
            self.ws.send(json.dumps(packet))

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

            # Remove sub packet from buffer
            self.buffer.remove(id)

            # Send to server
            self.send(packet, c)

        # Append a lambda on close key
        res.clear = clear

        # Return the object
        return res