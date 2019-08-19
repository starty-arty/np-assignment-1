# https://stackoverflow.com/questions/6920858/interprocess-communication-in-python#answer-6921402

from multiprocessing.connection import Listener
import time

address = ('localhost', 6000)     # family is deduced to be 'AF_INET'
listener = Listener(address, authkey=str.encode('secret password'))
conn = listener.accept()
print('Connection established. Say hi!')
# print('connection established from ', end='')
# print(listener.last_accepted)
num_msg, avg_time = 0, 0
while True:
    msg = conn.recv()
    recv_ts=time.time()
    print(msg)
    sent_ts = conn.recv()
    avg_time=(avg_time*num_msg+recv_ts-sent_ts)/(num_msg+1)
    num_msg=num_msg+1
    if msg == 'close':
        conn.close()
        break
print("Average delay: ", end='');
print(avg_time, end='')
print('s')
listener.close()