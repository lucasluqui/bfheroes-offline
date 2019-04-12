from twisted.internet.protocol import Protocol, DatagramProtocol
from util import PacketReader
from theater.cmd.client import conn, user, echo

class HANDLER(Protocol):
    def __init__(self):
        self.pid = 0

    def connectionMade(self):
        print("[TCP TheaterClientManager] Got CONNECTION")

    def dataReceived(self, data):
        try:
            command = PacketReader.read_cmd(data).lower()
            print("[TCP TheaterClientManager] cmd="+command.upper())
        except:
            command = None
        if command == "conn":
            conn.handle(self, data)
        if command == "user":
            user.handle(self, data)

class HANDLER_UDP(DatagramProtocol):

    def __init__(self):
        self.pid = 0

    def datagramReceived(self, data, addr):
        try:
            command = PacketReader.read_cmd(data).lower()
            print("[UDP TheaterClientManager] cmd="+command.upper()+",ip="+str(addr[0]))
        except:
            command = None
        if command == "echo":
            echo.handle(self, data, addr)
        else:
            print("[UDP TheaterClientManager] Unknown cmd received, how do I handle this?! cmd="+command)