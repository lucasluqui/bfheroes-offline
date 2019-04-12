import time
import os
import json
from util import PacketEncoder, StringUtil
from inout import JsonPersonas

def handle(self, txn):
    if txn == "nulogin":
        self.pid += 1
        self.login_key = StringUtil.random_str(24)
        LoginPacket = PacketEncoder.append('TXN', 'NuLogin')
        LoginPacket += PacketEncoder.append('profileId', '1001')
        LoginPacket += PacketEncoder.append('userId', '1001')
        LoginPacket += PacketEncoder.append('nuid', 'lucas')
        LoginPacket += PacketEncoder.append('lkey', self.login_key, True)
        LoginPacket = PacketEncoder.encode('acct', self.pid, LoginPacket)
        self.transport.getHandle().sendall(LoginPacket)
        print('[FESLClientManager] Sent LoginPacket')

    elif txn == 'nugetpersonas':
        self.pid += 1
        GetPersonasPacket = PacketEncoder.append('TXN', 'NuGetPersonas')
        personas = next(os.walk(JsonPersonas.path))[2]
        i = 0
        for persona in personas:
            pjson = json.load(open("src/heroes/"+persona, "r"))
            GetPersonasPacket += PacketEncoder.append('personas.'+str(i), pjson.get('heroName'))
            i += 1
        GetPersonasPacket += PacketEncoder.append('personas.[]', str(i), True)
        GetPersonasPacket = PacketEncoder.encode('acct', self.pid, GetPersonasPacket)
        self.transport.getHandle().sendall(GetPersonasPacket)
        print('[FESLClientManager] Sent GetPersonasPacket')

    elif txn == 'nugetaccount':
        self.pid += 1
        GetAccountPacket = PacketEncoder.append('TXN', 'NuGetAccount')
        GetAccountPacket += PacketEncoder.append('heroName', 'lucas')
        GetAccountPacket += PacketEncoder.append('nuid', 'test@test.com')
        GetAccountPacket += PacketEncoder.append('DOBDay', '1')
        GetAccountPacket += PacketEncoder.append('DOBMonth', '1')
        GetAccountPacket += PacketEncoder.append('DOBYear', '2017')
        GetAccountPacket += PacketEncoder.append('userId', '1001')
        GetAccountPacket += PacketEncoder.append('globalOptin', '0')
        GetAccountPacket += PacketEncoder.append('thidPartyOptin', '0')
        GetAccountPacket += PacketEncoder.append('language', 'enUS')
        GetAccountPacket += PacketEncoder.append('country', 'US', True)
        GetAccountPacket = PacketEncoder.encode('acct', self.pid, GetAccountPacket)
        self.transport.getHandle().sendall(GetAccountPacket)
        print('[FESLClientManager] Sent GetAccountPacket')

    elif txn == 'nuloginpersona':
        self.pid += 1
        self.loginkey = StringUtil.random_str(24)
        LoginPersonaPacket = PacketEncoder.append('TXN', 'NuLoginPersona')
        LoginPersonaPacket += PacketEncoder.append('lkey', self.loginkey)
        LoginPersonaPacket += PacketEncoder.append('profileId', '1001')
        LoginPersonaPacket += PacketEncoder.append('userId', '1001')
        LoginPersonaPacket = PacketEncoder.encode('acct', self.pid, LoginPersonaPacket)
        self.transport.getHandle().sendall(LoginPersonaPacket)
        print('[FESLClientManager] Sent LoginPersonaPacket')

    elif txn == 'nulookupuserinfo':
        self.pid += 1
        LookUpUserInfoPacket = PacketEncoder.append('TXN', 'NuLookupUserInfo')
        personas = next(os.walk(JsonPersonas.path))[2]
        i = 0
        for persona in personas:
            pjson = json.load(open("src/heroes/"+persona, "r"))
            LookUpUserInfoPacket += PacketEncoder.append('userInfo.'+str(i)+'.userName', pjson.get('heroName'))
            LookUpUserInfoPacket += PacketEncoder.append('userInfo.'+str(i)+'.userId', pjson.get('heroId'))
            LookUpUserInfoPacket += PacketEncoder.append('userInfo.'+str(i)+'.namespace', 'MAIN')
            LookUpUserInfoPacket += PacketEncoder.append('userInfo.'+str(i)+'.xuid', '24')
            i += 1
        LookUpUserInfoPacket += PacketEncoder.append('userInfo.[]', str(i), True)
        LookUpUserInfoPacket = PacketEncoder.encode('acct', self.pid, LookUpUserInfoPacket)
        self.transport.getHandle().sendall(LookUpUserInfoPacket)
        print('[FESLClientManager] Sent LookUpUserInfo')

