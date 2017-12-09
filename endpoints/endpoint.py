from abc import ABCMeta, abstractmethod


class Endpoint(metaclass=ABCMeta):
    def __init__(self, host, port):
        if host is None or port is None:
            raise ValueError("Host or Port are undefined.")
        self._host = host
        self._port = port

    @abstractmethod
    def send_message(self, message):
        pass

    @abstractmethod
    def receive_messages(self):
        pass
