from twisted.internet.protocol import Protocol, DatagramProtocol
from util import PacketReader

class HANDLER(Protocol):
    def __init__(self):
        self.pid = 0

    def connectionMade(self):
        print("[Kerberos] Got CONNECTION")

    def dataReceived(self, data):
        try:
            print(data)
            command = PacketReader.read_cmd(data)
            print("[Kerberos] cmd="+command.upper()+",ip="+self.ip)
        except:
            command = None

class HANDLER_UDP(DatagramProtocol):

    def __init__(self):
        self.pid = 0

    def datagramReceived(self, data):
        try:
            print(data)
            command = PacketReader.read_cmd(data)
            print(command)
        except:
            command = None