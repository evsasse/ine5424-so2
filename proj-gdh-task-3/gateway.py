from node import Node
from network import Network


class Gateway(Node):
    def __init__(self, exponent, all_nodes):
        self.exponent = exponent
        self.all_nodes = all_nodes

    def stage_4(self, old_key, origin):
        new_key = self.exponentiation(old_key)
        new_msg = {'key': new_key,
                   'stage': 4}
        Network.send(self, origin, new_msg)

    def receive(self, msg):
        self.stage_4(msg['key'], msg['origin'])
