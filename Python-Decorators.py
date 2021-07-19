import time 

def Timer(f):
    def wrapper(*args, **kwargs):
        start = time.time()
        f(*args, **kwargs)
        total = time.time() - start
        return total
    return wrapper
    
@Timer
def TestFunction(n):
    for i in range(n):
        pass 
    
print(TestFunction(999999))
