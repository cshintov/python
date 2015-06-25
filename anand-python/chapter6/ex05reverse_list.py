'''exercise 6.5 return the list reversed recursively'''
import sys

def reverse(list_,result=None):
    result = []
    for i in range(-1,-(len(list_)+1),-1):
        if isinstance(list_[i],list):
            result.append(reverse(list_[i]))
        else:
            result.append(list_[i])
    return result

if __name__ == '__main__':
    list_ = [[1,2],[3,4],[4,5,[6,7],[8,9,10]]]
    #list_ = [1,2]
    print 'given list:',list_
    print 'reversed list:',reverse(list_)
