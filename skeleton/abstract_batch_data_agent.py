'''
Created on 2020/11/10

@author: ukai
'''

class AbstractBatchDataAgent(object):
    '''
    classdocs
    '''

    # <<abstract>>
    def getMv(self):
        return None
    
    # <<abstract>>
    def getEntropy(self):
        return 1.