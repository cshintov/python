'''exercise 6.8 compute the number of ways an amount can be changed with the given set of coins'''
import sys

# memoizing the change-combination of sub - amounts
memory = {}

# "new" change-combinations gets added to the answer list
def add_change(amount,coin,change,sub):
    for lst in sub:
        temp = sorted(lst + [coin])
        if not temp in change:
            if sum(temp) == amount:
                change.append(temp)

#answer list is passed to the successive recursive calls by the keyword -argument 'change'
#and it is updated in each recursion with new change-combinations
def count_change(amount,coins,change=[]):
    mincoin = min(coins)
    if amount is mincoin:
        return [[amount]],1
    for i in range(len(coins)):
        div,mod = divmod(amount,coins[i])
        if mod == 0 : 
            change.append([coins[i]]*div)
        if amount > coins[i] and len(coins)>=2:
            rem = amount - coins[i]
            sub = memory.setdefault(rem,[])             #gets the change of the sub-amounts if it is already calculated
            if sub == []:
                sub,num = count_change(rem,coins,sub)
                memory[rem] = sub                       #memoizing the change of the subamounts
            add_change(amount,coins[i],change,sub)
    num_of_ways = len(change)
    return change,num_of_ways

if __name__ == '__main__':
    amount = int(sys.argv[1])
    coins = [1,5,10,25,50]
    change,num_of_ways = count_change(amount,coins)
    #print 'change list',change
    print '{} can be changed with coins {} in {} number of ways'.format(amount,coins,num_of_ways)
