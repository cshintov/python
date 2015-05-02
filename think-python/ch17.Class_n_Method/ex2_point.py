'''exercise 17.2 write init method for point class'''

class point(object):
  ''' a two dimensional point with x and y coordinates'''
  #creates a point object and initialises the point coordinates to default values 0,0
  def __init__(self,x=0,y=0):
    self.x = x
    self.y = y

  #prints the point object
  def print_point(p):
    print '(x,y) ==> ({:04.2f},{:04.2f})'.format(p.x,p.y) 

def create_point():
  x = float(raw_input('x: '))
  y = float(raw_input('y: '))
  p = point(x,y)
  return p

def main():
  while True:
    point_a = create_point()
    print 'The point is :',
    point_a.print_point()
    prompt="continue?yes/no:"
    string=raw_input(prompt)
    if string in('n','no'): 
      print "Bye!"
      break

if __name__=='__main__':
  print '*'*30,'\n'
  main()
  print '\n','*'*30
