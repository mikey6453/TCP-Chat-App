# TCP-Chat-App


This is a simple command-line TCP chat application that allows multiple clients to connect to a server and exchange messages in a chat room. The application uses Python and the socket library for network communication, along with threading for concurrent client handling.

# Features
- Multiple clients can connect to a central server.
- Clients can choose their own nicknames.
- Messages sent by clients are broadcasted to all connected clients.
- The server notifies when a client joins or leaves the chat room.

# Usage
Server
- Run the server script to start the chat server. The server will listen for incoming connections on a specified port (default is 55556).
- You can customize the server port by modifying the PORT variable in the server.py script.
- The server will display information about incoming connections and chat activity.

Client
- Run the client script to connect to the chat server. Provide a unique nickname when prompted.
- Start typing messages to send them to the chat room. Your messages will be broadcasted to all connected clients.

To exit the chat, simply close the client application.

# Implementation Details
- The server listens for incoming connections and creates a new thread for each connected client.
- Clients choose their nicknames, and the server broadcasts messages to all clients.
- The server also handles disconnections and updates the chat room accordingly.


# Dependencies
Python 3.x

# Author
Michael Park
