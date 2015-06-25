'''exercise 6.9 compute all the permutations of the given set'''

#updates the permutation list 
def add(sub_permute,selected,result):
    for item in sub_permute:
        result.append([selected]+item)

#returns a list without the item list_a[index]
def rest(list_a,index):
    return list_a[:index]+list_a[index+1:]

#returns the permutation list
def permute(list_a,result=[]):
    #base case: list with 2 elements 
    if len(list_a) == 2:
        return [list_a,sorted(list_a,reverse=True)]

    for index,item in enumerate(list_a):
        sublist = rest(list_a,index)
        sub_permute = permute(sublist,[])
        add(sub_permute,item,result)
        
    return result

if __name__ == '__main__':
    lst = [1,2,3,4,5]
    result = permute(lst)
    print result
    print 'number of permutations',len(result)
