'''
Created on 2020/12/07

@author: ukai
'''
from casestudies.work_template import WorkTemplate


class Runner(object):
    '''
    classdocs
    '''
    
    
    def __init__(self, work):
        
        assert isinstance(work, WorkTemplate)
        self.work = work
        
    def command(self, nCmd, *arg):
        
        if nCmd == 0:
            self.work.build(*arg)
            
        if nCmd == 1:
            self.work.evaluate(*arg)
            
        if nCmd == 2:
            self.work.exportSimulationResultAsFigure(*arg)

        if nCmd == 3:
            self.work.exportSimulationResultAsCsvFormatFile(*arg)
            
        if nCmd == 99:
            self.work.clean(*arg)        