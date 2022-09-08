import socket
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 8254
s.bind(("0.0.0.0", port))
s.listen(0)

hostname=socket.gethostname()   
IPAddr=socket.gethostbyname(hostname)   
print("Your Computer Name is:"+hostname)   
print("Your Computer IP Address is:"+IPAddr) 
print(f"Port: {port}")

while True:
    client, addr = s.accept()
    client.settimeout(5)
    while True:
        content = client.recv(10000)
        if len(content) == 0:
            break
        if str(content, "utf-8") == "\r\n":
            continue
        else:
            print(str(content, "utf-8"))
            client.send(b"Hello From Python")
    client.close()
