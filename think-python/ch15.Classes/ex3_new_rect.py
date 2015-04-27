'''
exercise 15.3 creates a new rectangle with the dimensions of the given rectangle at a different point

'''
from copy import copy,deepcopy
class point(object):
  '''a point'''
class rectangle(object):
  '''
    a rectangle with attributes 
    leftbottom corner,height,width
  '''

def create():
  box = rectangle()
  box.height = 1
  box.width = 1
  box.corner = point()
  box.corner.x=0
  box.corner.y=0
  return box
  
def new(box,dx,dy):
  rect = deepcopy(box)
  rect.corner.x += dx
  rect.corner.y += dy
  return rect

def print_rect(box):
  print 'height',box.height
  print 'width',box.width
  print 'corner',print_point(box.corner)

def print_point(pnt):
  return pnt.x,pnt.y
  
def repeat():
  while True:
    box = create()
    print_rect(box)
    x = int(raw_input('enter the x coordinate of the destination:'))
    y = int(raw_input('enter the y coordinate of the destination:'))
    box_a = new(box,x,y)
    print_rect(box_a)
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
