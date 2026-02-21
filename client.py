import socket

TCP_IP = '127.0.0.1' #Localhost
TCP_PORT = 65432
MESSAGE = "Hello, World!" #The message to send

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.send(b'Hi!')
data = s.recv(1024)
s.close()
 
print("received data:", data)