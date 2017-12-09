#!/usr/bin/python3
from endpoints.server_endpoint import ServerEndpoint


def main():
    endpoint = ServerEndpoint("127.0.0.1", 8080)
    while True:
        messages = endpoint.receive_messages()
        for message in messages:
            print(message)


if __name__ == "__main__":
    main()
