import socket

port = 8220
address = ('localhost', port)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((address))
server_socket.listen(5)

while True:
	try:
		print("Listening for client . . .")
		conn, address = server_socket.accept()
		print ("Connected to client at ", address)
		#pick a large output buffer size because i dont necessarily know how big the incoming packet is                                                                                              
		output = conn.recv(2048);
		if output:
			print ("Message received from client:")
			print (output.decode())

		#conn.send("This is a response from the server.")                                                                                                                                            
		conn.close()
		#print "Test message sent and connection closed." 
	finally:
		pass