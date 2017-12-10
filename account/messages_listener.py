from threading import Timer


LISTERNING_INTERVAL = 5


class MessageListener:
    def __init__(self, message_provider, on_receive_callback):
        self._message_provider = message_provider
        self._on_receive_callback = on_receive_callback
        self._start_timer()

    def _listen(self):
        messages = self._message_provider.get_messages()
        if len(messages) > 0:
            self._on_receive_callback(messages)
        self._start_timer()

    def _start_timer(self):
        self._timer = Timer(LISTERNING_INTERVAL, self._listen)
        self._timer.start()
