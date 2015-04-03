import sys
import os
from  math import *

def check(a,b,c):
  if a < b + c and b < a + c and c < a + b:
    return True
  return False

def is_triangle(a,b,c):
    
  condition=check(a,b,c)
  if condition:
    print "Yes!, they form a Triangle!"
  else:
    print "NO!, they don't form a Triangle!"

def input_sides():

  a="a:"
  a=float(raw_input(a))
  b="b:"
  b=float(raw_input(b))
  c="c:"
  c=float(raw_input(c))
  is_triangle(a,b,c)
  
def main():
  print "Checks whether the given sides form a triangle or not!"
  print "Enter the sides a,b,c"
  input_sides()
  	
if __name__=='__main__':
  print '*'*30,'\n'
  main()
  print '\n','*'*30
