from util import PacketEncoder, PacketReader
from inout import JsonPersonas
import json

def handle(self, txn, data):
    if txn == "getstats":
        self.pid += 1
        heroId = PacketReader.read_key(data, 'owner')
        GetStatsPacket = PacketEncoder.append('TXN', 'GetStats')
        GetStatsPacket += PacketEncoder.append('ownerId', heroId)
        GetStatsPacket += PacketEncoder.append('ownerType', PacketReader.read_key(data, 'ownerType'))
        total_keys = int(PacketReader.read_key(data, 'keys.[]'))
        key_names = []
        i = 0
        while i != total_keys:
                key_names.append(PacketReader.read_key(data, 'keys.' + str(i)))
                i += 1
        i = 0
        while i != total_keys:
                if int(heroId) != int(JsonPersonas.CONFIG['Settings']['AccountID']):
                    pjson = json.load(open(JsonPersonas.path+heroId+'.json', "r"))
                else:
                    pjson = json.load(open(JsonPersonas.path+'globalStats.json', "r"))
                GetStatsPacket += PacketEncoder.append('stats.'+str(i)+'.key', key_names[i])
                GetStatsPacket += PacketEncoder.append('stats.'+str(i)+'.value', pjson.get(key_names[i], ""))
                GetStatsPacket += PacketEncoder.append('stats.'+str(i)+'.text', pjson.get(key_names[i], ""))
                i += 1
        GetStatsPacket += PacketEncoder.append('stats.[]', total_keys)
        GetStatsPacket = PacketEncoder.encode('rank', self.pid, GetStatsPacket)
        self.transport.getHandle().sendall(GetStatsPacket)
        print('[FESLClientManager] Sent GetStatsPacket')

    elif txn == "getstatsforowners":
        self.pid += 1
        ownerIds = []
        ownerTypes = []
        key_names = []
        total_keys = int(PacketReader.read_key(data, 'keys.[]'))
        total_owners = int(PacketReader.read_key(data, 'owners.[]'))
        i = 0
        while i != total_owners:
            ownerIds.append(PacketReader.read_key(data, 'owners.'+str(i)+'.ownerId'))
            ownerTypes.append(PacketReader.read_key(data, 'owners.'+str(i)+'.ownerType'))
            i += 1
        GetStatsForOwnersPacket = PacketEncoder.append('TXN', 'GetStats')
        i = 0
        while i != total_keys:
            key_names.append(PacketReader.read_key(data, 'keys.'+str(i)))
            i += 1
        i = 0
        while i != total_owners:
            pjson = json.load(open(JsonPersonas.path+ownerIds[i]+'.json', "r"))
            GetStatsForOwnersPacket += PacketEncoder.append('stats.'+str(i)+'.ownerId', ownerIds[i])
            GetStatsForOwnersPacket += PacketEncoder.append('stats.'+str(i)+'.ownerType', ownerTypes[i])
            ii = 0
            while ii != total_keys:
                GetStatsForOwnersPacket += PacketEncoder.append('stats.'+str(i)+'.stats.'+str(ii)+'.key', key_names[ii])
                GetStatsForOwnersPacket += PacketEncoder.append('stats.'+str(i)+'.stats.'+str(ii)+'.value', pjson.get(key_names[ii], ''))
                GetStatsForOwnersPacket += PacketEncoder.append('stats.'+str(i)+'.stats.'+str(ii)+'.text', pjson.get(key_names[ii], ''))
                ii += 1
            GetStatsForOwnersPacket += PacketEncoder.append('stats.'+str(i)+'.stats.[]', str(total_keys))
            i += 1
        GetStatsForOwnersPacket += PacketEncoder.append('stats.[]', total_owners)
        GetStatsForOwnersPacket = PacketEncoder.encode('rank', self.pid, GetStatsForOwnersPacket)
        self.transport.getHandle().sendall(GetStatsForOwnersPacket)
        print('[FESLClientManager] Sent GetStatsForOwnersPacket')

    elif txn == "updatestats":
        UpdateStatsPacket = PacketEncoder.encode('rank', 0xC0000000, PacketEncoder.append('TXN', 'UpdateStats'))
        self.transport.getHandle().sendall(UpdateStatsPacket)
        print('[FESLClientManager] Sent UpdateStatsPacket')