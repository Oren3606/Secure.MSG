from socket import *

def verify_peer():
    ...

def register_peer():
    ...

def start(skt:socket): # TODO start two threads, one for sending and one for receiving
    while True:
        msg_otg: str = input("Enter message to send:")
        skt.send(msg_otg.encode())
        print("Message sent:", msg_otg, sep="\n")
        msg_inc:str = skt.recv(1024).decode()
        print("Message received:\n ", msg_inc)

        if msg_otg == "exit" or msg_inc == "exit":
            try:
                skt.close()
                print("Connection closed")
            except error as e:
                print("Connection close failed: ", end="")
                print(e)
            finally:
                break



