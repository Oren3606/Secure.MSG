"""
Server side logic- make nodes available for new connections, handle node exposing
"""
'''
toself:
hold list of exposed nodes
listen on any new connections on a single socket
find node in list to link new connection to
generate new node for linking
ability to remove nodes from list and add new nods to it, ability to replace exposed node
is it possible to only handle exposure from server side calls?
'''
from socket import socket, AF_INET, SOCK_STREAM
from network_node import NetworkNode
from threading import Thread

exposed_nodes = [] # list of tuples of pubkey and sockets bound to addresses

def expose_node(node: NetworkNode):
    """
    Make node available on server
    """
    ...

def _route_to_node(node: NetworkNode):
    """
    Route traffic to exposed node
    """
    ...
