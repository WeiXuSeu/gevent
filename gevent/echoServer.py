from gevent.server import StreamServer

def connection_handler(socket, address):
	for link in socket.makefile('r'):
		socket.sendall(link)
		
if __name__ == '__main__':
	server = StreamServer(('127.0.0.1', 8080), connection_handler)
	server.serve_forever()
