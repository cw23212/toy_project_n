import time
import json
class data:
    def __init__(self,typep,code_query,idP=None):
        self.type=typep
        if typep=="code":
            self.code=code_query
            self.id=hash(code_query+str(time.time()))%(10**5)
        elif typep=="query":
            self.query=code_query
            self.id=idP
