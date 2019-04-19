import socket
import sys

HOST, PORT = "localhost", 9999
filename = " ".join(sys.argv[1:])

# Create a socket (SOCK_STREAM means a TCP socket)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    # Connect to server and send data
    sock.connect((HOST, PORT))

    # Open the file and read its contents.
    with open(filename) as f:
        data = f.read()

    # Send the file contents to the server.
    sock.sendall(bytes(data + "\n", "utf-8"))


print("Sent:     {}".format(data))
