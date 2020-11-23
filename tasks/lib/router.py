import sys
import os
os.chdir( os.path.dirname(__file__) )

from os.path import isfile, join

class Router(object):

    def __init__( self ):

        #@todo: replace if necesary the project name
        self.rootFolder = 'data-wakes_6x49'
        
        #@todo: change the routes to the absolute project directory path
        self.root = 'C:\\Users\\Chema\\Documents\\+code\\' + self.rootFolder +  '\\'

        self.universe =  self.root + 'data\\universe\\'
        self.stage =  self.root + 'data\\stage\\'
        self.master =  self.root + 'data\\master\\'
        self.secret =  self.root + 'data\\secret\\'


    def getRoute( self, block ):
        if block == 'universe':
            return self.universe
        elif  block == 'stage':
            return self.stage
        elif  block == 'master':
            return self.master
        elif  block == 'secret':
            return self.secret
        else:
            raise Exception("Router: Not a valid block")