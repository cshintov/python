'''exercise 5.6.2 Draw a koch - snowflake '''

import sys
from  math import *
from swampy.TurtleWorld import *
def setup(dist):
  bob=Turtle()
  bob.delay=.0001
  pu(bob)
  rt(bob)
  fd(bob,dist)
  lt(bob)
  pd(bob)
  return bob

def koch(t,length):
  if length < 3:
    fd(t,length)
    return
  koch(t,length/3)
  lt(t,60)
  koch(t,length/3)
  rt(t,120)
  koch(t,length/3)
  lt(t,60)
  koch(t,length/3)

def snowflake(t,length):
  koch(t,length)
  rt(t,120)
  koch(t,length)
  rt(t,120)
  koch(t,length)

def main():
  print "Here are both the koach curve and the snowflake using it!"
  length=int(raw_input('What should be the length of the curve?(should be >= 100):'))
  world=TurtleWorld()
  bob=setup(50) 
  koch(bob,length)
  al=setup(200)
  snowflake(al,length)
  wait_for_user()

if __name__=='__main__':
  print '*'*30,'\n'
  main()
  print '\n','*'*30


