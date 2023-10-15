import socket
import threading


SERVER = socket.gethostbyname(socket.gethostname())
PORT = 55555
ADDRESS = (SERVER, PORT)
FORMAT = "UTF-8"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDRESS)  # bind socket to address
server.listen()

clients = []
nicknames = []


def broadcast(message):  # sends message to all connected clients
    for client in clients:
        client.send(message)


def handle_client(client):
    while True:
        try:  # if message receive, broadcast to other clients
            message = client.recv(1024)
            broadcast(message)