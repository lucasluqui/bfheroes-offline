import logging
from twisted.internet.protocol import Protocol
from util import packet_reader, data_util
from fesl.cmd.server import fsys, acct

class run(Protocol):

    def __init__(self):
        self.name = "FESLServerManager"
        self.pid = 0

    def connectionMade(self):
        self.ip, self.port = self.transport.client
        print(f"[{self.name}] Connection initiated, ip={self.ip}")

    def timeoutConnection(self):
        print(f"[{self.name}] Client timeout, ip={self.ip}")

    def connectionLost(self, reason):
        print(f"[{self.name}] Client lost connection, ip={self.ip}")

    def readConnectionLost(self):
        self.transport.loseConnection()

    def writeConnectionLost(self):
        print(f"[{self.name}] Closing client connection, ip={self.ip}")
        self.transport.loseConnection()

    def dataReceived(self, data):
        packets = data_util.read_data(data)
        
        for packet in packets:
            
            txn = packet_reader.read_txn(packet)
            command = packet_reader.read_cmd(packet)
            packet_id = packet_reader.read_pid(packet)
            
            logging.info(f"[{self.name}] command={command},txn={txn}")
            
            if command == "fsys":
                fsys.handle(self, txn=txn)
            elif command == "acct":
                acct.handle(self, txn=txn)
            else:
                logging.warning(f"[{self.name}] Unknown command+txn received, how do I handle this?! command={command},txn={txn}")