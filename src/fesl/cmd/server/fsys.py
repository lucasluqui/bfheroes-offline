import logging
from util import packet_encoder
from time import strftime

def handle (self, txn):
    if txn == 'Hello':
        mem_packet = packet_encoder.append('TXN', 'MemCheck')
        mem_packet += packet_encoder.append('memcheck.[]', 0)
        mem_packet += packet_encoder.append('salt', 5, True)
        mem_packet = packet_encoder.encode('fsys', 0xC0000000, mem_packet)
        
        self.pid += 1
        packet = packet_encoder.append('curTime', strftime('%b-%d-%Y %H:%M:%S UTC'))
        packet += packet_encoder.append('messengerIp', '127.0.0.1')
        packet += packet_encoder.append('messengerPort', 13505)
        packet += packet_encoder.append('TXN', 'Hello')
        packet += packet_encoder.append('domainPartition.subDomain', 'bfwest-server')
        packet += packet_encoder.append('theaterIp', '127.0.0.1')
        packet += packet_encoder.append('theaterPort', 18275)
        packet += packet_encoder.append('domainPartition.domain', 'eagames')
        packet += packet_encoder.append('activityTimeoutSecs', 3600, True)
        packet = packet_encoder.encode('fsys', self.pid, packet)

        self.transport.getHandle().sendall(mem_packet)
        self.log.debug(f'[{self.name}] Sent packet=MemCheck')
        self.transport.getHandle().sendall(packet)
        self.log.debug(f'[{self.name}] Sent packet=Hello')

    elif txn == "MemCheck":
        pass

    elif txn == "Goodbye":
        pass