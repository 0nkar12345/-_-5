import socket

def main():
    """
    Start the chat client.
    """
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("127.0.0.1", 12345))  # Connect to the server
    
    print("[INFO] Connected to the server.")
    while True:
        try:
            message = input("You: ")
            client_socket.send(message.encode('utf-8'))
            reply = client_socket.recv(1024).decode('utf-8')
            if not reply:
                break
            print(f"Server: {reply}")
        except KeyboardInterrupt:
            print("\n[INFO] Connection closed.")
            break
    client_socket.close()

if __name__ == "__main__":
    main()
