import os
import  sys
from core import src

print(os.path.dirname(__file__))

sys.path.append(os.path.dirname(__file__))

if __name__ == '__main__':
    src.run()