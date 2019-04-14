import logging, time, os, json
from configobj import ConfigObj
from twisted.web import resource
from util import json_personas

class run(resource.Resource):
    def __init__(self):
        self.name = "Magma API"
        self.log = logging.getLogger('root')
        self.config = ConfigObj('src/config.ini')

    isLeaf = True

    def render_GET(self, request):
        uri=request.uri.decode()
        self.log.info(f"[{self.name}] GET uri={uri}")
        request.setHeader('content-type', 'text/xml; charset=utf-8')

        if uri == '/nucleus/authToken':
            reply = '<success><token code="NEW_TOKEN">'+self.config['Settings']['SessionID']+'</token></success>'
            self.log.info(f"[{self.name}] GET reply={reply}")
            return reply.encode('utf-8', 'ignore')

        elif '/nucleus/check/user/' in uri:
            persona = json.load(open(json_personas.path+uri.replace('/nucleus/check/user/','')+'.json', "r"))
            reply = '<name>'+persona.get('heroName', 'undefined')+'</name>'
            self.log.info(f"[{self.name}] GET reply={reply}")
            return reply.encode('utf-8', 'ignore')

        elif uri.split(':')[0] == '/relationships/roster/nucleus':
            reply = '<update><id>1</id><name>Test</name><state>ACTIVE</state><type>server</type><status>Online</status><realid>'+uri.split(':')[1]+'</realid></update>'
            self.log.info(f"[{self.name}] GET reply={reply}")
            return reply.encode('utf-8', 'ignore')

        elif uri == '/ofb/products':
            reply = open("src/xml/products.xml", "r")
            self.log.info(f"[{self.name}] GET reply=xml/products.xml")
            return reply.read()
        
        elif uri.find('/nucleus/entitlements/') == 0:
            reply = open("src/xml/entitlements.xml", "r")
            self.log.info(f"[{self.name}] GET reply=xml/entitlements.xml")
            return reply.read()

        elif uri.find('/nucleus/wallets/') == 0:
            reply = open("src/xml/wallets.xml", "r")
            self.log.info(f"[{self.name}] GET reply=xml/wallets.xml")
            return reply.read()

    def render_POST(self, request):
        uri=request.uri.decode()
        self.log.info(f"[{self.name}] POST uri={uri}")

        if uri.split(':')[0] == '/relationships/status/nucleus':
            request.setHeader('content-type', 'text/plain; charset=utf-8')
            reply = '<update><id>1</id><name>Test</name><state>ACTIVE</state><type>server</type><status>Online</status><realid>' + uri.split(':')[1] + '</realid></update>'
            self.log.info(f"[{self.name}] POST reply={reply}")
            return reply.encode('utf-8', 'ignore')