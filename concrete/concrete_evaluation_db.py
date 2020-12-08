'''
Created on 2020/12/02

@author: ukai
'''
import sqlite3
import os
import traceback

class ConcreteEvaluationDb(object):
    '''
    classdocs
    '''


    def __init__(self, evaluationDbPath, buildParameterFactory):
        '''
        Constructor
        '''
        
        self.evaluationDbPath = evaluationDbPath
        self.buildParameterFactory = buildParameterFactory

    def removeRemainedFiles(self):
        if os.path.exists(self.evaluationDbPath):
            os.remove(self.evaluationDbPath)
        
    def initDb(self):
        
        conn = sqlite3.connect(self.evaluationDbPath)
        cur = conn.cursor()
        
        cur.executescript("""
  
Drop Table If Exists Agent;    
Create Table Agent(
    id Integer Primary Key,
    agentKey Text,
    epoch Integer,
    buildParameterLabel Text,
    buildParameterMemnto Text,
    Unique(agentKey, epoch)
);

Drop Table If Exists Evaluation;
Create Table Evaluation(
    id Integer Primary Key,
    idAgent Integer,
    evaluatorClass Text,
    name Text,
    value Float
);
        
        """)        
        
        conn.commit()
        conn.close()
        
        pass
    
    
    def saveSingleRow(self, cur, agentKey, epoch, buildParameterLabel, buildParameterMemnto, evaluatorClass, name, value):
        
        sql1 = """        
Insert Or Ignore Into Agent (agentKey, epoch, buildParameterLabel, buildParameterMemnto)
    values (?, ?, ?, ?);
        """
        
        sql2 = """        
Select id 
    From Agent
    Where agentKey = ?
    And epoch = ?
        """
        
        sql3 = """
Insert or Ignore Into Evaluation (idAgent, evaluatorClass, name, value)
    values (?, ?, ?, ?)        
        """
        
        cur.execute(sql1, (agentKey, epoch, buildParameterLabel, buildParameterMemnto))
        
        cur.execute(sql2, (agentKey, epoch))
        agentId, = cur.fetchone()
        
        cur.execute(sql3, (agentId, evaluatorClass, name, value))

    def saveGeneratedStats(self, statsGenerator):
        
        conn = None
        nUpdate = 0
        try:
            conn = sqlite3.connect(self.evaluationDbPath)
            cur = conn.cursor()

            for agentKey, epoch, buildParameterLabel, buildParameterMemnto, evaluatorClass, stats in statsGenerator:
                for name in stats:
                    self.saveSingleRow(cur, agentKey, epoch, buildParameterLabel, buildParameterMemnto, evaluatorClass, name, stats[name])
                    nUpdate += 1
    
            conn.commit()
            conn.close()                                    
        except Exception as inst:
            if conn is not None:
                conn.close()
            raise inst
        
        return nUpdate

    
    
    def exists(self, agentKey, epoch, evaluatorClass = None):
        
        conn = sqlite3.connect(self.evaluationDbPath)
        cur = conn.cursor()
        
        sql2 = """        
Select count(*)
    From Agent a
        Join Evaluation e
            On a.id == e.idAgent
    Where a.agentKey = ?
        And a.epoch = ?
        """ 
        if evaluatorClass is not None:
            sql2 += "And e.evaluatorClass = \"%s\"" % evaluatorClass
        
        cur.execute(sql2, (agentKey, epoch))
        count, = cur.fetchone()

        conn.close()
        
        return count > 0
    
    def export(self, buildParameterLabel, agentKey, epoch, evaluatorClass):
        
        conn = sqlite3.connect(self.evaluationDbPath)
        cur = conn.cursor()
        
        sql1 = """        
Select a.agentKey
    , a.epoch
    , a.buildParameterLabel
    , a.buildParameterMemnto
    , e.name
    , e.value
    From Agent a
        Join Evaluation e
            On a.id == e.idAgent
    Where a.buildParameterLabel like \"%s\"
        """ % buildParameterLabel 

        if evaluatorClass is not None:
            sql1 += " And e.evaluatorClass = \"%s\"" % evaluatorClass
        if epoch is not None:
            sql1 += " And a.epoch = %d" % epoch
        if agentKey is not None:
            sql1 += " And a.agentKey = \"%s\"" % agentKey
            
        cur.execute(sql1)
        target = [*cur.fetchall()]
        
        tbl = []
        for agentKey, epoch, buildParameterLabel, buildParameterMemnto, name, value in target:            
            
            buildParameter = self.buildParameterFactory.create()
            buildParameter.loadMemento(buildParameterMemnto)
            
            tbl.append({"agentKey": agentKey, "epoch": epoch, **buildParameter.__dict__, "evaluationName": name, "evaluationValue": value})
        
        conn.close()

        return tbl
        