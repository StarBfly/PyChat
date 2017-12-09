#!/usr/bin/python3
from endpoints.endpoint import Endpoint
from threading import Thread, Event
from queue import Queue
import socket

ACCEPT_TIMEOUT = 5
RECEIVE_TIMEOUT = 5
RECEIVE_BUFFER_SIZE = 4096


class ServerEndpointLoop(Thread):
    def __init__(self, host, port, message_queue, stop_event):
        super().__init__()
        self._message_queue = message_queue
        self._connections = []
        self._stop_event = stop_event
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._socket.bind((host, port))
        self._socket.setblocking(0)

    def run(self):
        self._socket.listen(5)

        while not self._stop_event.is_set():
            self._accept_next_connection(ACCEPT_TIMEOUT)
            self._receive_data(RECEIVE_TIMEOUT)
        self._socket.close()

    def _accept_next_connection(self, timeout):
        self._socket.settimeout(timeout)
        try:
            connection, _ = self._socket.accept()
            if connection is not None:
                self._connections.append(connection)
        except:
            pass

    def _receive_data(self, timeout):
        if len(self._connections) > 0:
            self._socket.settimeout(timeout)
        try:
            for connection in self._connections:
                message = connection.recv(RECEIVE_BUFFER_SIZE)
                if message:
                    self._message_queue.put(message)
        except:
            pass


class ServerEndpoint(Endpoint):
    def __init__(self, host, port):
        super(ServerEndpoint, self).__init__(host, port)
        self._message_queue = Queue()
        self._stop_event = Event()
        self._server_endpoint_loop = ServerEndpointLoop(self._host, self._port, self._message_queue, self._stop_event)
        self._server_endpoint_loop.start()

    def __del__(self):
        self._stop_event.set()

    def receive_messages(self):
        result = []
        while self._message_queue.qsize() != 0:
            result.append(self._message_queue.get().decode("utf-8"))
        return result
