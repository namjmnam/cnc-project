import socket
import threading
import os
import sys
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

def find_primes_range(start, end):
    """Find all prime numbers within range."""
    primes = []
    for number in range(start, end + 1):
        if is_prime(number):
            primes.append(number)
    return primes

class Server:
    def __init__(self, host='127.0.0.1', port=12345):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((host, port))
        self.server_socket.listen(5)
        self.client_count = 0
        self.is_running = True
        print(f"Server listening on {host}:{port}")

    def handle_client(self, client_socket, client_id):
        # Allocating 10% CPU for each client (this is a placeholder)
        psutil.cpu_percent(10)

        # Tell clients to compute
        interval = 2500
        start_range = client_id * interval + 1
        end_range = start_range + interval - 1
        primes = find_primes_range(start_range, end_range)
        print(primes)

        # Send a message
        message = "Thanks!"
        client_socket.send(message.encode())

        # Close the client connection
        client_socket.close()

    def start(self):
        while self.is_running:
            client_socket, addr = self.server_socket.accept()
            print(f"Connection from {addr}")

            client_id = self.client_count
            self.client_count += 1
            print(client_id)

            client_thread = threading.Thread(target=self.handle_client, args=(client_socket, client_id))
            client_thread.start()

    def stop(self):
        self.is_running = False
        self.server_socket.close()
        print("Server stopped.")

def listen_for_quit_command(server):
    while True:
        cmd = input()
        if cmd == 'quit':
            server.stop()
            break

if __name__ == "__main__":
    server = Server()
    quit_thread = threading.Thread(target=listen_for_quit_command, args=(server,))
    quit_thread.start()
    server.start()
