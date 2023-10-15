import socket
import threading

SERVER = socket.gethostbyname(socket.gethostname())  # local host
PORT = 5050
ADDRESS = (SERVER, PORT)
FORMAT = "UTF-8"

