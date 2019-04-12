class PacketObject():
    def __init__(self, Command, TXN, VAR, length):
        self.Command = Command
        self.TXN = TXN
        self.VAR = VAR
        self.length = length

