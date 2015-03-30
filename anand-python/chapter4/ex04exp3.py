def f():
    try:
        print "a"         #prints a
        return            #returns from the function
    except:
        print "b"         #never reaches here
    else:
        print "c"         #never reaches here
    finally:
        print "d"         #Prints d;finally gets executed before try block is exited

f()


#final output
#a
#d
