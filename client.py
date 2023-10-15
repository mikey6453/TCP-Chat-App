import socket
import threading

SERVER = socket.gethostbyname(socket.gethostname())
PORT = 55556
ADDRESS = (SERVER, PORT)
FORMAT = "UTF-8"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDRESS)

nickname = input("What is your nickname? ")

"""
Client should perform two things: receiving and sending messages to the server
"""


def receive():
    while True:
        try:
            message = client.recv(1024).decode(FORMAT)
            if message == "NICK":
                client.send(nickname.encode(FORMAT))
            else:
                print(message)
        except:
            print("An error occurred!")
            client.close()
            break


def send():
    while True:
        message = f'{nickname}: {input("")}'
        client.send(message.encode(FORMAT))


receive_thread = threading.Thread(target=receive)
receive_thread.start()

send_thread = threading.Thread(target=send)
send_thread.start()



