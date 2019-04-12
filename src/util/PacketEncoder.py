def append(key:str, value:str, last=False):
    new = f'{key}={value}'
    if last != False:
        new += '\n\x00'
    else:
        new += '\n'
    return new

def encode(cmd, pid, data):
    encoded = cmd.encode('ascii', 'ignore')
    encoded += (pid).to_bytes(4, byteorder="big")
    encoded += (len(data) + 12).to_bytes(4, byteorder="big")
    encoded += data.encode('ascii', 'ignore')
    return encoded

    