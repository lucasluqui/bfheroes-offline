import logging
from twisted.web import resource

class run(resource.Resource):
    def __init__(self):
        self.name = "WebBrowser API"
        self.log = logging.getLogger('root')

    isLeaf = True

    def render_GET(self, request):
        uri=request.uri.decode()
        self.log.debug(f'[{self.name}] GET uri={uri}')
        request.setHeader('content-type', 'text/html; charset=utf-8')
        request.setHeader('connection', 'keep-alive')
        request.setHeader('Cache-Control', 'public, max-age=31536000')
        request.setHeader('Pragma', 'public')

        if uri == '/en/game/footer':
            reply = '<html><style>html{background:url(https://i.imgur.com/6Lysxev.jpg) no-repeat center center fixed;-webkit-background-size:cover;-moz-background-size:cover;-o-background-size:cover;background-size:cover}</style><body></body></html>'
            self.log.debug(f'[{self.name}] GET reply={reply}')
            return reply.encode('utf-8', 'ignore')
    
    def render_POST(self, request):
        self.log.debug(f'[{self.name}] {request}')