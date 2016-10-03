"""
File: chatserver.py
Project 10.5

Server for a multi-client chat room.
The the chat record loads itself from a text file.  When each
message is added to the record, it is also saved to the file.
"""

from socket import *
from codecs import decode
from chatrecord import ChatRecord
from threading import Thread
from time import ctime

class ClientHandler(Thread):
    
    def __init__(self, client, record):
        Thread.__init__(self)
        self._client = client
        self._record = record

    def run(self):
        self._client.send(bytes('Welcome to the chat room!', CODE))
        self._name = decode(self._client.recv(BUFSIZE), CODE)
        self._client.send(bytes(str(self._record), CODE))
        while True:
            message = decode(self._client.recv(BUFSIZE), CODE)
            if not message:
                print('Client disconnected')
                self._client.close()
                break
            else:
                message = self._name + ' ' + \
                          ctime() + '\n' + message
                # add will also save this message to the file
                self._record.add(message)
                self._client.send(bytes(str(self._record), CODE))


HOST = 'localhost'
PORT = 5000
ADDRESS = (HOST, PORT)
BUFSIZE = 1024
CODE = 'ascii'

# The record is now loaded from a file
record = ChatRecord("record.txt")
server = socket(AF_INET, SOCK_STREAM)
server.bind(ADDRESS)
server.listen(5)

while True:
    print('Waiting for connection . . .')
    client, address = server.accept()
    print('... connected from:', address)
    handler = ClientHandler(client, record)
    handler.start()

