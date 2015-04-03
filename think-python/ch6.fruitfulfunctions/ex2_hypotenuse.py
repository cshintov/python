from math import *
def hypotenuse(a,b):
  print 'a is',a
  print 'b is',b
  result=sqrt( a**2 + b**2 )
  return result

def main():
  print 'enter the sides'
  a=float(raw_input('a:'))
  b=float(raw_input('b:'))  
  result=hypotenuse(a,b)
  print "the hypotenuse:",result
	
if __name__=='__main__':
  print '*'*30,'\n'
  main()
  print '\n','*'*30
