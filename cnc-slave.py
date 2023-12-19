import socket

def connect_to_server(host='127.0.0.1', port=12345):
    """Establish a connection to the server."""
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    return client_socket

def perform_computation(data):
    """Perform the assigned computation (this is a placeholder)."""
    # Replace this with the actual computation logic
    # For example, finding prime numbers, etc.
    result = f"Computed result for data: {data}"
    return result

def main():
    client_socket = connect_to_server()

    try:
        # Receiving task or instruction from the server
        data = client_socket.recv(1024).decode()

        # Perform computation
        result = perform_computation(data)

        print(result)

        # Optionally, send the result back to the server
        client_socket.send(result.encode())

    finally:
        # Close the connection
        client_socket.close()

if __name__ == "__main__":
    main()
