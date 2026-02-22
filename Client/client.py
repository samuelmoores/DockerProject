import socket, time

TCP_IP = "server"
TCP_PORT = 65432

s = None
for attempt in range(5):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((TCP_IP, TCP_PORT))
        print("Connected!")
        break
    except ConnectionRefusedError:
        print("Server not ready, retrying...")
        time.sleep(2)

s.send(b'Hi!')
data = s.recv(1024)
s.close()

print("received data:", data)