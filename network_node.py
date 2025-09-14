"""
Node network structure
"""
'''
toself
idea- peers are real nodes and they connect to the fake network using anonimizing nodes.

essentially- a mixed network with onion routing and encryption.
example of communication:
peer1 encrypts using next.pub->send to corresponding anonimizing node->
fake network propagates encrypted message until reaches anonimizing fake node for peer2-> send to peer2-decrypt->
peer2 encrypts using next.pub->send to corresponding anonimizing node, etc

interesting problem. implement a fake network where peers can never discover each other adn only ever see fake nodes.
2 peers need to be 2 fake nodes apart, to not share the same anonimizing node.
when new user joins more nodes need to be created.

for security, communication is bidirectional, but software should treat them as different nodes.

fake nodes only relay data without decrypting using own key or encrypting using next key
some networknodes may not be linked to a user or have a key

propagation should unpack packet and resend it to obfuscate origin.

for adding into network, user node should ping target and target should return next node
'''

class NetworkNode:
    """
    Represent a node in the network
    """
    def __init__(self):
        """
        Initialize publicly available node type to be accessed by User
        """
        self.key_pub = None
        self.addr: tuple[str, int] = "127.0.0.1", 12345
        self.linked: bool = False
        self.prev: None | NetworkNode = None
        self.next: None | NetworkNode = None

        self._validated: bool = False

    def __str__(self):
        comm = "public key: " + str(self.key_pub) \
        + "address: " + str(self.addr) \
        + "exposed: " + str("") # request from server

        if self.prev:
            comm += "previous: " + str(self.prev.addr)
        else:
            comm += "no previous"
        if self.next:
            comm += "next: " + str(self.next.addr)
        else:
            comm += "no next"

        return comm

    def link(self, node):
        """
        Add node into network
        """
        # todo cheking username can only be done once linked, username validation is impossible
        if self._validated:
            self.prev = node
            self.next = node
        else:
            raise ValueError("Node has not been validated")

    def expose(self):
        """
        Make a node available on server. Replaces current.
        """
        print("Exposing node", str(self.key_pub) + "...", end=" ")
        # todo listen and send pubkey in server
        # todo other things- listen for incoming connections and ping back next fake node
        print("done")

    def _compose_packet(self, text: str):
        """
        Compose packet for sending to another peer
        """
        # todo should hold: timestamp, username, pubkey
        ...

    def _parse_packet(self, packet: bytes):
        """
        Parse received packet
        """
        # should hold: timestamp, username, pubkey
        ...
