import socket
from ftpserver import start_ftp_server
from ftplib import FTP
from PIL import ImageGrab

def start_server():
    # Server configuration
    host = '127.0.0.1'  # Localhost
    port = 12345         # Arbitrary port for the server

    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the server address and port
    server_socket.bind((host, port))

    # Enable the server to accept connections (max 5 clients in the waiting queue)
    server_socket.listen(5)
    print(f"Server started on {host}:{port} and waiting for connections...")

    # Accept a connection from the client
    client_socket, client_address = server_socket.accept()
    print(f"Connected to {client_address}")

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

start_server()