"""
exercise 19.4.4 Image Processor
"""

from swampy.Gui import *
import Image as PIL
import ImageTk
import os
class View(object):

    files = os.listdir('.')
    files=iter(files)
    
    def __init__(self):
        self.g = Gui()
        self.g.title('image_processor')
        self.msg = self.g.la()
        self.g.row([1,0])
        self.canvas = self.g.ca(height=500,width=500,bg='blue')
        self.canvas.bind('<Button-1>',self.view)
        self.g.col()
        self.saveas = self.g.en()
        self.g.bu('convert',command=self.convert)
        
        self.g.la(text='Zoom')
        sizes=['1x','2x','3x']
        mb = self.g.mb(text=sizes[0])

        def setsize(size):
            mb.config(text=size)
            self.msg.config(text='zoomed to '+size)
            self.zoom(size)

        for size in sizes:
            self.g.mi(mb,text=size,command=Callable(setsize,size))
        
        self.g.la(text='Rotate')
        angles=['90','180','270',]
        mb = self.g.mb(text=angles[0])

        def setangle(angle):
            mb.config(text=angle)
            self.msg.config(text='rotated '+angle+' degree!')
            self.rotate(angle)

        for angle in angles:
            self.g.mi(mb,text=angle,command=Callable(setangle,angle))
    
    def rotate(self,angle):
        if angle == '90': angle = 90
        elif angle == '180': angle = 180
        elif angle == '270' : angle = 270

        self.newi = self.image.rotate(angle)
        self.photo = ImageTk.PhotoImage(self.newi)
        self.canvas.image([400,-20], image=self.photo)

    def zoom(self,size):
        if size == '1x': ztup = (128,128)
        elif size == '2x': ztup = (256,256)
        elif size == '3x' : ztup = (512,512)

        self.newi = self.image.resize(ztup)
        self.photo = ImageTk.PhotoImage(self.newi)
        self.canvas.image([400,-20], image=self.photo)

    def view(self,event):
        try:
            self.f = self.files.next()
        except:
            self.photo = None
            self.msg.config(text = 'No More Images!')
            print 'No more images!'
            return
        try:
            self.image = PIL.open(self.f)
        except IOError,message:
            self.photo = None
            self.msg.config(text = message)
            print message
            return
        self.photo = ImageTk.PhotoImage(self.image)
        self.canvas.image([400,-20], image=self.photo)
        self.msg.config(text = self.f)
    
    def convert(self):
        outfile = self.saveas.get()
        of,oe = os.path.splitext(outfile)
        inf,ine = os.path.splitext(self.f)
        if oe == ine:
            self.msg.config(text='same format!')
        else:
            try:
                self.image.save(outfile)
                new = PIL.open(outfile)
                new.show()
            except IOError:
                self.msg.config(text='Unknown Image Format!')

    def event_loop(self):
        self.g.mainloop()


if __name__=='__main__':
    view = View()
    view.event_loop()
