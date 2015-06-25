'''exercise 6.3 unflatten a dictionary'''

def unflatten(dct,result=None):
    if result is None:
        result = {}
    for key in dct:
        if '.' in key:
            p = key.find('.')
            keyf = key[:p]
            keyl = key[p+1:]
            result.setdefault(keyf,{})
            result[keyf][keyl] = dct[key]
        else:
            result[key] = dct[key]
    for key in result:
        if isinstance(result[key],dict):
            result[key] = unflatten(result[key])
    return result

if __name__ == '__main__':
    dct = {'a':1,'b.x':2,'b.y':3,'b.z.l':4,'b.z.m':5,'c':6}
    print unflatten(dct)
