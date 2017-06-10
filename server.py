import socket               #include socket for networking

serv = socket.socket()      #creating Socket object
host = socket.gethostbyname(socket.gethostname())
port = 10080
serv.bind((host,port))
serv.listen(2)
print "waiting for connection"
serv.accept()
serv.close()