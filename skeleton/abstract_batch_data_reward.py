'''
Created on 2020/11/10

@author: ukai
'''

class AbstractBatchDataReward(object):
    '''
    classdocs
    '''
        
    def __init__(self, reward = None):
        self.reward = reward
        
    def getValue(self):
        return 1.