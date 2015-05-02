'''
exercise 17.8 For each named color possible in the system draw a sphere in the position
              that corresponds to its RGB values

'''
from color_list import *
from visual import *
  
def main():

  colors=read_colors()
  scene.range = (256,256,256)
  scene.center = (128,128,128)
  for c in colors.keys():
    pos = c
    color = c[0]/255.0,c[1]/255.0,c[2]/255.0 
    sphere(pos=pos,radius=10,color=color)

if __name__=='__main__':
  print '*'*30,'\n'
  main()
  print '\n','*'*30
