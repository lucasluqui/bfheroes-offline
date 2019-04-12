from util import PacketEncoder
from util import PacketReader
import time

def handle(self, data):
    UserPacket = PacketEncoder.append('TID', PacketReader.read_key(data, 'TID'))
    UserPacket += PacketEncoder.append('NAME', 'lucas')
    UserPacket += PacketEncoder.append('CID', '', True)
    UserPacket = PacketEncoder.encode('user', self.pid, UserPacket)
    self.transport.getHandle().sendall(UserPacket)
    print('[TheaterClientManager] Sent UserPacket')