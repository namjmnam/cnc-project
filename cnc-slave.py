import socket

def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_primes_in_range(start, end):
    """Find all prime numbers within range."""
    primes = []
    for number in range(start, end + 1):
        if is_prime(number):
            primes.append(number)
    return primes

def connect_to_server(host='127.0.0.1', port=12345):
    """Establish a connection to the server."""
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    return client_socket

def main():
    client_socket = connect_to_server()

    try:
        # Receiving range from the server
        data = client_socket.recv(1024).decode()
        start_range, end_range = map(int, data.split('-'))

        # Perform computation
        result = find_primes_in_range(start_range, end_range)
        print(f"Primes in range {start_range}-{end_range}:\n{result}")

        # message = "Done!"
        # client_socket.send(message.encode())

        # Send the result back to the server
        result_str = ','.join(map(str, result))
        client_socket.send(result_str.encode())

    finally:
        # Close the connection
        client_socket.close()

if __name__ == "__main__":
    main()
