#!python3.7
import sys, time, logging, platform, subprocess
from configobj import ConfigObj
from twisted.internet import ssl, reactor
from twisted.internet.protocol import Factory, Protocol
from twisted.web import server, resource
from fesl import FESLClientManager, FESLServerManager
from theater import TheaterClientManager, TheaterServerManager
from magma import MagmaWebServer
from inout import JsonServices

def run():

    if platform.system() != "Windows":
        logging.warning('Will not attempt to automatically start the game since we are not running on Windows.')
    else:
        print('Attempting to automatically start the game...')
        try:
            subprocess.STARTF_USESHOWWINDOW = 1
            subprocess.Popen('cd game&start.bat', shell=True)
            logging.info('Game started.')
        except:
            logging.error('A strange error occured whilst trying to start the game. Have you renamed any files or bypassed run.bat?')

    for service in JsonServices.services:
        port = JsonServices.services[service]['port']
        if service != "MagmaWebServer":
            try:
                factory = Factory()
                if service == "FESLClientManager":
                    factory.protocol = FESLClientManager.HANDLER
                elif service == "FESLServerManager":
                    factory.protocol = FESLServerManager.HANDLER
                elif service == "TheaterClientManager":
                    factory.protocol = TheaterClientManager.HANDLER
                    reactor.listenUDP(JsonServices.services['TheaterClientManager']['port-udp'], TheaterClientManager.HANDLER_UDP())
                elif service == "TheaterServerManager":
                    factory.protocol = TheaterServerManager.HANDLER
                    reactor.listenUDP(JsonServices.services['TheaterServerManager']['port-udp'], TheaterServerManager.HANDLER_UDP())
                reactor.listenTCP(port, factory)
            except Exception:
                sys.exit(1)
        else:
            try:
                site = server.Site(MagmaWebServer.Simple())
                reactor.listenTCP(port, site)
            except Exception:
                sys.exit(1)
        logging.info('['+service+'] Started listening on port: '+str(port))
    reactor.run()

if __name__ == '__main__':
    run()

