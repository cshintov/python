"""
exercise 19.4 Image viewer
#from Tkinter import PhotoImage
"""


from swampy.Gui import *
import Image as PIL
import ImageTk
import os
class View(object):
    
    def __init__(self):
        self.g = Gui()
        self.g.title('image_viewer')
        self.canvas = self.g.ca(height=500,width=500,bg='blue')
        self.canvas.bind('<Button-1>',self.view)
        self.msg = self.g.la()
        files = os.listdir('.')
        self.files=iter(files)
    
    def view(self,event):
        try:
            f = self.files.next()
        except:
            self.photo = None
            self.msg.config(text = 'No More Images!')
            print 'No more images!'
            return
        try:
            image = PIL.open(f)
        except IOError,message:
            self.photo = None
            self.msg.config(text = message)
            print message
            return
        self.photo = ImageTk.PhotoImage(image)
        self.canvas.image([0,0], image=self.photo)
        self.msg.config(text = f)
    
    def event_loop(self):
        self.g.mainloop()


if __name__=='__main__':
    view = View()
    view.event_loop()
