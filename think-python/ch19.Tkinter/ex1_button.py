'''exercise 19.1 execute command through the button press'''
from swampy.Gui import *

def make_button():
    g.bu('Now Press Me!',command=make_label)
def make_label():
    g.la('Nice Job!')

g = Gui()
g.title( 'gui')
button = g.bu('Press Me!',command=make_button)
g.mainloop()
