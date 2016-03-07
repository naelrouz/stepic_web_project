import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 2222))
s.listen(1)
while True:
	conn, addr = s.accept()
	while True:
		data = conn.recv(1024)
		data = data.decode('utf-8')
		if not data: break
		if data == "close":
			#conn.close()
			print("connect is close")
			break
		conn.send(data.encode('utf-8'))
	conn.close()


	# data = conn.recv(1024)
	# data = data.decode('utf-8')
	# if data == "c":
	# 	print("data: c")
	# 	break