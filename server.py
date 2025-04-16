from socket import *

orig_ip = "127.0.0.1"
orig_port = 1234

incoming = socket(AF_INET, SOCK_STREAM)

try:
    incoming.bind((orig_ip, orig_port))
except error as e:
    print("Binding failed: ", end="")
    print(e)

incoming.listen()
print("Listening for connections")
conn, addr = incoming.accept()
print("Connection accepted from: ", end="")

while True:
    msg = conn.recv(1024).decode()
    print("Message received:\n ", msg)
    if msg == "exit":
        try:
            conn.close()
            print("Connection closed")
        except error as e:
            print("Connection close failed: ", end="")
            print(e)
        finally:
            break
