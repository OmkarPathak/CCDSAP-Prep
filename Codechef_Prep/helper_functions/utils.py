import time

def timeit(method):
    '''
        A decorator to find the time taken by a code snippet to execute
    '''
    def time_method(*args, **kwargs):
        start = time.time()
        result = method(*args, **kwargs)
        end = time.time()
        print('{}, {}s'.format(method.__name__, (end - start) * 100))
        return result
        
    return time_method