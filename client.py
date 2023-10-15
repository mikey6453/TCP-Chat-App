import socket

SERVER = socket.gethostbyname(socket.gethostname())
PORT = 55556
ADDRESS = (SERVER, PORT)
FORMAT = "UTF-8"