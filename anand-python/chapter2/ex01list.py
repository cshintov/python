x = [0, 1, [2]]
x[2][0] = 3
print x # [0,1,[3]]
x[2].append(4)
print x # [0,1,[3,4]]
x[2] = 2
print x # [0,1,2]
