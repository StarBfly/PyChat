#!/usr/bin/python3
from endpoints.endpoint import Endpoint
import socket


class ClientEndpoint(Endpoint):
    def __init__(self, host, port):
        super(ClientEndpoint, self).__init__(host, port)
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._socket.connect((self._host, self._port))

    def __del__(self):
        self._socket.close()

    def send_message(self, message):
        if message is None:
            raise ValueError('Message is not defined.')
        self._socket.send(message.encode('utf-8'))

    def receive_messages(self):
        pass
