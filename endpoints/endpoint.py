from abc import ABCMeta, abstractmethod


class Endpoint(metaclass=ABCMeta):
    def __init__(self, host, port):
        self._host = host
        self._port = port

    @abstractmethod
    def send_message(self, message):
        pass

    @abstractmethod
    def receive_messages(self):
        pass
