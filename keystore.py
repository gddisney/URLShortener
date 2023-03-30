import json
from threading import Lock
import ast

class KeyStore(object):
    """KeyStore is a thread safe python class that is intended to replace sqlite3 for most use cases."""
    def __init__(self,**kwargs):
            global key
            global value
            global KeyStore
            for key, value in kwargs.items():
                    self.key = key
                    self.value = value
                    KeyStore = {}
                    KeyStore[key] = value
                    for key in KeyStore:
                        setattr(self, key, KeyStore[key])


    def __missing__(self):
         KeyStore[key] = value
         return 
    

    def __setitem__(self, key, value):
        KeyStore[key] = value
        setattr(self, key, KeyStore[key])
        return KeyStore
    

    def __getitem__(self, key):
         try:
            return KeyStore[key]
         except KeyError:
            return self.__missing__()
         

    def __delitem__(self, key):
            KeyStore[key] = ""
            return KeyStore[key]
    

    def __dict__(self):
        KeyStore[key] = value
        return KeyStore


    def __repr__(self):
         return repr(KeyStore)
    

    def lock(self):
         lock = Lock()
         return lock.acquire
    

    def unlock(self):
        lock = Lock()
        return lock.release 
    

    def get(self):
        return KeyStore
    

    def set(self,key,value):
        KeyStore[key] = value
        return KeyStore
    

    def write(self,id,database):
         self.lock()
         db = open(database,'a+')
         db.write(f"{id} |#| {KeyStore}\n")
         db.close()
         self.unlock()
         return db
    
    def read(self,database):
        self.lock()
        db = open(database, 'r+').read()
        delimeter = "|#|" 
        result = [i for i in db]
        self.unlock()
        return result
    
    def get(self,id,database):
        self.lock()
        db = open(database, 'r+').read()
        db = db.split("\n")
        result = [i for i in db if id in i]
        result = str(result[0]).split("|#|")[1][1:]
        self.unlock()
        return ast.literal_eval(json.loads(json.dumps(result)))
    
    def len(self,database):
        self.lock()
        db = open(database, 'r+').read()
        db = db.split("\n")
        self.unlock()
        return len(db)
    
    def json(self):
         return json.dumps(KeyStore)
    

    def dict(self,blob):
         return json.loads(blob)
    
 
def test():    
    x = KeyStore(hello="world")
    print("Class Test:")
    print(x)
    print("Attribute Test:")
    print(x.hello)
    print("Dict Test:")
    x['hello'] = 'bye'
    print(x)
    print("Attribute Test:")
    x.hello = "Goodbye"
    x['hello'] = x.hello
    print(x)
    print("Write Test:")
    x.write("id-test","id.db")
    print("Read Test:")
    print(x.read("id-test","id.db"))
    print("Len Test:")
    _len = x.len('id.db')
    x.write(f"id-test-{_len}","id.db")
    y = x.read(f"id-test-{_len}","id.db")
    print("JSON Dump Test:")
    _json = x.json()
    print(_json)
    print("JSON Load Test:")
    _dict = x.dict(_json)
    print(_dict['hello'])
    print("Missing key test:")
    x['missing']
    print(x)


if __name__ == '__main__':
     test()