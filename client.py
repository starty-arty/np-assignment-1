# https://stackoverflow.com/questions/6920858/interprocess-communication-in-python#answer-6921402

import time
from multiprocessing.connection import Client

address = ('localhost', 6000)
conn = Client(address, authkey=str.encode('secret password'))
# conn.send('close')
# can also send arbitrary objects:
# conn.send(['a', 2.5, None, int, sum])
print('Connection established. Say hi!')
while(True):
  inp=str(input())
  sent_ts=time.time()
  conn.send(inp)
  conn.send(sent_ts)
  if(inp=="close"):
    break
conn.close()