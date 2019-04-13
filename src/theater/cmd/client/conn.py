import time, logging
from util import packet_encoder
from util import packet_reader

def handle(self, data):
    packet = packet_encoder.append('TID', packet_reader.read_key(data, 'TID'))
    packet += packet_encoder.append('TIME', str(time.time()).split('.')[0])
    packet += packet_encoder.append('activityTimeoutSecs', 3600)
    packet += packet_encoder.append('PROT', packet_reader.read_key(data, 'PROT'))
    packet = packet_encoder.encode('CONN', self.pid, packet)
    self.transport.getHandle().sendall(packet)
    self.log.debug(f'[{self.name}] Sent packet=CONN')