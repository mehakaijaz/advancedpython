

from threading import Thread
import os
import time
def square_numbers():
    for i in range(100):
        i*i
        time.sleep(0.1)

threads=[]
num_thread=10

#creating threads

for i in range(num_thread):
    p=Thread(target=square_numbers)
              #args=())
    threads.append(p)
    
#start
for p in threads:
    p.start()
    
#join
for p in threads:
    p.join()
    
print('end main')