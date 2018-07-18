import os
import sys

def pathSetup(): 
    dir = os.path.dirname(__file__)

    paths = [
        os.path.join(dir, 'queries'),
        os.path.join(dir, 'mutations'),
        os.path.join(dir, 'db'),
        os.path.join(dir, 'schema')
    ]
    
    for path in paths:
        sys.path.append(path)
        
    print('setup path finished')
