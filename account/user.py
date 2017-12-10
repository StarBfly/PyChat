class User:
    def __init__(self, user_data, endpoint_type):
        self._name = user_data.get("name")
        self._surname = user_data.get("surname")
        self._nickname = user_data.get("nickname")
        host = user_data["endpoint"]["host"]
        port = user_data["endpoint"]["port"]
        if endpoint_type is not None:
            self._endpoint = endpoint_type(host, port)

    @property
    def nickname(self):
        return self._nickname

    def send_to(self, message):
        self._endpoint.send_message(message)
