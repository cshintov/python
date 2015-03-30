try:
    print "a"             #prints a
    raise Exception("doom")#exception raised 
except:
    print "b"             #prints b since exception raised
else:
    print "c"             #skips else since exception raised
finally:
    print "d"             #prints d regardless of exceptions
    
#final output
#a
#doom            #wrong :only raised not printed
#b
#d

