'''
Created on 2020/12/02

@author: ukai
'''
import unittest
from concrete.concrete_evaluation_db import ConcreteEvaluationDb
from concrete.concrete_build_parameter_factory import ConcreteBuildParameterFactory
from concrete.concrete_build_parameter import ConcreteBuildParameter


class Test(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        super(Test, cls).setUpClass()
        
        cls.db = ConcreteEvaluationDb("test.sqlite", buildParameterFactory=ConcreteBuildParameterFactory())
        
    @classmethod
    def tearDownClass(cls):
        super(Test, cls).tearDownClass()
        
#         cls.db.removeRemainedFiles()

    def test001(self):
        
        assert isinstance(self.db, ConcreteEvaluationDb)
        
        self.db.initDb()
        
    def test002(self):
        
        assert isinstance(self.db, ConcreteEvaluationDb)
        
        self.db.initDb()
        
        agentKey = "abc"
        epoch = 123
        evaluatorClass = "evaluator001"
        
        def gen():
            yield agentKey, epoch, "test", "who are you?", evaluatorClass, {"count": 123, "XXX": 456}
        
        self.db.saveGeneratedStats(gen())
        
        assert self.db.exists(agentKey, epoch, evaluatorClass)
        assert self.db.exists(agentKey, epoch + 1, evaluatorClass) == False
        assert self.db.exists(agentKey + "hoge", epoch, evaluatorClass) == False
        assert self.db.exists(agentKey, epoch) 

    def test004(self):
        
        assert isinstance(self.db, ConcreteEvaluationDb)
        
        self.db.initDb()
        
        nRow = 3
        stats = {"count": 123, "XXX": 456}
        
        def gen():
            
            for k1 in range(nRow):
                agentKey = "abc %d" % k1
                buildParameterLabel = "test %d" % k1
                epoch = 123
                evaluatorClass = "evaluator001"
                
                buildParameter = ConcreteBuildParameter()
                yield agentKey, epoch, buildParameterLabel, buildParameter.createMemento(), evaluatorClass, stats         
        
        assert self.db.saveGeneratedStats(gen()) > 0

        tbl = self.db.export(buildParameterLabel = "%", agentKey = None, epoch = None, evaluatorClass = "evaluator001")
        
        assert len(tbl) == nRow * len(stats)
                
        tbl = self.db.export(buildParameterLabel = "test 0", agentKey = None, epoch = None, evaluatorClass = None)
                
        assert len(tbl) == len(stats), len(tbl)

        tbl = self.db.export("test%", agentKey = None, epoch = None, evaluatorClass = None)
                
        assert len(tbl) == len(stats) * nRow, len(tbl)
        
        tbl = self.db.export(buildParameterLabel = "%", agentKey = "abc 0", epoch = None, evaluatorClass = None)
                
        assert len(tbl) == len(stats), len(tbl)

        tbl = self.db.export(buildParameterLabel = "%", agentKey = "abc 0", epoch = 123, evaluatorClass = None)
                
        assert len(tbl) == len(stats), len(tbl)
        
        tbl = self.db.export(buildParameterLabel = "%", agentKey = "abc 0", epoch = 123, evaluatorClass = "evaluator001")
                
        assert len(tbl) == len(stats), len(tbl)
        
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test001']
    unittest.main()