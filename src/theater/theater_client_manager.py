import logging
from twisted.internet.protocol import Protocol, DatagramProtocol
from util import packet_reader, data_util
from theater.cmd.client import conn, user, echo

class run(Protocol):
    def __init__(self):
        self.name = "(TCP) TheaterClientManager"
        self.pid = 0
        self.log = logging.getLogger('root')

    def connectionMade(self):
        self.ip, self.port = self.transport.client
        self.log.info(f"[{self.name}] Connection initiated, ip={self.ip}")

    def timeoutConnection(self):
        self.log.info(f"[{self.name}] Client timeout, ip={self.ip}")

    def connectionLost(self, reason):
        self.log.warning(f"[{self.name}] Client lost connection, ip={self.ip}")

    def dataReceived(self, data):
        packets = data_util.read_data(data)
        
        for packet in packets:
            
            txn = packet_reader.read_txn(packet)
            command = packet_reader.read_cmd(packet)
            packet_id = packet_reader.read_pid(packet)
            
            self.log.debug(f"[{self.name}] command={command}")
            
            if command == "CONN":
                conn.handle(self, data=packet)
            elif command == "USER":
                user.handle(self, data=packet)
            else:
                self.log.warning(f"[{self.name}] Unknown command+txn received, how do I handle this?! command={command},txn={txn}")

class run_datagram(DatagramProtocol):

    def __init__(self):
        self.name = "(UDP) TheaterClientManager"
        self.pid = 0
        self.log = logger.getLogger('root')

    def datagramReceived(self, data, addr):
        command = packet_reader.read_cmd(data)
        self.log.debug(f"[{self.name}] command={command},ip={str(addr[0])}")

        if command == "ECHO":
            echo.handle(self, data, addr)
        else:
            self.log.warning(f"[{self.name}] Unknown command received, how do I handle this?! command={command}")