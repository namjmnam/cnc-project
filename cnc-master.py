import socket
import threading
import os
import psutil

def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_primes(limit):
    """Find all prime numbers up to a given limit."""
    primes = []
    for number in range(2, limit + 1):
        if is_prime(number):
            primes.append(number)
    return primes

class Server:
    def __init__(self, host='192.168.0.74', port=12345):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((host, port))
        self.server_socket.listen(5)
        print(f"Server listening on {host}:{port}")

    def handle_client(self, client_socket):
        # Allocating 10% CPU for each client (this is a placeholder)
        psutil.cpu_percent(10)

        # Perform prime number computation
        limit = 10000  # You can adjust this limit
        primes = find_primes(limit)
        print(primes)
        
        # Optionally, send the result back to the client
        # ...

        # Close the client connection
        client_socket.close()

    def start(self):
        while True:
            client_socket, addr = self.server_socket.accept()
            print(f"Connection from {addr}")
            client_thread = threading.Thread(target=self.handle_client, args=(client_socket,))
            client_thread.start()

if __name__ == "__main__":
    server = Server()
    server.start()
