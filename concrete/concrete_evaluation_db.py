'''
Created on 2020/12/02

@author: ukai
'''
import sqlite3
import os

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
    
    def save(self, agentKey, epoch, buildParameterLabel, buildParameterMemnto, evaluatorClass, stats):
        
        conn = sqlite3.connect(self.evaluationDbPath)
        cur = conn.cursor()
        
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
        
        for name in stats:
            cur.execute(sql3, (agentId, evaluatorClass, name, stats[name]))
        
        conn.commit()
        conn.close()
    
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
    
    def export(self, buildParameterLabel = None):
        
        conn = sqlite3.connect(self.evaluationDbPath)
        cur = conn.cursor()
        
        sql1 = """        
Select agentKey, epoch, buildParameterLabel, buildParameterMemnto from Agent
"""
        if buildParameterLabel is not None:
            sql1 += "Where buildParameterLabel like \"%s\"" % buildParameterLabel
   
        sql2 = """        
Select e.name, e.value
    From Agent a
        Join Evaluation e
            On a.id == e.idAgent
    Where a.agentKey = ?
        And a.epoch = ?
        """

        cur.execute(sql1)
        target = [*cur.fetchall()]
        
        tbl = []
        for agentKey, epoch, buildParameterLabel, buildParameterMemnto in target:            
            
            buildParameter = self.buildParameterFactory.create()
            buildParameter.loadMemento(buildParameterMemnto)
            
            head = {"agentKey": agentKey, "epoch": epoch, **buildParameter.__dict__}

            cur.execute(sql2, (agentKey, epoch))            
            for name, value in cur.fetchall():
                tbl.append({**head, "evaluationName": name, "evaluationValue": value})
        
        conn.close()

        return tbl
        