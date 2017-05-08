from network import Network


class Node:
    def __init__(self, exponent, next_node, gateway):
        self.exponent = exponent
        self.next_node = next_node
        self.gateway = gateway

    def stage_1(self, old_key):
        new_key = self.exponentiation(old_key)
        new_msg = {'key': new_key,
                   'stage': 1}
        Network.send(self, self.next_node, new_msg)

    def stage_2(self, old_key):
        new_key = self.exponentiation(old_key)
        new_msg = {'key': new_key,
                   'stage': 2}
        for node in self.next_node:
            Network.send(self, node, new_msg)

    def stage_3(self, old_key):
        new_key = self.factor_out(old_key)
        new_msg = {'key': new_key,
                   'origin': self,
                   'stage': 3}
        Network.send(self, self.gateway, new_msg)

    def stage_4(self, old_key):
        new_key = self.exponentiation(old_key)
        self.group_key = new_key
        print(self.exponent, 'calculated group key', new_key)

    def receive(self, msg):
        if msg['stage'] is 1:
            if type(self.next_node) is list:
                self.stage_2(msg['key'])
            else:
                self.stage_1(msg['key'])
        elif msg['stage'] is 2:
            self.stage_3(msg['key'])
        elif msg['stage'] is 4:
            self.stage_4(msg['key'])

    def exponentiation(self, old_key):
        return old_key+[self.exponent]

    def factor_out(self, old_key):
        new_key = list(old_key)
        new_key.remove(self.exponent)
        return new_key
