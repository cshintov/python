x = 1
def f():
        print x #Works fine
        y = x 
        '''Thought it would work fine y is assigned value of x declared before f() : 1
           Actually error: undefined x ???? print x and return x works fine not assignment
           '''
        x = 2 #local x created and assigned 2
        return x + y # returns 2 + 1 : 3
print x   #1
print f() #Thought 3 But turned out error
print x   #never reaches here

