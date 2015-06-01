'''exercise 5.8 write a function that returns the first element of the iterator and an equivalent iterator'''

from itertools import chain

#returns the first element and the iterator
def peep(it):
    eqiter = []
    for i in it:
        eqiter.append(i)
    first = eqiter[0]
    eqiter = iter(eqiter)
    return first,eqiter

if __name__=='__main__':
    iter_ = iter(range(5))
    first,eqiter = peep(iter_)
    print first,list(eqiter)
