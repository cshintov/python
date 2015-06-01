def integers():
    i = 1
    while True:
        yield i
        i += 1

def squares():
    for i in integers():
        yield i * i

def take(n,seq):
    try :
        for i in range(n):
            print seq.next()
    except StopIteration:
        pass

#take(5,squares())
pyt = ((x,y,z)for z in integers() for y in range(1,z)for x in range(1,y)if x*x + y*y ==z*z)
take(10,pyt)
