# Chat Application

A simple TCP-based multi-client chat application built in Python using sockets and threading.

## Features

- Multi-client support — multiple users can connect simultaneously
- Timestamped messages — every message includes a `[HH:MM:SS]` timestamp
- Username identification — each client joins with a display name
- Built-in commands — type `/help` to see all available commands

## Commands

| Command  | Description                      |
|----------|----------------------------------|
| `/help`  | Show all available commands      |
| `/users` | List all currently connected users |
| `/quit`  | Disconnect from the chat         |

## Project Structure

```
chat-app/
├── server/
│   └── server.py   # TCP server — handles connections and message routing
├── client/
│   └── client.py   # TCP client — sends/receives messages
└── README.md
```

## How to Run

### Start the server

```bash
python server/server.py
```

### Connect a client

```bash
python client/client.py
```

Enter a username when prompted. Open multiple terminals to simulate multiple users.

## Example Session

```
Enter username: Ajay
[14:05:01] SERVER: Welcome to the chat!
[14:05:10] SERVER: Ajay joined the chat.
[14:05:15] Ritik: Hey Ajay
[14:05:20] Ajay: Hi Ritik
```

## Requirements

- Python 

