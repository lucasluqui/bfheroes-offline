# Create Packet Checksum (8 bytes between command and data)
# First one is command id, 2nd one is data length

from binascii import unhexlify


def CommandID(value):
    if value == 0:
        # Value 0 are used in Theater connections, and its always the same
        return bytes('\x00\x00\x00\x00'.encode())
    else:
        width = value.bit_length()
        width += 8 - ((width % 8) or 8)
        fmt = '%%0%dx' % (width // 4)
        CommandID = unhexlify(fmt % value)
        return CommandID

def PacketLength(data):

    loop = 0
    slen = len(data) + 12
    ascii_chars = ''

    if slen > 256:
        width = slen.bit_length()
        width += 8 - ((width % 8) or 8)
        fmt = '%%0%dx' % (width // 1.5)
        ascii_chars = unhexlify(fmt % slen)
    else:
        while loop != 4:
            ascii = slen >> ((4 - 1 - loop) << 3)
            ascii_chars += chr(ascii)
            loop += 1

    # Bug fix if generated packet length bytes is higher than 4

    if len(ascii_chars) > 4:
        additional_characters = len(ascii_chars) - 4
        ascii_chars = ascii_chars[additional_characters:]
    return ascii_chars

def CreateChecksum(data, value):
    cmd_id = CommandID(value)
    pl = PacketLength(data)
    checksum = cmd_id + pl.encode()
    return checksum