#!/usr/bin/python3
from endpoints.client_endpoint import ClientEndpoint


def main():
    endpoint1 = ClientEndpoint("127.0.0.1", 8080)
    endpoint2 = ClientEndpoint("127.0.0.1", 8080)
    endpoint1.send_message("Hello!")
    endpoint2.send_message("Rita!")


if __name__ == "__main__":
    main()
