"""with open ('notes.txt','w') as file:#this is much cleaner
    file.write('sometodo...')
file=open('notes.txt','w')
try:
    file.write('sometodo...')
finally:
    file.close()"""
    
"""from threading import Lock
lock=Lock()

lock.acquire()
lock.release()    

#simple and better way
with lock:
"""

#enter and exit methods
class managerfile:
    def __init__(self,filename):
        print('init')
        self.filename=filename    
        
    def __enter__(self):
        print('enter')
        self.file=open(self.filename,'w')
        return self.file 
    def __exit__(self,exc_type,exc_value,exc_traceback):
        if self.file:
            self.file.close()
        if exc_type is not None:
            print('exception')
        #print('exc:',exc_type,exc_value)
        print('exit')
        return True
        
with managerfile('notes.txt') as file:
    print('do something')
    file.write('sometodo')
    file.somemethod()#this is our given error
print('continuing')


from contextlib import contextmanager
@contextmanager
def  open_managed_file(filename):
    f=open(filename,'w')
    try:
        yield f
    finally:
        f.close()
with open_managed_file('notes.txt') as f:
    file.write('sometodo')