#!/usr/bin/python3
from endpoints.server_endpoint import ServerEndpoint


def main():
    endpoint = ServerEndpoint("127.0.0.1", "8080")


if __name__ == "__main__":
    main()
