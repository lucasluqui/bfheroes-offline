import json
from configobj import ConfigObj

CONFIG = ConfigObj('src/config.ini')
path = CONFIG['Settings']['HeroesPath']