def read_data(data):
    packets = []
    packets += data.split(b'\n\x00')
    packets = list(filter(lambda a: a != b'', packets))
    for packet in packets:
        packet += b'\n\x00'
        # Required workaround to handle a strange packet received after ACCT NuLoginPersona
        # where \n\x00 is found in the middle of the packet, making it hard to work with.
        if len(packet.split()) > 0:
            packet = b'rank\xc0\x00\x00\n\x00'+packet
    return packets