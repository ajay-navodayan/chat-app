import socket
import threading

HOST = "127.0.0.1"
PORT = 5000

COMMANDS = {
    "/help":  "Show all available commands",
    "/users": "List all connected users",
    "/quit":  "Disconnect from the chat",
}

def receive_messages(sock):
    while True:
        try:
            message = sock.recv(1024).decode()
            if not message:
                break
            print(message)
        except:
            print("Disconnected from server")
            break

def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))

    username = input("Enter username: ")
    client.send(f"JOIN {username}".encode())

    receive_thread = threading.Thread(target=receive_messages, args=(client,))
    receive_thread.daemon = True
    receive_thread.start()

    while True:
        msg = input()

        if msg == "/quit":
            client.send("QUIT".encode())
            client.close()
            break

        elif msg == "/help":
            print("Available commands:")
            for cmd, desc in COMMANDS.items():
                print(f"  {cmd} - {desc}")

        elif msg == "/users":
            client.send("USERS".encode())

        elif msg.startswith("/"):
            print(f"Unknown command: {msg}  (type /help for available commands)")

        else:
            client.send(f"MSG {msg}".encode())

if __name__ == "__main__":
    start_client()
