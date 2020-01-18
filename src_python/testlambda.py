import os
import sys
print(sys.path)
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from config import config

print(config.cyProxy)
print(os.path.dirname(__file__))
print(os.path.join(os.path.dirname(__file__), '..'))
print(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
print(os.path.abspath('c:/Users/ahok/Desktop/GitHub/rocketbook/src_python/..'))