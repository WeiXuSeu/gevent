import socket
s = socket.socket()
url = 'www.google.com'
port = 80
s.connect((url, port))
print("We are connected to %s: %d", s.getpeername())
