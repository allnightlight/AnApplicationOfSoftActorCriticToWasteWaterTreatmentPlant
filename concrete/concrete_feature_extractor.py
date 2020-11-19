'''
Created on 2020/11/17

@author: ukai
'''
from skeleton.abstract_feature_extractor import AbstractFeatureExtractor
import tensorflow

class ConcreteFeatureExtractor(AbstractFeatureExtractor, tensorflow.keras.Model):
    '''
    classdocs
    '''
    
    def __init__(self):
        super().__init__()

