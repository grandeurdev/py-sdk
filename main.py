# Import the library
import grandeurcloud.apollo.device as apollo

# Define the apiKey and Auth token
apiKey = "ck412ssij0007xr239uos8jfk"
token = "eyJ0b2tlbiI6ImV5SmhiR2NpT2lKSVV6STFOaUlzSW5SNWNDSTZJa3BYVkNKOS5leUpwWkNJNkltUmxkbWxqWld0bmJYZHRObVpsTm1KNmJEQXhlV1UwWlhReU1XeHpiU0lzSW5SNWNHVWlPaUprWlhacFkyVWlMQ0pwWVhRaU9qRTJNRE0wT1RZNE16ZDkucGQxNnJJS3BrWnc0MFJYTzlkMG5jdnpTb2YySWdIQzVaOUdQNEtkOWNkOCJ9"

# Event listener on connection state
def onConnection(state):
    # Print the current state
    print(state)

# Callback function to get summary
def handleSummary(data):
    # Print
    print(data)

# Init the SDK and get reference to the project
project = apollo.init(apiKey, token)

# Place listener
project.onConnection(onConnection)

# Get a reference to device class
device = project.device("devicekgmwm6f26bzk01ye1o725t0u")

# Get summary of the device
device.getSummary(handleSummary)

# Block main thread
while 1:
    pass