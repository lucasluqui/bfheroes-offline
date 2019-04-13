import logging

class StreamHandler(logging.StreamHandler):

    def __init__(self):
        logging.StreamHandler.__init__(self)
        fmt = '%(asctime)s %(levelname)s %(message)s'
        fmt_date = '%H:%M:%S'
        formatter = logging.Formatter(fmt, fmt_date)
        self.setFormatter(formatter)

class FileHandler(logging.FileHandler):

    def __init__(self, fn):
        logging.FileHandler.__init__(self, filename=fn)
        fmt = '%(asctime)s %(levelname)s %(message)s'
        fmt_date = '%H:%M:%S'
        formatter = logging.Formatter(fmt, fmt_date)
        self.setFormatter(formatter)