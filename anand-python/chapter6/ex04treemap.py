'''exercise 6.4 maps a function to a list'''

def treemap(list_,func):
    result = []
    for i in list_:
        if isinstance(i,(list)):
            result.append(treemap (i,func))
        else:
            result.append(func(i))
    return result

def square(x):
    return x*x

def strdouble(s):
    return s+s

if __name__ == '__main__':
    dct = ['a','b',['x','y','z',['l','m']],'c']
    f = square
    s = strdouble
    idct = [1,2,[3,4,[4,5]]]
    print treemap(dct,s)
    print treemap(idct,f)
