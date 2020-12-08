'''
Created on 2020/07/09

@author: ukai
'''
import glob
import json
import os
import sqlite3
import traceback

from framework.store_field import StoreField
from framework.util import Utils
import shutil


class Store(object):
    '''
    classdocs
    '''
    
    
    def __init__(self, dbPath, trainLogFolderPath = "./trainlog"):
                
        self.dbPath = dbPath        
        self.trainLogFolderPath = trainLogFolderPath
        if not os.path.exists(trainLogFolderPath):
            os.mkdir(trainLogFolderPath)

    def removeHistory(self):
        
        if os.path.exists(self.dbPath):
            os.remove(self.dbPath)
        if os.path.exists(self.trainLogFolderPath):
            shutil.rmtree(self.trainLogFolderPath)        

    def append(self, storeField):
        assert isinstance(storeField, StoreField)
        
        dataToSave = {
            "buildParameterKey": storeField.buildParameterKey
            , "buildParameterLabel": storeField.buildParameterLabel
            , "buildParameterMemento": storeField.buildParameterMemento
            , "agentMemento": storeField.agentMemento
            , "epoch": storeField.epoch
            , "agentKey": storeField.agentKey   
            }
        
        trainLogFilePath = os.path.join(self.trainLogFolderPath, Utils.generateRandomString(16))        
        with open(trainLogFilePath, "w") as fp:
            json.dump(dataToSave, fp)
            
            
    def update_db(self):

        def create_db(dbPath):
            conn = sqlite3.connect(dbPath)
            cur = conn.cursor()
        
            cur.executescript("""
        
            Drop Table If Exists BuildParameter;
            Create Table BuildParameter(
                build_parameter_id Integer Primary Key,
                build_parameter_key Text Unique,                
                build_parameter_label Text,
                build_parameter_memento Text
            );
        
            Drop Table If Exists TrainLog;
            Create Table TrainLog(
                train_log_id Integer Primary Key,
                build_parameter_id Integer,
                agent_memento Text Unique,
                epoch Integer,
                agent_key Text,
                Unique(agent_key, epoch),
                FOREIGN KEY (build_parameter_id) REFERENCES BuildParameter (build_parameter_id) 
            );
        
            """)
        
            conn.commit()
            conn.close()

        def myupdate(cur, build_parameter_key, build_parameter_label, build_parameter_memento, agent_memento, epoch, agent_key):
            
            cur.execute("""
            Insert Or Ignore Into BuildParameter (
                build_parameter_key
                , build_parameter_label
                , build_parameter_memento
                ) values (?, ?, ?)
            """, (build_parameter_key, build_parameter_label, build_parameter_memento,))
            cur.execute("""
            Select 
                build_parameter_id
                    From BuildParameter
                    Where build_parameter_key = ?
            """, (build_parameter_key,))
            build_parameter_id, = cur.fetchone()
        
            cur.execute("""
            Insert Or Ignore Into TrainLog (
                build_parameter_id
                , agent_memento
                , epoch
                , agent_key
                ) values (?,?,?,?)
            """, (build_parameter_id, agent_memento, epoch,agent_key,))
            
        if not os.path.exists(self.dbPath):
            create_db(self.dbPath)
        
        trainLogFiles = glob.glob(os.path.join(self.trainLogFolderPath, "*"))
        
        conn = None
        cntUpdate = 0
        try:
            conn = sqlite3.connect(self.dbPath)
            cur = conn.cursor()

            for trainLogFilePath in trainLogFiles:
                with open(trainLogFilePath, "r") as fp:
                    dataFromFile = json.load(fp)
                
                myupdate(cur
                         , dataFromFile["buildParameterKey"]
                         , dataFromFile["buildParameterLabel"]
                         , dataFromFile["buildParameterMemento"]
                         , dataFromFile["agentMemento"]
                         , dataFromFile["epoch"]
                         , dataFromFile["agentKey"])

                cntUpdate += 1

            conn.commit()
            
            for trainLogFilePath in trainLogFiles:
                os.remove(trainLogFilePath)
                        
        except:
            traceback.print_exc()
        finally:
            if conn is not None:
                conn.close()
                
        return cntUpdate


    def restore(self, buildParameterLabel="%", epoch = None, buildParameterKey = None, agentKey = None):
                
        def my_find_all(dbPath, buildParameterKey, buildParameterLabel, epoch, agentKey):
            conn = sqlite3.connect(dbPath)
            cur = conn.cursor()
                    
            sql = """\
            Select
                t.agent_memento
                , t.epoch
                , b.build_parameter_memento
                , b.build_parameter_key
                , b.build_parameter_label
                , t.agent_key
                From TrainLog t
                    Join BuildParameter b
                        On t.build_parameter_id = b.build_parameter_id
                Where b.build_parameter_label like ?"""
            if epoch is not None:
                sql += " And epoch = %d" % epoch
            if buildParameterKey is not None:
                sql += " And build_parameter_key = \"%s\"" % buildParameterKey
            if agentKey is not None:
                sql += " And t.agent_key = \"%s\"" % agentKey

            sql += " Order by b.build_parameter_id, t.epoch"
                
            cur.execute(sql, (buildParameterLabel,))
                
            res = [*cur.fetchall()]
            conn.close()

            for agent_memento, epoch, buildParameterMemento, buildParameterKey, buildParameterLabel, agentKey in res:
                yield (agent_memento, epoch, buildParameterMemento, buildParameterKey, buildParameterLabel, agentKey)
        
        for (agent_memento, epoch, buildParameterMemento, buildParameterKey, buildParameterLabel, agentKey) in my_find_all(self.dbPath, buildParameterKey, buildParameterLabel, epoch, agentKey):
            yield StoreField(agent_memento, epoch, buildParameterMemento, buildParameterKey, buildParameterLabel, agentKey)