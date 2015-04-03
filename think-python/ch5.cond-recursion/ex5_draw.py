import sys
import os
from  math import *
from swampy.TurtleWorld import *
def setup(dist):
  bob=Turtle()
  bob.delay=0.001
  pu(bob)
  rt(bob)
  fd(bob,dist)
  lt(bob)
  pd(bob)
  return bob

world=TurtleWorld()
bob=setup(300)
def draw(t,length,n):
  if n==0:
    return
  angle=50
  fd(t,length*n)
  lt(t,angle)
  draw(t,length,n-1)
  rt(t,2*angle)
  draw(t,length,n-1)
  lt(t,angle)
  bk(t,length*n)  
length=int(sys.argv[1])
n=int(sys.argv[2])
draw(bob,length,n)
wait_for_user()
