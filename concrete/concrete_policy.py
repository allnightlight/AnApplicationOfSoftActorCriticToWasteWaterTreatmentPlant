'''
Created on 2020/11/15

@author: ukai
'''

import tensorflow

from sac.sac_policy import SacPolicy


class ConcretePolicy(SacPolicy, tensorflow.keras.Model):
    '''
    classdocs
    '''


    def __init__(self, nMv):
        super().__init__()
        
        SacPolicy.__init__(self)
        
    def call(self, batchDataFeature):
        raise NotImplementedError()