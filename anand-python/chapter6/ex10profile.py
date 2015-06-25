'''
exericse 6.10 compute the time time taken by a function to execute using
decorator.
'''

from time import time
from ex09permute import *

def profile(func):
    def newfunc(*args):
        start = time()
        result = func(*args)
        end = time()
        print 'Took','%4.2f'%(end-start),'seconds!'
        return result
    return newfunc

if __name__ == '__main__':
    lst = [1,2,3,4,5,6,7,8,9,10]
    permute = profile(permute)
    result = permute(lst)
    #print result
    print 'number of permutations',len(result)
