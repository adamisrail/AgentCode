'''
Created on Feb 11, 2019

@author: dr.aarij
'''
from abc import abstractmethod

class Agent(object):
    '''
    classdocs
    '''



    @abstractmethod
    def __init__(self):
        pass
    
    @abstractmethod
    def sense(self,environment):
        pass
    
    @abstractmethod
    def act(self):
        pass