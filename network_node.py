"""
Set up a new session, handle new peers, propagate messages through DHT, manage network nodes
"""
'''
toself
fake nodes need to be hosted as servers outside of real users' control (after router=after isp)
that could make it easier to id fake nodes from real ones
todo - how to make normal
'''

class NetworkNode:
    """
    Represent a node in the network
    """
    def __init__(self):
        self.exposed: bool = False # to be used with Session.expose_node() and Session.hide_node()
        self.key_pub = None # pub key
        self.next_addr: tuple[str, int] = ("127.0.0.1", 0) # next node address address, port

        self._validated: bool = False

    def establish(self):
        if self._validated:
            ...

    def link(self):
        if self._validated:
            ...

    def expose_node(self):
        """
        Make a node available on server. Replaces current
        """
        print("Exposing node", str(self.key_pub) + "...", end=" ")
        self.exposed_node = self
        # todo other things
        print("done")

    def hide_node(self):
        """
        Revoke node (and thus session) availability on server
        """
        self.exposed_node = None
        # todo other things

    def compose_packet(self, text: str):
        """
        Compose packet for sending to another peer
        """
        # should hold: timestamp, username, pubkey
        text
        # todo

    def parse_packet(self, packet: bytes):
        """
        Parse received packet
        """
        # should hold: timestamp, username, pubkey
        ...

    def _blend(self):
        # todo make packets come from a different node as to not expose real user ip
        ...
