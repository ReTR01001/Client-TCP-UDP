import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    while True:
        msg = input("Message: ") + "\n"
        client.sendto(msg.encode(), ("127.0.0.1", 4433))
        data, sender = client.recvfrom(1024)
        print(sender[0] + ": " + data.decode())
except Exception as e:
    print("Error connecting")
    print(e)