import socket
import threading
from datetime import datetime

HOST = "0.0.0.0"
PORT = 5000

clients = []
usernames = {}

def timestamp():
    return datetime.now().strftime("[%H:%M:%S]")

def broadcast(message, sender_conn=None):
    for client in clients:
        if client != sender_conn:
            try:
                client.send(message.encode())
            except:
                remove_client(client)

def remove_client(conn):
    if conn in clients:
        username = usernames.get(conn, "Unknown")
        print(f"{username} disconnected")

        clients.remove(conn)
        del usernames[conn]

        broadcast(f"{timestamp()} SERVER: {username} has left the chat.")
        conn.close()

def handle_client(conn, addr):
    print(f"Connection from {addr}")

    try:
        while True:
            data = conn.recv(1024)

            if not data:
                remove_client(conn)
                break

            message = data.decode().strip()

            if message.startswith("JOIN"):
                username = message.split(" ", 1)[1]
                usernames[conn] = username
                clients.append(conn)

                print(f"{username} joined")

                conn.send(f"{timestamp()} SERVER: Welcome to the chat!".encode())
                broadcast(f"{timestamp()} SERVER: {username} joined the chat.", conn)

            elif message.startswith("MSG"):
                text = message.split(" ", 1)[1]
                username = usernames.get(conn, "Unknown")

                ts = timestamp()
                formatted = f"{ts} {username}: {text}"
                print(formatted)
                broadcast(formatted, conn)
                conn.send(formatted.encode())  # Echo back to sender with timestamp

            elif message.startswith("USERS"):
                user_list = ", ".join(usernames.values()) if usernames else "No users online"
                conn.send(f"{timestamp()} SERVER: Online users ({len(usernames)}): {user_list}".encode())

            elif message.startswith("QUIT"):
                remove_client(conn)
                break

    except:
        remove_client(conn)

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()

    print(f"Server running on port {PORT}")

    while True:
        conn, addr = server.accept()

        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()

if __name__ == "__main__":
    start_server()
