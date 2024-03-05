#errors and exceptions
#x=-75
#if x<0:
 #   raise Exception('x should be positive')
#assert (x>=0),'x is not positive'

try:
    a=5/5
    b=2+a
#except:
    print('an error happened')
#except Exception as e:
    #print(e)
except ZeroDivisionError:# best way to express
    print("a")
except TypeError:
    print("b")
else:
    print("if no exceptions occurred")#if everything is fine then only this runs
finally:
    print("cleaning up")#it runs always


#defining own exceptions
class ValueTooHighError(Exception):
    pass
class ValueTooSmallError(Exception):
    def __init__(self,message,value):
        self.message=message
        self.value=value

def test_value(x):
    if x>100:
        raise ValueTooHighError(f'value is too high')
    if x<5:
        raise ValueTooSmallError(f'value too small')
try:
    test_value(2)
except Exception as e:
    print(e)
except ValueTooSmallError as e:
    print(e.message, e.value)
