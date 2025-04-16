from socket import *

dest_ip = "127.0.0.1"
dest_port = 1234

external = socket(AF_INET, SOCK_STREAM)
# external.bind((dest_ip, dest_port))

try:
    external.connect((dest_ip, dest_port))
    print("Connected to server")
except error as e:
    print("Connection to server failed: ", end="")
    print(e)

while True:
    msg: str = input("Enter message to send: ")
    if msg == "exit":
        break

    external.send(msg.encode())
    print("Message sent:\n ", msg)


print("Closing connection")
try:
    external.close()
    print("Connection closed")
except error as e:
    print("Connection close failed: ", end="")
    print(e)
