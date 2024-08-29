
from src.api import listener
from src.api import entries
from src.prepare import start_preperation
from json import loads

if __name__ == '__main__':
    start_preperation()
    listener.start()
