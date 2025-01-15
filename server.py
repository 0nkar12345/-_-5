import socket
import threading

def handle_client(client_socket, client_address):
    """
    Handle incoming messages from the client.
    """
    print(f"[INFO] Connected to {client_address}")
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break
            print(f"Client: {message}")
            reply = input("You: ")
            client_socket.send(reply.encode('utf-8'))
        except ConnectionResetError:
            print("[INFO] Connection closed by client.")
            break
    client_socket.close()

def main():
    """
    Start the chat server.
    """
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("127.0.0.1", 12345))  # Localhost and port
    server_socket.listen(1)
    print("[INFO] Server started and waiting for a connection...")
    
    client_socket, client_address = server_socket.accept()
    handle_client(client_socket, client_address)

if __name__ == "__main__":
    main()
