import socket

def start_server():
    # Set up the server
    host = '127.0.0.1'  # Localhost
    port = 65432  # Port to bind the server

    # Create a socket and bind it to the host and port
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)

    print("Server is waiting for a connection...")

    try:
        # Accept incoming connections
        conn, addr = server_socket.accept()
        print(f"Connected by {addr}")

        # Send a message to the client
        message = "Hello from server!"
        conn.sendall(message.encode('utf-8'))

        # Close the connection
        conn.close()

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        server_socket.close()

if __name__ == "__main__":
    start_server()



import socket

def start_client():
    # Set up the client
    host = '127.0.0.1'  # Localhost
    port = 65432  # Port to connect to

    try:
        # Create a socket and connect to the server
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((host, port))

        # Receive the message from the server
        message = client_socket.recv(1024).decode('utf-8')

        print(f"Message from server: {message}")

        # Close the connection
        client_socket.close()

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    start_client()
