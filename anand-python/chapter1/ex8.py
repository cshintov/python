x = 1
def f():
    return x # No problem in using x since we are not modifying it otherwise we would've needed global stmt
print x #prints 1
print f() #prints 1 

