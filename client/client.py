import socket
import threading

HOST = "127.0.0.1"
PORT = 5000

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
    receive_thread.start()

    while True:
        msg = input()

        if msg == "/quit":
            client.send("QUIT".encode())
            client.close()
            break

        client.send(f"MSG {msg}".encode())

if __name__ == "__main__":
    start_client()