
import sys
import os

def is_between(x,y,z):
  print 'x is',x
  print 'y is',y
  print 'z is',z
  return x <= y and y <= z

def main():
  print "Checks whether three numbers x,y,z satisfies the rule x <= y <=z \nEnter the three numbers to check in order x, y, z"
  x=float(raw_input('x:'))
  y=float(raw_input('y:'))
  z=float(raw_input('z:'))
  if is_between(x,y,z):
    print "The given numbers satisfies the rule:{0} <= {1} <= {2}".format(x,y,z)
  else:
    print "The given numbers Does Not satisfy the rule:{0} <= {1} <= {2}".format(x,y,z)
	
if __name__=='__main__':
  print '*'*30,'\n'
  main()
  print '\n','*'*30
