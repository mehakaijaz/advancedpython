'''from multiprocessing import Process,Value,Array,Lock
import time
def add_100(nums,lock):
    for i in range(100):
        time.sleep(0.01)
        """this portion can also be written as
        for num in nums:
            num +=1"""
        for i in range(len(nums)):
            with lock:
                nums[i] +=1
        """lock.acquire()
        num.value +=1
        lock.release()
    #use lock as context manager which will automatically acquire and release no need to type extra code
        with lock:
            num.value +=1"""
        
if __name__=='__main__':
    lock=Lock()
    #single value
    #shared_num=Value('i',0)#takes two arguments datatype as string''and then a starting value
    #array
    shared_array=Array('d',[0.0,100.0,87.0,56.0])
    #print('nim',shared_num.value)
    print('arry',shared_array[:])
    p1=Process(target=add_100,args=(shared_array,lock))
    p2=Process(target=add_100,args=(shared_array,lock))
    
    p1.start()
    p2.start()
    
    p1.join()
    p2.join()
    
    #print('num at end',shared_num.value)
    print('arry at the end ',shared_array[:])
    '''
    
from multiprocessing import Process,Value,Array,Lock,Pool
from multiprocessing import Queue
import time
def square(nums,queue):
    for i in nums:
        queue.put(i*i)
        
def make_neg(nums,queue):
    for i in nums:
        queue.put(-1*i)
        
if __name__=='__main__': 
    nums=range(1,8)
    q= Queue()
    
    p1=Process(target=square,args=(nums,q))
    p2=Process(target=make_neg,args=(nums,q))
    
    p1.start()
    p2.start()
    
    p1.join()
    p2.join()
    
    while not q.empty():
        print(q.get())
        
        
# for pool
def cube(num):
    return num*num*num

if __name__=='__main__':
    num=range(10)
    pool=Pool()
    #map,apply ,join,close
    result=pool.map(cube,num)
    #pool.apply(cube,num[0])
    pool.close()
    pool.join()
    print(result)
    #print(a)