import time, logging
from util import packet_encoder
from util import packet_reader

def handle(self, data, addr):
    packet = packet_encoder.append('TID', packet_reader.read_key(data, 'TID'))
    packet += packet_encoder.append('TXN', '')
    packet += packet_encoder.append('IP', addr[0])
    packet += packet_encoder.append('PORT', addr[1])
    packet += packet_encoder.append('ERR', 0)
    packet += packet_encoder.append('TYPE', 1)
    packet = packet_encoder.encode('ECHO', self.pid, packet)
    self.transport.write(packet, addr)
    self.log.debug('[UDP TheaterClientManager] Sent packet=ECHO')
