import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.settimeout(3)

client.connect(("127.0.0.1", 4466))
client.send("testing".encode())
pacotes_recebidos = client.recv(1024).decode()

print("Error connecting")