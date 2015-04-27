'''
exercise 15.4 Draw Rectangle and Circle
'''
from swampy.World import World
class point(object):
  '''a point with attributes 
  x and y coordinates'''

class rectangle(object):
  
  '''a rectangle with attributes 
  leftbottom corner,height,width'''

class circle(object):
    '''a circle with attributes
    center point,radius length'''

def create_point():
  pnt = point()
  pnt.x= float(raw_input('enter x: '))
  pnt.y= float(raw_input('enter y: '))
  pnt.colour = raw_input('enter the colour of the point')
  return pnt

def create_rectangle():
  box = rectangle()
  box.height=float(raw_input('enter the height: '))
  box.width = float(raw_input('enter the width: '))
  box.corner = point()
  box.corner.x= float(raw_input('enter x: '))
  box.corner.y= float(raw_input('enter y: '))
  box.colour=raw_input('colour: ')
  return box

def create_circle():
  cir = circle()
  circle.center = point()
  circle.center.x = float(raw_input('enter x of the center: '))
  circle.center.y = float(raw_input('enter y of the center: '))
  cir.radius = float(raw_input('enter radius of the circle: '))
  cir.colour=raw_input('colour: ')
  return cir
'''
def print_rect(box):
  print 'height',box.height
  print 'width',box.width
  print 'left-bottom corner',print_point(box.corner)

def print_point(pnt):
  return pnt.x,pnt.y
'''
def find_dim(box):
  bbox = [list((box.corner.x,box.corner.y))]
  rt = []
  rt.append(box.corner.x + box.width)
  rt.append(box.corner.y + box.height)
  bbox.append(list(rt))
  return bbox

def draw_rectangle(canv,rect):
  
  bbox=find_dim(rect)
  canv.rectangle(bbox,fill=rect.colour,outline='yellow',width=3)

def draw_circle(canv,circle):
  
  center = list((circle.center.x,circle.center.y))
  canv.circle(center,circle.radius,fill=circle.colour,outline='black')

def draw_point(canv,pnt):
  cir = circle()
  cir.center = point()
  cir.center.x = pnt.x
  cir.center.y = pnt.y
  cir.radius = 1
  cir.colour = pnt.colour 
  draw_circle(canv,cir)

def draw_czech(canv,width,height):
  points=[[0,0],[0,height],[width/2.0,height/2.0]]
  canv.polygon(points,fill='blue')
  points=[[0,height],[width,height],[width,height/2.0],[width/2.0,height/2.0]]
  canv.polygon(points,fill='white')
  points=[[0,0],[width/2.0,height/2.0],[width,height/2.0],[width,0]]
  canv.polygon(points,fill='red')

def repeat():

  while True:
    choice = raw_input('draw what? r:rectangle c:circle p:point f:flag d:done --> ') 
    
    if choice in ('r','rectangle'): 
      
      box = create_rectangle()
      world = World()
      canvas = world.ca(width=500,height=500,background='black')
      draw_rectangle(canvas,box)  
      world.mainloop()
      continue

    if choice in ('c','circle'): 
      
      circle = create_circle()
      world = World()
      canvas = world.ca(width=500,height=500,background='black')
      draw_circle(canvas,circle)  
      world.mainloop()
      continue
    
    if choice in ('p','point'): 
      
      pnt = create_point()
      world = World()
      canvas = world.ca(width=500,height=500,background='black')
      draw_point(canvas,pnt)
      world.mainloop()
      continue

    if choice in ('f','flag'): 

      size = int(raw_input('enter the size of the flag:'))
      world = World()
      canvas = world.ca(width=500,height=500,background='black')
      draw_czech(canvas,3*size,2*size)
      world.mainloop()
      continue

    if choice in ('d','done'): 
      print "Bye!"
      break

    else:
      print 'unknown option!'
      
def main():
  repeat()

if __name__=='__main__':
  print '*'*30,'\n'
  main()
  print '\n','*'*30
