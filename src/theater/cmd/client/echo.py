from util import PacketEncoder
from util import PacketReader
import time

def handle(self, data, addr):
    EchoPacket = PacketEncoder.append('TID', PacketReader.read_key(data, 'TID'))
    EchoPacket += PacketEncoder.append('TXN', '')
    EchoPacket += PacketEncoder.append('IP', addr[0])
    EchoPacket += PacketEncoder.append('PORT', addr[1])
    EchoPacket += PacketEncoder.append('ERR', 0)
    EchoPacket += PacketEncoder.append('TYPE', 1)
    EchoPacket = PacketEncoder.encode('ECHO', self.pid, EchoPacket)
    self.transport.write(EchoPacket, addr)
    print('[UDP TheaterClientManager] Sent EchoPacket')
