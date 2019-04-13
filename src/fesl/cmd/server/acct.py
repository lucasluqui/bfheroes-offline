import logging
from util import packet_encoder, string_util

def handle(self, txn):
    if txn == 'NuLogin':
        self.pid += 1
        self.login_key = string_util.random_str(24)
        packet = packet_encoder.append('TXN', 'NuLogin')
        packet += packet_encoder.append('lkey', self.login_key)
        packet += packet_encoder.append('nuid', 'test-server')
        packet += packet_encoder.append('profileId', '1000')
        packet += packet_encoder.append('userId', '1000')
        packet = packet_encoder.encode('acct', self.pid, packet)
        self.transport.getHandle().sendall(packet)
        self.log.debug(f'[{self.name}] Sent packet=NuLogin')
    
    elif txn == 'NuGetPersonas':
        self.pid += 1
        packet = packet_encoder.append('TXN', 'NuGetPersonas')
        packet += packet_encoder.append('personas.[]', 0)
        packet = packet_encoder.encode('acct', self.pid, packet)
        self.transport.getHandle().sendall(packet)
        self.log.debug(f'[{self.name}] Sent packet=NuGetPersonas')

    elif txn == 'NuGetAccount':
        self.pid += 1
        packet = packet_encoder.append('TXN', 'NuGetAccount')
        packet += packet_encoder.append('heroName', 'test-server')
        packet += packet_encoder.append('nuid', 'test-server@test.com')
        packet += packet_encoder.append('DOBDay', '1')
        packet += packet_encoder.append('DOBMonth', '1')
        packet += packet_encoder.append('DOBYear', '2017')
        packet += packet_encoder.append('userId', '1000')
        packet += packet_encoder.append('globalOptin', '0')
        packet += packet_encoder.append('thidPartyOptin', '0')
        packet += packet_encoder.append('language', 'enUS')
        packet += packet_encoder.append('country', 'US')
        packet = packet_encoder.encode('acct', self.pid, packet)
        self.transport.getHandle().sendall(packet)
        self.log.debug(f'[{self.name}] Sent packet=NuGetAccount')

    elif txn == 'NuLoginPersona':
        packet = packet_encoder.append('TXN', 'NuLoginPersona')
        packet += packet_encoder.append('lkey', self.login_key)
        packet += packet_encoder.append('profileId', '1000')
        packet += packet_encoder.append('userId', '1000')
        packet = packet_encoder.encode('acct', self.pid, packet)
        self.transport.getHandle().sendall(packet)
        self.log.debug(f'[{self.name}] Sent packet=NuLoginPersona')

    elif txn == 'NuLookupUserInfo':
        packet = packet_encoder.append('TXN', 'NuLookupUserInfo')
        packet += packet_encoder.append('userInfo.0.userName', 'test-server')
        packet += packet_encoder.append('userInfo.0.userId', '1000')
        packet += packet_encoder.append('userInfo.0.masterUserId', '1000')
        packet += packet_encoder.append('userInfo.0.namespace', 'MAIN')
        packet += packet_encoder.append('userInfo.0.xuid', '24')
        packet += packet_encoder.append('userInfo.0.cid', '1000')
        packet += packet_encoder.append('userInfo.[]', '1')
        packet = packet_encoder.encode('acct', self.pid, packet)
        self.transport.getHandle().sendall(packet)
        self.log.debug(f'[{self.name}] Sent packet=NuLookupUserInfo')