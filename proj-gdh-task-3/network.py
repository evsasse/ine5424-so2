class Network:
    @staticmethod
    def send(origin, to, msg):
        print('msg from', origin.exponent, 'to', to.exponent, '=', msg)
        to.receive(msg)
