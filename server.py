import socket
import threading
from queue import Queue

SERVER = socket.gethostbyname(socket.gethostname())
PORT = 55556
ADDRESS = (SERVER, PORT)
FORMAT = "UTF-8"

message_queue = Queue()

clients = []
nicknames = []


class ChatServer:
    def __init__(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind(ADDRESS)  # bind socket to address

    def broadcast(self, message):  # sends message to all connected clients
        for client in clients:
            client.send(message)

    def handle_client(self, client):
        while True:
            try:  # if message receive, broadcast to other clients
                message = client.recv(1024)
                message_queue.put(message.decode(FORMAT))
                self.broadcast(message)
            except:
                index = clients.index(client)
                client.remove(client)
                client.close()
                nickname = nicknames[index]
                self.broadcast(f'{nickname} has left the chat.'.encode(FORMAT))
                nicknames.remove(nickname)
                break

    def start(self):
        self.server.listen()
        while True:
            client, address = self.server.accept()  # accepting clients at all times

            client.send("NICK".encode(FORMAT))
            nickname = client.recv(1024).decode(FORMAT)
            nicknames.append(nickname)
            clients.append(client)
            self.broadcast(f"{nickname} has joined the chat!".encode(FORMAT))  # broadcast that 'nickname' has joined the chat
            client_thread = threading.Thread(target=self.handle_client, args=(client,))
            client_thread.start()


