
import sys

def flaten(list_,result=None):
    if result is None:
        result = []
    for i in list_:
        if isinstance(i,(list)):
            flaten(i,result)
        else:
            result.append(i)
    return result

if __name__ == '__main__':
    list_ = [[1,2],[3,4],[4,5,[6,7],[8,9,10]]]
    print flaten(list_)
