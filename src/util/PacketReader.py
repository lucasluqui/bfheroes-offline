def read_cmd(packet):
    return packet[:4].decode('ascii','ignore')

def read_txn(packet):
    try:
        txn = packet.decode('ascii','ignore').split('TXN=')[1].split('\n')[0]
        return txn
    except:
        return None

def read_pid(packet):
    # todo:
    # make it actually return packet id and not byte 4 to 8.
    return packet[4:8]

def read_key(packet, key):
    return packet.decode('ascii','ignore').split(key+'=')[1].split('\n')[0]