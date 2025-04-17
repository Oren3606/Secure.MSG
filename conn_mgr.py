from socket import *
from  session import *

skt = socket(AF_INET, SOCK_STREAM)

def establish(inc_addr:tuple[str, int]):
    try:
        skt.bind(inc_addr)
        print("Socket bound to:", inc_addr, end="")

    except error as e:
        print("Binding failed: ", end="")

    while True:
        print("Listening for connections")
        skt.listen()

        conn, addr = skt.accept()
        print("Connection accepted from:", conn, end="")

        start(conn)

def link(otg_addr:tuple[str, int]):    
    try:
        skt.connect(otg_addr)
        print("Connected to server")
    except error as e:
        print("Connection to server failed:", end="")
        print(e)

    start(skt)    

def _get_params(addr: tuple[str, int], name:str, file:str, port:int, observe:bool):
    raise NotImplementedError("This function is not implemented yet")
