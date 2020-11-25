'''
Created on 2020/11/10

@author: ukai
'''

class SacBatchDataAgent(object):
    '''
    classdocs
    '''
    
    # <<abstract>>
    def getSampledActionOnEnvironment(self):
        return None
    
    # <<abstract>>
    def getEntropy(self):
        return 1.