import socket

# Listen on all available network interfaces so Docker can route traffic to this container
HOST = '0.0.0.0'
PORT = 65432

# The `with` block ensures the socket is properly closed even if an error occurs
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Bind the socket to the host/port so it can receive incoming connections
    s.bind((HOST, PORT))

    # Start listening for incoming connections (using default backlog queue size)
    s.listen()
    print(f"Server listening on {HOST}:{PORT}")

    # Block here until a client connects, then return a new socket `conn` for that connection
    # and the client's address as `addr`
    while True:
        conn, addr = s.accept()
    
        with conn:
            print(f"Connected by {addr}")

            # Keep receiving data until the client disconnects
            while True:
                data = conn.recv(1024)  # Receive up to 1024 bytes
                if not data: break      # Empty data means the client closed the connection
                print("received data:", data)
                conn.sendall(data.upper())  # Echo the message back to the client in uppercase
            conn.close()