import socket
import threading


SERVER = socket.gethostbyname(socket.gethostname())
PORT = 55556
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
        except:
            index = clients.index(client)
            client.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast(f'{nickname} has left the chat.'.encode(FORMAT))
            nicknames.remove(nickname)
            break


def start():
    while True:
        client, address = server.accept()  # accepting clients at all times
        print(f"Connected with {str(address)}")

        client.send("NICK".encode(FORMAT))
        nickname = client.recv(1024).decode(FORMAT)
        nicknames.append(nickname)
        clients.append(client)

        print(f"Nickname of the client is {nickname}")
        broadcast(f"{nickname} has joined the chat!".encode(FORMAT))  # broadcast that 'nickname' has joined the chat
        client.send('Connected to the server!'.encode(FORMAT))  # msg to the individual client

        client_thread = threading.Thread(target=handle_client, args=(client,))
        client_thread.start()

start()