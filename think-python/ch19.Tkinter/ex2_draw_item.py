'''exercise 19.2 Draw Items on the canvas'''
from swampy.Gui import *

def draw_circle():
    item = canvas.circle([0,0],100,fill='blue')
def draw_rectangle():
    item = canvas.rectangle([[0,0],[100,100]],fill='red')

g = Gui()
g.title( 'gui')
canvas = g.ca(width=500,height=500)
canvas.config(bg='white')
g.bu('Circle!',command=draw_circle)
g.bu('Rectangle!',command=draw_rectangle)
g.mainloop()
