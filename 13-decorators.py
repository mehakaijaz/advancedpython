#decorator=A decorator in Python is like a tool that helps you modify or add extra abilities to a function. 
# It's like wrapping a gift – you keep the original gift, but you put it inside a decorative wrapper.
import functools

"""def start_end_decorator(func):
    @functools.wraps(func)#wraps this here only.it allows "add func" in add.__name__
    def wrapper(*args, **kwargs):
        print("start")
        result=func(*args, **kwargs)
        print("end")
        return result
    return wrapper

def printname():
    print('alex')

#printname=start_end_decorator(printname)#this will print start alex end
 
printname()

@start_end_decorator
def add(x):
    return x+5
result=add(10)
print(help(add))
print(add.__name__)
print(result)"""

"""def repeat(num_times):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result=func(*args, **kwargs)
            return result            
        return wrapper
    return decorator_repeat

def debug(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        args_repr=[repr(a) for a in args]
        kwargs_repr=[f'{k}={v!r}' for k,v in kwargs.items()]
        signature=",".join(args_repr + kwargs_repr)
        print(f'calling{func.__name__}({signature})')
        result=func(*args, **kwargs)
        print(f'{func.__name__!r} returned {result}')
        return result
    return wrapper

@debug
@repeat(num_times=3)
def greet(name):
    print(f'hello {name}')
    
greet("alex")"""

#class decorator

class countcalls:
    def __init__(self,func):
        self.func=func
        self.num_calls=0
    def __call__(self, *args, **kwargs):
        #print('hi there')
        self.num_calls+=1
        print(f'this is executed {self.num_calls} times')
        return self.func(*args, **kwargs)
        


@countcalls
def say_hello():
    print('hello')
    
say_hello()