import socket
from threading import Thread

from ftpserver import start_ftp_server

HOST = '127.0.0.1'  # Localhost
PORT = 12345  # Arbitrary port for the server


def start_server():
    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the server address and port
    server_socket.bind((HOST, PORT))

    # Enable the server to accept connections (max 5 clients in the waiting queue)
    server_socket.listen(5)
    print(f"Server started on {HOST}:{PORT} and waiting for connections...")

    while True:
        # Accept a connection from the client
        client_socket, client_address = server_socket.accept()
        print(f"Connected to {client_address}")
        handle_client_thread = Thread(target=handle_connection, args=[client_socket])
        handle_client_thread.start()


def handle_connection(client_socket: socket.socket):
    # Receive data from the client
    message = client_socket.recv(1024).decode('utf-8')
    print(f"Received from client: {message}")

    if message == 'start':
        client_socket.send("start2".encode('utf-8'))
        start_ftp_server()
        print("ftp started")
        client_socket.send("start2".encode('utf-8'))

    # Close the client socket connection
    client_socket.close()
