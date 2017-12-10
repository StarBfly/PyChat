#!/usr/bin/python3
from endpoints.server_endpoint import ServerEndpoint
from account.user import User
from account.messages_listener import MessageListener


def main():
    current_user_data = {
        "name": "Anton",
        "surname": "Pashkouski",
        "nickname": "loh",
        "endpoint": {
            "host": "127.0.0.1",
            "port": 8080
        }
    }
    current_user = User(current_user_data, ServerEndpoint)
    listener = MessageListener(current_user, _print_all_messages)


def _print_all_messages(messages):
    for message in messages:
        print(message)


if __name__ == "__main__":
    main()
