from twisted.internet.protocol import Protocol, DatagramProtocol
from util import PacketReader

class HANDLER(Protocol):

    def __init__(self):
        self.pid = 0

    def connectionMade(self):
        print("[TCP TheaterServerManager] Got CONNECTION")

    def dataReceived(self, data):
        packet_buffer = []
        packet_buffer += data.split(b'\n\x00')
        for packet in packet_buffer:
            if packet != b'':
                packet += b'\n\x00'
                try:
                    command = PacketReader.read_cmd(packet).lower()
                    packetid = PacketReader.read_pid(packet)
                    print("[TCP TheaterServerManager] cmd="+command.upper())
                except:
                    command = None
                if False:
                    print('')
                else:
                    print("[TCP TheaterServerManager] Unknown cmd received, how do I handle this?! cmd="+command)
            else:
                continue
            
class HANDLER_UDP(DatagramProtocol):

    def __init__(self):
        self.pid = 0

    def datagramReceived(self, data, addr):
        try:
            command = PacketReader.read_cmd(data).lower()
            print("[UDP TheaterServerManager] cmd="+command.upper()+",ip="+str(addr[0]))
        except:
            command = None
        if False:
            print('')
        else:
            print("[UDP TheaterServerManager] Unknown cmd received, how do I handle this?! cmd="+command)