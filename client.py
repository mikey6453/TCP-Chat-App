import socket
import threading

SERVER = socket.gethostbyname(socket.gethostname())
PORT = 55556
ADDRESS = (SERVER, PORT)
FORMAT = "UTF-8"


class ChatClient:
    def __init__(self, nickname):  # Initialization method
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect(ADDRESS)
        self.nickname = nickname

    def receive(self):  # listens for incoming messages all the time
        while True:
            try:
                message = self.client.recv(1024).decode(FORMAT)
                print(message)
            except:
                print("An error occurred!")
                self.client.close()
                break

    def send(self, msg):  # Sends a message
        while True:
            message = f'{self.nickname}: {msg}'
            self.client.send(message.encode(FORMAT))

    def start(self):  # starts the receiving thread
        receive_thread = threading.Thread(target=self.receive)
        receive_thread.start()


if __name__ == "__main__":
    chat_client = ChatClient()
    chat_client.start()