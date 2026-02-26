import socket, time

# The hostname "server" refers to the server container's service name in docker-compose.yml,
# which Docker's internal DNS resolves automatically
TCP_IP = "server"
TCP_PORT = 65432

s = None
# Retry loop — the client may start before the server container is ready,
# so we attempt to connect up to 5 times before giving up
for attempt in range(5):
    try:
        # Create a TCP socket (AF_INET = IPv4, SOCK_STREAM = TCP)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((TCP_IP, TCP_PORT))
        print("Connected!")
        break  # Exit the retry loop on successful connection
    except ConnectionRefusedError:
        # Server isn't listening yet — wait 2 seconds before retrying
        print("Server not ready, retrying...")
        time.sleep(2)

if s is None:
    print("Could not connect to server.")
    exit(1)

# Send a message to the server (must be bytes, not a string)
s.send(b'Hi!')

# Wait to receive the server's response (up to 1024 bytes)
data = s.recv(1024)
s.close()

print("received data:", data)