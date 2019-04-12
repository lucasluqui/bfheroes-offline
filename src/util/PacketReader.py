def read_cmd(packet):
    command = packet[:4].decode('ascii','ignore')
    return command

def read_txn(packet):
    try:
        txn = packet.decode('ascii','ignore').split('TXN=')[1].split('\n')[0]
        return txn
    except:
        return None

def read_pid(packet):
    pid = packet[4:8]
    return pid

def read_key(packet, key_name):
    value = packet.decode('ascii','ignore').split(key_name + '=')[1].split('\n')[0]
    return value