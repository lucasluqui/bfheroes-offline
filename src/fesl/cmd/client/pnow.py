import logging
from util import packet_encoder

def handle(self, txn, data):
    if txn == "Start":
        packet = packet_encoder.append('TXN', 'Start')
        packet += packet_encoder.append('id.id', 1)
        packet += packet_encoder.append('id.partition', '/eagames/bfwest-dedicated', True)
        packet = packet_encoder.encode('pnow', self.pid, packet)
        self.transport.getHandle().sendall(packet)
        self.log.debug(f'[{self.name}] Sent packet=Start')

        packet = packet_encoder.append('TXN', 'Status')
        packet += packet_encoder.append('id.id', 1)
        packet += packet_encoder.append('id.partition', '/eagames/bfwest-dedicated')
        packet += packet_encoder.append('sessionState', 'COMPLETE')
        packet += packet_encoder.append('props.{}.[]', 2)
        packet += packet_encoder.append('props.{resultType}', 'JOIN')

        if False:
            return
        else:
            self.log.warning(f'[{self.name}] There are no matches available.')
            packet += packet_encoder.append('props.{games}.[]', 0)

        packet = packet_encoder.encode('pnow', self.pid, packet)
        self.transport.getHandle().sendall(packet)
        self.log.debug(f'[{self.name}] Sent packet=Status')