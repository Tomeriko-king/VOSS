import socket
import threading

# Function to handle each client
def handle_client(client_socket, client_address):
    print(f"New connection from {client_address}")
    try:
        # Communicating with the client
        client_socket.send("Welcome to the server!".encode('utf-8'))
        while True:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break  # Break if no data is received (client disconnected)
            print(f"Received from {client_address}: {message}")
            response = f"Server echo: {message}"
            client_socket.send(response.encode('utf-8'))
    except Exception as e:
        print(f"Error with {client_address}: {e}")
    finally:
        print(f"Closing connection with {client_address}")
        client_socket.close()


# Main server function
def start_server(host='127.0.0.1', port=65432):
    # Create a TCP/IP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the server address and port
    server_socket.bind((host, port))

    # Listen for incoming connections (max 2 clients)
    server_socket.listen(2)
    print(f"Server started, listening on {host}:{port}")

    # Accept multiple client connections
    while True:
        client_socket, client_address = server_socket.accept()
        # Start a new thread for each client
        client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_thread.daemon = True  # Allow thread to exit when main program exits
        client_thread.start()


# Start the server
if __name__ == "__main__":
    start_server()
