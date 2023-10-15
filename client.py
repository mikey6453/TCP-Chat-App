import socket

SERVER = socket.gethostbyname(socket.gethostname())
PORT = 55556
ADDRESS = (SERVER, PORT)
FORMAT = "UTF-8"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDRESS)

"""
Client should perform two things: receiving and sending messages to the server
"""

def receive():
    pass



def send():
    pass