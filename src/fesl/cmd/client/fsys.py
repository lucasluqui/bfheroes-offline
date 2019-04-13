import time, logging
from util import packet_encoder
from time import strftime

def handle(self, txn):
    if txn == "Hello":
        mem_packet = packet_encoder.append('TXN', 'MemCheck')
        mem_packet += packet_encoder.append('memcheck.[]', 0)
        mem_packet += packet_encoder.append('salt', 5, True)
        mem_packet = packet_encoder.encode('fsys', 0xC0000000, mem_packet)

        session_packet = packet_encoder.append('TXN', 'GetSessionId', True)
        session_packet = packet_encoder.encode('gsum', 0x0, session_packet)

        self.pid += 1
        packet = packet_encoder.append('curTime', strftime('%b-%d-%Y %H:%M:%S UTC'))
        packet += packet_encoder.append('messengerIp', '127.0.0.1')
        packet += packet_encoder.append('messengerPort', 13505)
        packet += packet_encoder.append('TXN', 'Hello')
        packet += packet_encoder.append('domainPartition.subDomain', 'bfwest-dedicated')
        packet += packet_encoder.append('theaterIp', '127.0.0.1')
        packet += packet_encoder.append('theaterPort', 18275)
        packet += packet_encoder.append('domainPartition.domain', 'eagames')
        packet += packet_encoder.append('activityTimeoutSecs', 3600, True)
        packet = packet_encoder.encode('fsys', self.pid, packet)

        self.transport.getHandle().sendall(mem_packet)
        self.log.debug('[FESLClientManager] Sent packet=MemCheck')
        self.transport.getHandle().sendall(session_packet)
        self.log.debug('[FESLClientManager] Sent packet=GetSessonId')
        self.transport.getHandle().sendall(packet)
        self.log.debug('[FESLClientManager] Sent packet=Hello')

    elif txn == "MemCheck":
        pass

    elif txn == "Goodbye":
        pass

    elif txn == "GetPingSites":
        self.pid += 1
        packet = packet_encoder.append('TXN', 'GetPingSites')
        packet += packet_encoder.append('minPingSitesToPing', 2)
        packet += packet_encoder.append('pingSites.[]', 2)
        packet += packet_encoder.append('pingSites.0.addr', '127.0.0.1')
        packet += packet_encoder.append('pingSites.0.name', 'gva')
        packet += packet_encoder.append('pingSites.0.type', 0)
        packet += packet_encoder.append('pingSites.1.addr', '127.0.0.1')
        packet += packet_encoder.append('pingSites.1.name', 'nrt')
        packet += packet_encoder.append('pingSites.1.type', 0)
        packet = packet_encoder.encode('fsys', self.pid, packet)
        self.transport.getHandle().sendall(packet)
        self.log.debug('[FESLClientManager] Sent packet=GetPingSites')

    else:
        pass