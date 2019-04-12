from util import PacketEncoder
from time import strftime
import time

def handle(self, txn):
    if txn == "hello":
        MemCheckPacket = PacketEncoder.append('TXN', 'MemCheck')
        MemCheckPacket += PacketEncoder.append('memcheck.[]', 0)
        MemCheckPacket += PacketEncoder.append('salt', 5, True)
        MemCheckPacket = PacketEncoder.encode('fsys', 0xC0000000, MemCheckPacket)
        GetSessionIdPacket = PacketEncoder.append('TXN', 'GetSessionId', True)
        GetSessionIdPacket = PacketEncoder.encode('gsum', 0x0, GetSessionIdPacket)
        self.pid += 1
        HelloPacket = PacketEncoder.append('curTime', strftime('%b-%d-%Y %H:%M:%S UTC'))
        HelloPacket += PacketEncoder.append('messengerIp', '127.0.0.1')
        HelloPacket += PacketEncoder.append('messengerPort', 13505)
        HelloPacket += PacketEncoder.append('TXN', 'Hello')
        HelloPacket += PacketEncoder.append('domainPartition.subDomain', 'bfwest-dedicated')
        HelloPacket += PacketEncoder.append('theaterIp', '127.0.0.1')
        HelloPacket += PacketEncoder.append('theaterPort', 18275)
        HelloPacket += PacketEncoder.append('domainPartition.domain', 'eagames')
        HelloPacket += PacketEncoder.append('activityTimeoutSecs', 3600, True)
        HelloPacket = PacketEncoder.encode('fsys', self.pid, HelloPacket)

        self.transport.getHandle().sendall(MemCheckPacket)
        print('[FESLClientManager] Sent MemCheckPacket')
        self.transport.getHandle().sendall(GetSessionIdPacket)
        print('[FESLClientManager] Sent GetSessonIdPacket')
        self.transport.getHandle().sendall(HelloPacket)
        print('[FESLClientManager] Sent HelloPacket')

    elif txn == "memcheck":
        pass

    elif txn == "goodbye":
        pass

    elif txn == "getpingsites":
        self.pid += 1
        GetPingSitesPacket = PacketEncoder.append('TXN', 'GetPingSites')
        GetPingSitesPacket += PacketEncoder.append('minPingSitesToPing', 2)
        GetPingSitesPacket += PacketEncoder.append('pingSites.[]', 2)
        GetPingSitesPacket += PacketEncoder.append('pingSites.0.addr', '127.0.0.1')
        GetPingSitesPacket += PacketEncoder.append('pingSites.0.name', 'gva')
        GetPingSitesPacket += PacketEncoder.append('pingSites.0.type', 0)
        GetPingSitesPacket += PacketEncoder.append('pingSites.1.addr', '127.0.0.1')
        GetPingSitesPacket += PacketEncoder.append('pingSites.1.name', 'nrt')
        GetPingSitesPacket += PacketEncoder.append('pingSites.1.type', 0)
        GetPingSitesPacket = PacketEncoder.encode('fsys', self.pid, GetPingSitesPacket)
        self.transport.getHandle().sendall(GetPingSitesPacket)
        print('[FESLClientManager] Sent GetPingSitesPacket')

    else:
        pass