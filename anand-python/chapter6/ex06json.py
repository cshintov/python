'''exercise 6.6 implements the json encoder'''

def enjson(data):
    if isinstance(data,bool):
        if data : return "true"
        else : return "false"

    elif isinstance(data,(int,float)):
        return str(data)

    elif isinstance(data,str):
        return escape_string(data)

    elif isinstance(data,list):
        return "["+', '.join(enjson(d) for d in data)+"]"
    
    elif isinstance(data,dict):
        dctjson = "{ "
        '''
        for key in data:
            dctjson += enjson(key)+":"+enjson(data[key])+", "
        '''
        items = data.items()
        for key,val in items:
             dctjson += enjson(key)+":"+enjson(val)+", "
        dctjson = dctjson[:-2]+" }"
        return dctjson
    else:
        return TypeError("%s is not json serializable" % data)

def escape_string(data):
    data = data.replace('"','\\"')
    data = data.replace('\t','\\t')
    data = data.replace('\n','\\n')
    return data

if __name__ == '__main__':
    stng = 'shinto'
    integ = 6
    flt = 0.7
    flag = True
    lst = [1,2,3,4]
    dct = {'a':1,'b':{'c':3,'d':[1,2]}}
    print 'integer:',enjson(integ)
    print 'float:',enjson(flt)
    print 'bool:',enjson(flag)
    print 'string:',enjson(stng)
    print 'list:',enjson(lst)
    print 'dictionary:',enjson(dct)
