import socket
from time import sleep

from ftpclient import clientdt
from ftplib import FTP
from PIL import ImageGrab
from ftpclient import send_png_via_ftp


def start_client():
    # Server configuration
    host = '127.0.0.1'  # Server IP address (localhost in this case)
    port = 12345         # Same port as the server

    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server
    client_socket.connect((host, port))
    print(f"Connected to server at {host}:{port}")

    while True:
        # Send a message to the server
        message = "start"
        client_socket.send(message.encode('utf-8'))

        response = client_socket.recv(1024).decode('utf-8')
        print(response)

        sleep(5)

    # if response == 'start2':
    #     print("received start2")
    #     clientdt()
    #     print("started the client")

    # Close the socket connection
    client_socket.close()

