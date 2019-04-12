import logging
from twisted.internet.protocol import Protocol, DatagramProtocol
from util import packet_reader, data_util

class run(Protocol):

    def __init__(self):
        self.name = "(TCP) TheaterServerManager"
        self.pid = 0

    def connectionMade(self):
        self.ip, self.port = self.transport.client
        logging.info(f"[{self.name}] Connection initiated, ip={self.ip}")

    def timeoutConnection(self):
        logging.info(f"[{self.name}] Client timeout, ip={self.ip}")

    def connectionLost(self, reason):
        logging.info(f"[{self.name}] Client lost connection, ip={self.ip}")

    def dataReceived(self, data):
        packets = data_util.read_data(data)
        
        for packet in packets:
            
            txn = packet_reader.read_txn(packet)
            command = packet_reader.read_cmd(packet)
            packet_id = packet_reader.read_pid(packet)
            
            logging.info(f"[{self.name}] command={command}")
            
class run_datagram(DatagramProtocol):

    def __init__(self):
        self.name = "(UDP) TheaterServerManager"
        self.pid = 0

    def datagramReceived(self, data, addr):
        command = packet_reader.read_cmd(data)
        logging.info(f"[{self.name}] command={command},ip={str(addr[0])}")