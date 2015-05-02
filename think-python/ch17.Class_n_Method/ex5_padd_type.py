'''exercise 17.4 Implementing add method using dispatch based on type feature 
   the __add__ method calls apropriate methods ,add_point if other is of point type 
   add_tuple is other is of type tuple
'''

class point(object):
  ''' a two dimensional point with x and y coordinates'''
  def __init__(self,x=0,y=0):
    self.x = x
    self.y = y
  
  def __add__(self,other):
    if isinstance(other,point):
      return self.add_point(other)
    else:
      return self.add_tuple(other)
  
  #handles the add method when the point is on the right side of the operator   
  def __radd__(self,other):
    return self.__add__(other)

  def add_point(self,other):
    sum = point()
    sum.x = self.x + other.x
    sum.y = self.y + other.y
    return sum
  
  def add_tuple(self,tup):
    sum = point()
    sum.x = self.x + tup[0]
    sum.y = self.y + tup[1]
    return sum

  #prints the point object
  def __str__(p):
    return '({:04.2f},{:04.2f})'.format(p.x,p.y) 

def create_point(choice='p'):
  x = float(raw_input('x: '))
  y = float(raw_input('y: '))
  if choice == 'p':
    p = point(x,y)
  else:
    p = (x,y)
  return p

def main():
  while True:
    print 'enter the first point'
    point_a = create_point()
    print 'enter the second point'
    point_b = create_point()
    print 'enter the tuple'
    point_tup = create_point('t')
    print 'The sum of the points is :',
    print point_a + point_b
    print 'the sum of the first point and the tuple is :',
    print point_tup + point_a 
    prompt="continue?yes/no:"
    string=raw_input(prompt)
    if string in('n','no'): 
      print "Bye!"
      break

if __name__=='__main__':
  print '*'*30,'\n'
  main()
  print '\n','*'*30
