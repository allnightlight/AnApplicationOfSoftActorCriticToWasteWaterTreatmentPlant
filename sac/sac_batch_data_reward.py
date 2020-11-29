'''
Created on 2020/11/10

@author: ukai
'''

class SacBatchDataReward(object):
    '''
    classdocs
    '''
        
    def __init__(self, reward):
        self.reward = reward
        
    # <<abstract>>
    def getValue(self):
        return self.reward