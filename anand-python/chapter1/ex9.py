x = 1
def f():
    x = 2 #No problem since we are creating a local x
    return x
print x #global x
print f() #returns local x in f()
print x #global x unchanged
