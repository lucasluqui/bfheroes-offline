from util import PacketEncoder
from util import PacketReader
import time

def handle(self, data):
    ConnPacket = PacketEncoder.append('TID', PacketReader.read_key(data, 'TID'))
    ConnPacket += PacketEncoder.append('TIME', str(time.time()).split('.')[0])
    ConnPacket += PacketEncoder.append('activityTimeoutSecs', 3600)
    ConnPacket += PacketEncoder.append('PROT', PacketReader.read_key(data, 'PROT'))
    ConnPacket = PacketEncoder.encode('CONN', self.pid, ConnPacket)
    self.transport.getHandle().sendall(ConnPacket)
    print('[TheaterClientManager] Sent ConnPacket')