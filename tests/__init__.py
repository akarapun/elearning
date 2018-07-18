import os
import sys

dir = os.path.dirname(__file__)
splittedDir = dir.split('/')
splittedDir = splittedDir[:-1]

joinnedDir = '/'.join(splittedDir)
sys.path.append(joinnedDir)

import setup
setup.pathSetup()

import schema as RootSchema
schema = RootSchema.get()




