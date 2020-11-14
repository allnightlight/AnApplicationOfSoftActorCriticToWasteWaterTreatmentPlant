'''
Created on 2020/11/14

@author: ukai
'''

class AbstractPlant(object):
    '''
    classdocs
    '''


    def getPv(self):
        return None # as pv
    
    def update(self, u):
        return None # reward
    
    def reset(self):
        pass