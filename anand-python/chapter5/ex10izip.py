'''exercise 5.9 implement enumerate function''' 


#returns an iterator 
def izip(iter_a,iter_b):
    ziped = zip(iter_a,iter_b)
    return iter(ziped)

#enumerates the iterable
def my_enumerate(iterable):
    index = iter(range(len(iterable)))
    iterable = iter(iterable)
    enumer = izip(index,iterable)
    return enumer

if __name__=='__main__':
    iter_ = ['a','b','c','d']
    eqiter = my_enumerate(iter_)
    #print list(eqiter)
    for x,c in eqiter:
        print x,c
