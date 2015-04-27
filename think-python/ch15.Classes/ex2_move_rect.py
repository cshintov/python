'''
exercise 15.2 move the rectangle to a different point

'''
class point(object):
  '''a point'''

class rectangle(object):
  '''
    a rectangle with attributes 
    leftbottom corner,height,width
  '''

def create_rectangle():
  box = rectangle()
  box.height=float(raw_input('enter the height: '))
  box.width = float(raw_input('enter the width: '))
  box.corner = point()
  box.corner.x= float(raw_input('enter x: '))
  box.corner.y= float(raw_input('enter y: '))
  return box
  
def move(rect,dx,dy):
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
    box = create_rectangle()
    print_rect(box)
    x = int(raw_input('enter the x coordinate of the destination:'))
    y = int(raw_input('enter the y coordinate of the destination:'))
    move(box,x,y)
    print_rect(box)
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
