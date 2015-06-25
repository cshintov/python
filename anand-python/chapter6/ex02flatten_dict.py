'''exercise 6.2 flatten a dictionary'''

def flatten(dct,pkey=None,result=None):
    if result is None:
        result = {}
    for key in dct:
        if isinstance(dct[key],(dict)):
            if pkey != None:
                prtkey = pkey+'.'+key
            else :
                prtkey = key
            flatten(dct[key],prtkey,result)
        else:
            if pkey == None:
                result[key] = dct[key]
            else:
                result[pkey+'.'+key] = dct[key]
    return result

if __name__ == '__main__':
    dct = {'a':1,'b':{'x':2,'y':3,'z':{'l':4,'m':5}},'c':6}
    print flatten(dct)
