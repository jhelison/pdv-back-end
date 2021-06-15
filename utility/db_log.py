from time import time

def stopwatch(fun):
    def inner(*args, **kwargs):
        start = time()
        
        res = fun(*args, **kwargs)
        
        total_time = "%.6f" % ((time() - start) / 1000)
        
        print("##### Total time taken to execute:", fun.__name__, args, kwargs, total_time, "#####")
        
        return res
        
    return inner