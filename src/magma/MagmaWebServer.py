from twisted.web import resource
import time
import os

class Simple(resource.Resource):
    isLeaf = True

    def render_GET(self, request):
        uri=request.uri.decode()
        print("[Magma] GET uri="+uri)
        request.setHeader('content-type', 'text/xml; charset=utf-8')

        if uri == '/nucleus/authToken':
            reply = '<success><token code="NEW_TOKEN">123456</token></success>'
            print("[Magma] replying to last GET request="+reply)
            return reply.encode('utf-8', 'ignore')

        elif '/nucleus/check/user/' in uri:
            reply = '<name>'+uri.replace('/nucleus/check/user/','')+'</name>'
            print("[Magma] replying to last GET request="+reply)
            return reply.encode('utf-8', 'ignore')

        elif uri.split(':')[0] == '/relationships/roster/nucleus':
            reply = '<update><id>1</id><name>Test</name><state>ACTIVE</state><type>server</type><status>Online</status><realid>'+uri.split(':')[1]+'</realid></update>'
            print("[Magma] replying to last GET request="+reply)
            return reply.encode('utf-8', 'ignore')

        elif uri == '/ofb/products':
            reply = open("src/xml/products.xml", "r")
            print("[Magma] replying to last request with xml/products.xml file")
            return reply.read()
        
        elif uri.find('/nucleus/entitlements/') == 0:
            reply = open("src/xml/entitlements.xml", "r")
            print("[Magma] replying to last request with xml/entitlements.xml file")
            return reply.read()

        elif uri.find('/nucleus/wallets/') == 0:
            reply = open("src/xml/wallets.xml", "r")
            print("[Magma] replying to last request with xml/wallets.xml file")
            return reply.read()

    def render_POST(self, request):
        uri=request.uri.decode()
        print("[Magma] POST uri="+uri)

        if uri.split(':')[0] == '/relationships/status/nucleus':
            request.setHeader('content-type', 'text/plain; charset=utf-8')
            reply = '<update><id>1</id><name>Test</name><state>ACTIVE</state><type>server</type><status>Online</status><realid>' + uri.split(':')[1] + '</realid></update>'
            print("[Magma] replying to last POST request="+reply)
            return reply.encode('utf-8', 'ignore')