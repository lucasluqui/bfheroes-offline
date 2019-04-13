import json, logging
from util import packet_encoder, packet_reader
from inout import json_personas

def handle(self, txn, data):
    if txn == "GetStats":
        self.pid += 1
        heroId = packet_reader.read_key(data, 'owner')
        packet = packet_encoder.append('TXN', 'GetStats')
        packet += packet_encoder.append('ownerId', heroId)
        packet += packet_encoder.append('ownerType', packet_reader.read_key(data, 'ownerType'))
        total_keys = int(packet_reader.read_key(data, 'keys.[]'))
        key_names = []
        i = 0
        while i != total_keys:
                key_names.append(packet_reader.read_key(data, 'keys.' + str(i)))
                i += 1
        i = 0
        while i != total_keys:
                if int(heroId) != int(json_personas.CONFIG['Settings']['AccountID']):
                    pjson = json.load(open(json_personas.path+heroId+'.json', "r"))
                else:
                    pjson = json.load(open(json_personas.path+'globalStats.json', "r"))
                packet += packet_encoder.append('stats.'+str(i)+'.key', key_names[i])
                packet += packet_encoder.append('stats.'+str(i)+'.value', pjson.get(key_names[i], ""))
                packet += packet_encoder.append('stats.'+str(i)+'.text', pjson.get(key_names[i], ""))
                i += 1
        packet += packet_encoder.append('stats.[]', total_keys)
        packet = packet_encoder.encode('rank', self.pid, packet)
        self.transport.getHandle().sendall(packet)
        self.log.debug('[FESLClientManager] Sent packet=GetStats')

    elif txn == "GetStatsForOwners":
        self.pid += 1
        ownerIds = []
        ownerTypes = []
        key_names = []
        total_keys = int(packet_reader.read_key(data, 'keys.[]'))
        total_owners = int(packet_reader.read_key(data, 'owners.[]'))
        i = 0
        while i != total_owners:
            ownerIds.append(packet_reader.read_key(data, 'owners.'+str(i)+'.ownerId'))
            ownerTypes.append(packet_reader.read_key(data, 'owners.'+str(i)+'.ownerType'))
            i += 1
        packet = packet_encoder.append('TXN', 'GetStats')
        i = 0
        while i != total_keys:
            key_names.append(packet_reader.read_key(data, 'keys.'+str(i)))
            i += 1
        i = 0
        while i != total_owners:
            pjson = json.load(open(json_personas.path+ownerIds[i]+'.json', "r"))
            packet += packet_encoder.append('stats.'+str(i)+'.ownerId', ownerIds[i])
            packet += packet_encoder.append('stats.'+str(i)+'.ownerType', ownerTypes[i])
            ii = 0
            while ii != total_keys:
                packet += packet_encoder.append('stats.'+str(i)+'.stats.'+str(ii)+'.key', key_names[ii])
                packet += packet_encoder.append('stats.'+str(i)+'.stats.'+str(ii)+'.value', pjson.get(key_names[ii], ''))
                packet += packet_encoder.append('stats.'+str(i)+'.stats.'+str(ii)+'.text', pjson.get(key_names[ii], ''))
                ii += 1
            packet += packet_encoder.append('stats.'+str(i)+'.stats.[]', str(total_keys))
            i += 1
        packet += packet_encoder.append('stats.[]', total_owners)
        packet = packet_encoder.encode('rank', self.pid, packet)
        self.transport.getHandle().sendall(packet)
        self.log.debug('[FESLClientManager] Sent packet=GetStatsForOwners')

    elif txn == "UpdateStats":
        packet = packet_encoder.encode('rank', 0xC0000000, packet_encoder.append('TXN', 'UpdateStats'))
        self.transport.getHandle().sendall(packet)
        self.log.debug('[FESLClientManager] Sent packet=UpdateStats')