import socket
import random

while True:
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(("localhost", 8220))
        num = random.randint(0,5)
        if num==3:
            data = "Stress Detected"
            print('send to server: ' + data)
            client_socket.send(bytes(data,'utf-8'))
        else:
            data = "Working Fine"
            print('send to server: ' + data)
            client_socket.send(bytes(data,'utf-8'))
        client_socket.close()
    except Exception as msg:
        print(msg)