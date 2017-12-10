from account.message_provider import MessageProvider


class User(MessageProvider):
    def __init__(self, user_data, endpoint_type):
        self._name = user_data.get("name")
        self._surname = user_data.get("surname")
        self._nickname = user_data.get("nickname")
        host = user_data["endpoint"]["host"]
        port = user_data["endpoint"]["port"]
        if endpoint_type is not None:
            self._endpoint = endpoint_type(host, port)
        self._message_filter_predicate = lambda x: True
        self._received_messages = []

    @property
    def nickname(self):
        return self._nickname

    def send_to(self, message):
        self._endpoint.send_message(message)

    @property
    def message_filter_predicate(self):
        return self._message_filter_predicate

    @message_filter_predicate.setter
    def message_filter_predicate(self, predicate):
        self._message_filter_predicate = predicate

    def get_messages(self):
        received_messages = self._endpoint.receive_messages()
        if len(received_messages) > 0:
            self._received_messages.extend(received_messages)
        read_messages = list(filter(self._message_filter_predicate, self._received_messages))
        self._check_read_messages(read_messages)
        return read_messages

    def _check_read_messages(self, read_messages):
        for read_message in read_messages:
            self._received_messages.remove(read_message)
