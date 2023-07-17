'''
Created on Feb 11, 2019

@author: dr.aarij
'''

from com.agent import Agent

class VaccumAgent(Agent.Agent):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        pass

    def sense(self,env):
        self.environment = env
    
    def act(self):
        if self.environment.currentRoom.status == 'dirty':
            return 'clean'
        if self.environment.currentRoom.location == 'A':
            return 'right'   
        if self.environment.currentRoom.location == 'B':
            return 'center'
        return 'left'
            
            