from util import PacketEncoder
from time import strftime

def handle (self, txn):
    if txn == 'hello':
        MemCheckPacket = PacketEncoder.append('TXN', 'MemCheck')
        MemCheckPacket += PacketEncoder.append('memcheck.[]', 0)
        MemCheckPacket += PacketEncoder.append('salt', 5, True)
        MemCheckPacket = PacketEncoder.encode('fsys', 0xC0000000, MemCheckPacket)
        self.pid += 1
        HelloPacket = PacketEncoder.append('curTime', strftime('%b-%d-%Y %H:%M:%S UTC'))
        HelloPacket += PacketEncoder.append('messengerIp', '127.0.0.1')
        HelloPacket += PacketEncoder.append('messengerPort', 13505)
        HelloPacket += PacketEncoder.append('TXN', 'Hello')
        HelloPacket += PacketEncoder.append('domainPartition.subDomain', 'bfwest-server')
        HelloPacket += PacketEncoder.append('theaterIp', '127.0.0.1')
        HelloPacket += PacketEncoder.append('theaterPort', 18275)
        HelloPacket += PacketEncoder.append('domainPartition.domain', 'eagames')
        HelloPacket += PacketEncoder.append('activityTimeoutSecs', 3600, True)
        HelloPacket = PacketEncoder.encode('fsys', self.pid, HelloPacket)

        self.transport.getHandle().sendall(MemCheckPacket)
        print('[FESLServerManager] Sent MemCheckPacket')
        self.transport.getHandle().sendall(HelloPacket)
        print('[FESLServerManager] Sent HelloPacket')

    elif txn == "memcheck":
        pass

    elif txn == "goodbye":
        pass