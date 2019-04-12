from twisted.internet.protocol import Protocol
from util import PacketReader
from fesl.cmd.client import fsys, acct, rank

class HANDLER(Protocol):

    def __init__(self):
        self.login_key = None
        self.pid = 0

    def connectionMade(self):
        self.ip, self.port = self.transport.client
        print("[FESLClientManager] Got CONNECTION from: " + self.ip)

    def timeoutConnection(self):
        print("[FESLClientManager] Timeout ip="+self.ip)

    def connectionLost(self, reason):
        print("[FESLClientManager] Lost connection ip="+self.ip)

    def readConnectionLost(self):
        self.transport.loseConnection()

    def writeConnectionLost(self):
        print("[FESLClientManager] Closing connection ip="+self.ip)
        self.transport.loseConnection()

    def dataReceived(self, data):
        packet_buffer = []
        packet_buffer += data.split(b'\n\x00')
        for packet in packet_buffer:
            if packet != b'':
                packet += b'\n\x00'
                txn = PacketReader.read_txn(packet)
                if txn != None:
                    try:
                        command = PacketReader.read_cmd(packet).lower()
                        txn = txn.lower()
                        packetid = PacketReader.read_pid(packet)
                        print("[FESLClientManager] cmd="+command.upper()+",ip="+self.ip)
                        print("[FESLClientManager] txn="+txn.upper()+",ip="+self.ip)
                    except:
                        command = None
                        txn = None
                    if command == "fsys":
                        fsys.handle(self, txn=txn)
                    elif command == "acct":
                        acct.handle(self, txn=txn)
                    elif command == "rank":
                        rank.handle(self, txn=txn, data=packet)
                    # Required workaround to handle a strange packet received after ACCT NuLoginPersona
                    # where \n\x00 is found in the middle of the packet, making it hard to work with.
                    elif len(command.split()) > 0:
                        packet = b'rank\xc0\x00\x00\n\x00'+packet
                        txn = PacketReader.read_txn(packet).lower()
                        rank.handle(self, txn=txn, data=packet)
                    else:
                        print("[FESLClientManager] Unknown cmd+txn received, how do I handle this?! cmd="+command+",txn="+txn)
                else:
                    continue
            else:
                continue