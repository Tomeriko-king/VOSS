import socket

def start_client(host='127.0.0.1', port=65432):
    # Create a TCP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server
    client_socket.connect((host, port))

    # Receive and print welcome message
    welcome_message = client_socket.recv(1024).decode('utf-8')
    print(welcome_message)

    # Send messages to the server
    while True:
        message = input("Enter message to send to server (or 'exit' to quit): ")
        if message.lower() == 'exit':
            break
        client_socket.send(message.encode('utf-8'))

        # Receive the server's response
        response = client_socket.recv(1024).decode('utf-8')
        print(response)

    # Close the connection
    client_socket.close()


if __name__ == "__main__":
    start_client()
