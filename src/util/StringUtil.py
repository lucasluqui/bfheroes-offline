import string
import random

def random_str(size):
    CHARS = string.ascii_uppercase+string.digits+string.ascii_lowercase
    return ''.join(random.choice(CHARS) for _ in range(size))
