'''exercise 6.5 Compute Ackermann's function?
This function explodes even for small values of m and n
629826 recursion were able to run without answer for ack(4,1) at 629827 max recursion error raised!
'''
import sys
from math import *
x=0
def ack(m,n):
  global x
  if x == 629826:
    print "Stop!"
    sys.exit(1)
  x += 1
  print x
  if m==0:
    return n + 1
  if m > 0 and n == 0:
    return ack(m-1,1)
  if m > 0 and n > 0:
    return ack(m-1,ack(m,n-1))

def main():
  print 'enter the two parameters'
  m=float(raw_input('m:'))
  n=float(raw_input('n:'))  
  result=ack(m,n)
  print "ackermann({0},{1}):".format(m,n),result
	
if __name__=='__main__':
  print '*'*30,'\n'
  main()
  print '\n','*'*30
