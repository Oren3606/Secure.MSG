from argparse import *
from genericpath import *
from os import *
from pathlib import *
from typing import *
from conn_mgr import *

def is_registered(name:str):
    return False # temp

def add_end(name:str, check:Callable) -> str:
    tmp = name
    i = 1
    while check(tmp):
        tmp = name + str(i)
        i += 1
    
    return tmp

parser = ArgumentParser(
    prog="Secure.MSG",
    usage="secmsg [establish | link] [options]",
    epilog="Secure.MSG is a secure messaging platform",
    description="Secure decentralized messaging platform",
)

parser.add_argument("connection", type=str, help="Connection method", choices=["establish", "link"], default='establish', required=True)
parser.add_argument("--target", "-t", type=str, help="target peer")
parser.add_argument("--name", "-n", type=str, help="Username", default="Peer")
parser.add_argument("--file", "-f", type=str, help="file path", default="")
parser.add_argument("--port", "-p", type=int, nargs=2, help="Port to use, 0 for auto", default=0)
parser.add_argument("--observe", "-o", action="store_true", help="Wehther to only observe non-interactively")

args = parser.parse_args()

user_name = add_end(args.name, is_registered)

filename = args.file
if path.exists(filename):
    if path.isfile(filename):
        filename = add_end(filename, isfile) # todo handle extension
    if path.isdir(args.file):
        filename = add_end(filename + "secmsg_session", isfile)
     
if args.port == 0:
        args.port = 13456 # todo auto

observe = args.observe

addr_ip = args.target
print("addr ip", addr_ip)

if args.connection == "establish":
    print("Establish selected")
    #temp
    args.target = "127.0.0.1"
    print(f"Name: {args.name}")
    print(f"File path: {args.file}")

    addr= (args.target, args.port)
    establish((args.target, args.port))


elif args.connection == "link":
    print(f"Link selected with target: {args.target}")
    print(f"Name: {args.name}")
    print(f"File path: {args.file}")
    link((args.target, args.port))
