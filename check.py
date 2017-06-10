import socket

print socket.gethostname()
port = 10080
cli = socket.connect((socket.gethostname(),port))