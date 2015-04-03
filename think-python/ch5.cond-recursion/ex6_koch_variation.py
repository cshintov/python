'''exercise 5.6.3 Draw a koch-snowflake variation found in koch curve in wiki pedia
Following is the implementation of the one dimensional, 90 degree, quadratic type 2 curve and snowflake with it 
'''

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

'''
fractal dimension = log (number of elements in generator) / log (scaling down factor)
generator is the form yielded by the first iteration (given in wikipage)

http://en.wikipedia.org/wiki/Koch_snowflake
http://en.wikipedia.org/wiki/List_of_fractals_by_Hausdorff_dimension

fractal dimension of the quadratic type 2 koch curve= log 8 /log 4
Reading the following pdf will give us the idea of koch curve generalization

http://archive.bridgesmathart.org/2000/bridges2000-301.pdf

The algorithm is determined by the generator shape which gives us the rotation angles
'''

def koch(t,length):
  if length < 4:
    fd(t,length)
    return
  koch(t,length/4)
  lt(t,90)
  koch(t,length/4)
  rt(t,90)
  koch(t,length/4)
  rt(t,90)
  koch(t,length/4)
  koch(t,length/4)
  lt(t,90)
  koch(t,length/4)
  lt(t,90)
  koch(t,length/4)
  rt(t,90)
  koch(t,length/4)
  
'''Snowflake of quadratic type 2 curve needs four of the original curve'''  
def snowflake(t,length):
  koch(t,length)
  rt(t,90)
  koch(t,length)
  rt(t,90)
  koch(t,length)
  rt(t,90)
  koch(t,length)


def main():
  print "Here are both the koach curve and the snowflake using it!"
  length=int(raw_input('What should be the length of the curve?(should be >= 50):'))
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

