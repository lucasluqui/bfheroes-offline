from util import PacketEncoder, StringUtil

def handle(self, txn):
    if txn == 'nulogin':
        self.pid += 1
        self.login_key = StringUtil.random_str(24)
        LoginPacket = PacketEncoder.append('TXN', 'NuLogin')
        LoginPacket += PacketEncoder.append('lkey', self.login_key)
        LoginPacket += PacketEncoder.append('nuid', 'test-server')
        LoginPacket += PacketEncoder.append('profileId', '1000')
        LoginPacket += PacketEncoder.append('userId', '1000')
        LoginPacket = PacketEncoder.encode('acct', self.pid, LoginPacket)
        self.transport.getHandle().sendall(LoginPacket)
        print('[FESLServerManager] Sent LoginPacket')
    
    elif txn == 'nugetpersonas':
        self.pid += 1
        GetPersonasPacket = PacketEncoder.append('TXN', 'NuGetPersonas')
        GetPersonasPacket += PacketEncoder.append('personas.[]', 0)
        GetPersonasPacket = PacketEncoder.encode('acct', self.pid, GetPersonasPacket)
        self.transport.getHandle().sendall(GetPersonasPacket)
        print('[FESLServerManager] Sent GetPersonasPacket')

    elif txn == 'nugetaccount':
        self.pid += 1
        GetAccountPacket = PacketEncoder.append('TXN', 'NuGetAccount')
        GetAccountPacket += PacketEncoder.append('heroName', 'test-server')
        GetAccountPacket += PacketEncoder.append('nuid', 'test-server@test.com')
        GetAccountPacket += PacketEncoder.append('DOBDay', '1')
        GetAccountPacket += PacketEncoder.append('DOBMonth', '1')
        GetAccountPacket += PacketEncoder.append('DOBYear', '2017')
        GetAccountPacket += PacketEncoder.append('userId', '1000')
        GetAccountPacket += PacketEncoder.append('globalOptin', '0')
        GetAccountPacket += PacketEncoder.append('thidPartyOptin', '0')
        GetAccountPacket += PacketEncoder.append('language', 'enUS')
        GetAccountPacket += PacketEncoder.append('country', 'US')
        GetAccountPacket = PacketEncoder.encode('acct', self.pid, GetAccountPacket)
        self.transport.getHandle().sendall(GetAccountPacket)
        print('[FESLServerManager] Sent GetAccountPacket')

    elif txn == 'nuloginpersona':
        LoginPersonaPacket = PacketEncoder.append('TXN', 'NuLoginPersona')
        LoginPersonaPacket += PacketEncoder.append('lkey', self.login_key)
        LoginPersonaPacket += PacketEncoder.append('profileId', '1000')
        LoginPersonaPacket += PacketEncoder.append('userId', '1000')
        LoginPersonaPacket = PacketEncoder.encode('acct', self.pid, LoginPersonaPacket)
        self.transport.getHandle().sendall(LoginPersonaPacket)
        print('[FESLServerManager] Sent LoginPersonaPacket')

    elif txn == 'nulookupuserinfo':
        LookUpUserInfoPacket = PacketEncoder.append('TXN', 'NuLookupUserInfo')
        LookUpUserInfoPacket += PacketEncoder.append('userInfo.0.userName', 'test-server')
        LookUpUserInfoPacket += PacketEncoder.append('userInfo.0.userId', '1000')
        LookUpUserInfoPacket += PacketEncoder.append('userInfo.0.masterUserId', '1000')
        LookUpUserInfoPacket += PacketEncoder.append('userInfo.0.namespace', 'MAIN')
        LookUpUserInfoPacket += PacketEncoder.append('userInfo.0.xuid', '24')
        LookUpUserInfoPacket += PacketEncoder.append('userInfo.0.cid', '1000')
        LookUpUserInfoPacket += PacketEncoder.append('userInfo.[]', '1')
        LookUpUserInfoPacket = PacketEncoder.encode('acct', self.pid, LookUpUserInfoPacket)
        self.transport.getHandle().sendall(LookUpUserInfoPacket)
        print('[FESLServerManager] Sent LookUpUserInfoPacket')