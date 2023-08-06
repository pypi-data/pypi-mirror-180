from math import ceil


class hyperlist:
    
    def __init__(self, *vs, **kvs):
        self.core = list(*vs, **kvs)
    
    def __repr__(self): return repr(self.core)
    def __str__(self): return str(self.core)

    def cut(self, size):
        data = self.core
        lis = [data[size*(i-1): size*i] for i in range(1, ceil(len(data)/size)+1)]
        lis = [hyperlist(x) for x in lis]
        return hyperlist(lis)