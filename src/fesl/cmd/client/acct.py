import time, os, json, logging
from util import packet_encoder, string_util
from inout import json_personas

def handle(self, txn):
    if txn == "NuLogin":
        self.pid += 1
        self.login_key = string_util.random_str(24)
        packet = packet_encoder.append('TXN', 'NuLogin')
        packet += packet_encoder.append('profileId', '1001')
        packet += packet_encoder.append('userId', '1001')
        packet += packet_encoder.append('nuid', 'lucas')
        packet += packet_encoder.append('lkey', self.login_key, True)
        packet = packet_encoder.encode('acct', self.pid, packet)
        self.transport.getHandle().sendall(packet)
        self.log.debug('[FESLClientManager] Sent packet=NuLogin')

    elif txn == 'NuGetPersonas':
        self.pid += 1
        packet = packet_encoder.append('TXN', 'NuGetPersonas')
        personas = next(os.walk(json_personas.path))[2]
        i = 0
        for persona in personas:
            pjson = json.load(open("src/heroes/"+persona, "r"))
            packet += packet_encoder.append('personas.'+str(i), pjson.get('heroName'))
            i += 1
        packet += packet_encoder.append('personas.[]', str(i), True)
        packet = packet_encoder.encode('acct', self.pid, packet)
        self.transport.getHandle().sendall(packet)
        self.log.debug('[FESLClientManager] Sent packet=NuGetPersonas')

    elif txn == 'NuGetAccount':
        self.pid += 1
        packet = packet_encoder.append('TXN', 'NuGetAccount')
        packet += packet_encoder.append('heroName', 'lucas')
        packet += packet_encoder.append('nuid', 'test@test.com')
        packet += packet_encoder.append('DOBDay', '1')
        packet += packet_encoder.append('DOBMonth', '1')
        packet += packet_encoder.append('DOBYear', '2017')
        packet += packet_encoder.append('userId', '1001')
        packet += packet_encoder.append('globalOptin', '0')
        packet += packet_encoder.append('thidPartyOptin', '0')
        packet += packet_encoder.append('language', 'enUS')
        packet += packet_encoder.append('country', 'US', True)
        packet = packet_encoder.encode('acct', self.pid, packet)
        self.transport.getHandle().sendall(packet)
        self.log.debug('[FESLClientManager] Sent packet=NuGetAccount')

    elif txn == 'NuLoginPersona':
        self.pid += 1
        self.loginkey = string_util.random_str(24)
        packet = packet_encoder.append('TXN', 'NuLoginPersona')
        packet += packet_encoder.append('lkey', self.loginkey)
        packet += packet_encoder.append('profileId', '1001')
        packet += packet_encoder.append('userId', '1001')
        packet = packet_encoder.encode('acct', self.pid, packet)
        self.transport.getHandle().sendall(packet)
        self.log.debug('[FESLClientManager] Sent packet=NuLoginPersona')

    elif txn == 'NuLookupUserInfo':
        self.pid += 1
        packet = packet_encoder.append('TXN', 'NuLookupUserInfo')
        personas = next(os.walk(json_personas.path))[2]
        i = 0
        for persona in personas:
            pjson = json.load(open("src/heroes/"+persona, "r"))
            packet += packet_encoder.append('userInfo.'+str(i)+'.userName', pjson.get('heroName'))
            packet += packet_encoder.append('userInfo.'+str(i)+'.userId', pjson.get('heroId'))
            packet += packet_encoder.append('userInfo.'+str(i)+'.namespace', 'MAIN')
            packet += packet_encoder.append('userInfo.'+str(i)+'.xuid', '24')
            i += 1
        packet += packet_encoder.append('userInfo.[]', str(i), True)
        packet = packet_encoder.encode('acct', self.pid, packet)
        self.transport.getHandle().sendall(packet)
        self.log.debug('[FESLClientManager] Sent packet=NuLookupUserInfo')

