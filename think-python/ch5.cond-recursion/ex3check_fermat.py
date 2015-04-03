import sys
import os
from  math import *
def check_fermat(a,b,c,n):
    
  left=pow(a,n)+pow(b,n)
  if left == pow(c,n):
    print "Holly Smokes! Fermat was wrong!"
  else:
    print "NO! That doesn't work!"

def input_param():

  a="a:"
  a=int(raw_input(a))
  b="b:"
  b=int(raw_input(b))
  c="c:"
  c=int(raw_input(c))
  n="n:"
  n=int(raw_input(n))
  if n<=2:
    print "n should be greater than TWO!"
    input_param()

  check_fermat(a,b,c,n)
  sys.exit(0)
  
def main():
  print "Checks whether a^n+b^n equals c^n"
  print "Enter the integer numbers a,b,c and n"
  input_param()
  	
if __name__=='__main__':
  print '*'*30,'\n'
  main()
  print '\n','*'*30
