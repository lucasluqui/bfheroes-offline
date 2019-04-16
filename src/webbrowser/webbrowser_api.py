import os, logging, random
from twisted.web import resource
from configobj import ConfigObj

class run(resource.Resource):
    def __init__(self):
        self.name = "WebBrowserAPI"
        self.log = logging.getLogger('root')
        self.config = ConfigObj('src/config.ini')

    isLeaf = True

    def render_GET(self, request):
        uri=request.uri.decode()
        self.log.debug(f'[{self.name}] GET uri={uri}')
        request.setHeader('connection', 'keep-alive')
        request.setHeader('Cache-Control', 'max-age=31536000')
        request.setHeader('Pragma', 'public')

        if uri == '/en/game/footer':
            image_name = self.config['WebBrowser']['ServedFooter']
            image = open(self.config['Paths']['WebBrowserRsrcPath']+'footer/'+image_name, 'rb')
            request.setHeader('content-type', 'image/'+image_name.split('.')[1])
            self.log.debug(f'[{self.name}] GET reply={image_name}')
            return image.read()

        elif uri == '/en/game/loading':
            image_name = self.config['WebBrowser']['ServedLoading']
            image = open(self.config['Paths']['WebBrowserRsrcPath']+'loading/'+image_name, 'rb')
            request.setHeader('content-type', 'image/'+image_name.split('.')[1])
            self.log.debug(f'[{self.name}] GET reply={image_name}')
            return image.read()

        elif uri == '/game/banner':
            image_name = self.config['WebBrowser']['ServedBanner']
            image = open(self.config['Paths']['WebBrowserRsrcPath']+'banner/'+image_name, 'rb')
            request.setHeader('content-type', 'image/'+image_name.split('.')[1])
            self.log.debug(f'[{self.name}] GET reply={image_name}')
            return image.read()

        elif uri == '/en/game/eor':
            image_name = self.config['WebBrowser']['ServedEOR']
            image = open(self.config['Paths']['WebBrowserRsrcPath']+'eor/'+image_name, 'rb')
            request.setHeader('content-type', 'image/'+image_name.split('.')[1])
            self.log.debug(f'[{self.name}] GET reply={image_name}')
            return image.read()
    
    def render_POST(self, request):
        self.log.debug(f'[{self.name}] {request}')