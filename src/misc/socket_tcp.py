import socket
import multiprocessing
import random
from util import PacketReader

class Socket(object):
    def __init__(self, hostname:str, port:int, fesl:bool=False):
        self.hostname = hostname
        self.port = port
        self.fesl = fesl
        self.sid = random.randint(1000,10000)
        self.pcount = 0
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.hostname, self.port))

    def listen(self):
        self.sock.listen(17)
        print('['+str(self.socketid)+'-TCPSocket] Now listening on hostname ' + self.hostname + ':' + str(self.port))
        print('['+str(self.socketid)+'-TCPSocket] FESL: ' + str(self.fesl))
        while True:
            client, address = self.sock.accept()
            print('['+str(self.socketid)+'-TCPSocket] NEW CONNECTION: ' + address)
            client.settimeout(60)
            process = multiprocessing.Process(target=handle, args=(client, address))
            self.pcount += 1 
            process.daemon = True
            process.start()

    def handle(self, client, address):
        BUFFER_SIZE = 1024
        while True:
            try:
                data = client.recv(BUFFER_SIZE)
                if data:
                    packet = PacketReader.read_packet(data)
                    print('['+str(self.socketid)+'-TCPSocket] PACKET START')
                    print(packet.command)
                    print(packet.txn)
                    print(packet.var)
                    print(packet.length)
                    print('['+str(self.socketid)+'-TCPSocket] PACKET END')
                    client.close()
                else:
                    raise error('Client disconnected')
            except:
                client.close()
                return False

    def stop(self, process):
        process.terminate()
