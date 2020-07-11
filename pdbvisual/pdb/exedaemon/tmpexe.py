import json
from data import data
import daemon
from client import client

c=client()
d=data("code","123","print(3)")
j=json.dumps(d.data)
a=c.send(j)
print(a)