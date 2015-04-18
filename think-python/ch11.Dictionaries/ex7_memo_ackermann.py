'''
exercise 11.7 Compute Ackermann's function with memoized version 
This function explodes even for small values of m and n
Not even memoization helps for Ackermann's function
eventhough memoized ack can compute upto 3,8
standard ack can only compute upto 3,6 but takes far greater time than memoized version ; 3.5 seconds compared 75 seconds 
'''
import time
import sys
from math import *
def ack(m,n):
  if m==0:
    return n + 1
  if m > 0 and n == 0:
    return ack(m-1,1)
  if m > 0 and n > 0:
    return ack(m-1,ack(m,n-1))

known={}
def ackermann(m,n):
  if (m,n) in known:
    return known[(m,n)]
  else: 
    if m==0:
      ack = n + 1
    if m > 0 and n == 0:
      ack = ackermann(m-1,1)
    if m > 0 and n > 0:
      ack = ackermann(m-1,ackermann(m,n-1))
    known[(m,n)] = ack
    return ack
    
def main():
  print 'enter the two parameters'
  m=float(raw_input('m:'))
  n=float(raw_input('n:'))  
  start=time.clock()
  result=ackermann(m,n)
  end=time.clock()
  print "ackermann({0},{1}):".format(m,n),result
  print 'memoized ackermann took {} seconds'.format((end-start)*1000)
  print
  
  start=time.clock()
  result=ack(m,n)
  end=time.clock()
  print "ackermann({0},{1}):".format(m,n),result
  print 'standard algorithm took {} seconds'.format((end-start)*1000)
  print
	

if __name__=='__main__':
  print '*'*30,'\n'
  main()
  print '\n','*'*30
