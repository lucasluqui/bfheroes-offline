from twisted.internet.protocol import Protocol
from util import PacketReader
from fesl.cmd.server import fsys, acct

class HANDLER(Protocol):

    def __init__(self):
        self.pid = 0

    def connectionMade(self):
        self.ip, self.port = self.transport.client
        print("[FESLServerManager] Got CONNECTION from: " + self.ip)

    def timeoutConnection(self):
        print("[FESLServerManager] Timeout ip="+self.ip)

    def connectionLost(self, reason):
        print("[FESLServerManager] Lost connection ip="+self.ip)

    def readConnectionLost(self):
        self.transport.loseConnection()

    def writeConnectionLost(self):
        print("[FESLServerManager] Closing connection ip="+self.ip)
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
                        print("[FESLServerManager] cmd="+command.upper()+",ip="+self.ip)
                        print("[FESLServerManager] txn="+txn.upper()+",ip="+self.ip)
                    except:
                        command = None
                        txn = None
                    if command == 'fsys':
                        fsys.handle(self, txn=txn)
                    elif command == 'acct':
                        acct.handle(self, txn=txn)
                    else:
                        print("[FESLServerManager] Unknown cmd+txn received, how do I handle this?! cmd="+command+",txn="+txn)
                else:
                    continue
            else:
                continue