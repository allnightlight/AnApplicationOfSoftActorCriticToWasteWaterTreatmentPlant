'''
Created on 2020/11/14

@author: ukai
'''

class AbstractPlant(object):
    '''
    classdocs
    '''

    # <<abstract>>
    def getPv(self):
        return None # as pv
    
    # <<abstract>>
    def update(self, u):
        return None # reward
    
    # <<abstract>>
    def reset(self):
        pass
    
    # <<abstract>>
    def getNmv(self):
        return -1
    
        # <<abstract>>
    def getNpv(self):
        return -1