'''
exercise 15.1 finds the distance between two points

'''
from math import sqrt

class point(object):
  '''a point'''
  
def distance(pointa,pointb):
  print pointa.x,pointb.x
  print pointa.y,pointb.y
  dist = sqrt((pointa.x-pointb.x)**2+(pointa.y-pointb.y)**2)
  return dist

def create():
  pnt = point()
  pnt.x = int(raw_input('enter the x coordinate:'))
  pnt.y = int(raw_input('enter the y coordinate:'))
  return pnt
        
def repeat():
  while True:
    pointa = create()
    pointb = create()
    dist = distance(pointa,pointb)
    print 'The distance between the given points:',dist

    prompt="continue?yes/no:"
    string=raw_input(prompt)
    if string in('n','no'): 
      print "Bye!"
      break
      
def main():
  repeat()

if __name__=='__main__':
  print '*'*30,'\n'
  main()
  print '\n','*'*30
