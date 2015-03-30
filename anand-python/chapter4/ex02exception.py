try:
    print "a"   #prints a no problem
except:
    print "b"   #since try works fine except is skipped
else:
    print "c"   #prints c since no exception raised
finally:
    print "d"   #prints d regardless of exceptions
    
#final output
#a
#c
#d
    
