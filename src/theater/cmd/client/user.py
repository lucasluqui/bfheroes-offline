import time, logging
from util import packet_encoder
from util import packet_reader

def handle(self, data):
    packet = packet_encoder.append('TID', packet_reader.read_key(data, 'TID'))
    packet += packet_encoder.append('NAME', 'lucas')
    packet += packet_encoder.append('CID', '', True)
    packet = packet_encoder.encode('user', self.pid, packet)
    self.transport.getHandle().sendall(packet)
    self.log.debug(f'[{self.name}] Sent packet=user')