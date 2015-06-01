from swampy.Gui import *
class App(object):
    def draw_circle(self):
        color = self.entry.get()
        try:
            self.item = self.canvas.circle([0,0],100,fill=color)
        except:
            print 'invalid color!'

    def change_color(self):
        color = self.entry.get()
        
        try:
            self.item.config(fill = color)
        except AttributeError:
            print 'There is No circle'
        except :
            print 'invalid color!'

    def draw(self):
        g = Gui()
        g.title( 'gui')
        self.canvas = g.ca(width=500,height=500)
        self.canvas.config(bg='white')
        self.entry = g.en(text='color')
        g.bu(text='Circle',command = self.draw_circle)
        g.bu('change color',command = self.change_color)
        g.mainloop()

if __name__=='__main__':
    app = App()
    app.draw()
