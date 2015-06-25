l = [[5, 'a'], [3, 'c'], [4, 'b']]
print l
print sorted(l)
print sorted(l, key=lambda item: item[1])


def ith(x):

    def key(lst):
        return lst[x]
    return key

print 'sorting using closure'
print sorted(l, key=ith(1))
