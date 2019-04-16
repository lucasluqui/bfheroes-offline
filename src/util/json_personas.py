import json
from configobj import ConfigObj

CONFIG = ConfigObj('src/config.ini')
path = CONFIG['Paths']['HeroesPath']

with open(path+'globalStats.json') as global_stats:
    global_stats = json.load(global_stats)