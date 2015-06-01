from Tkinter import *
from swampy.TurtleWorld import *
from dow import get_text
class Browser(object):
    
    def __init__(self,master):
        self.master = master
        master.title('Browser')


        frame = Frame(self.master,width=300,height=300)
        frame.pack(expand=True,fill=BOTH)
        self.add = Entry(frame)
        self.add.pack(fill=X)
        self.gobu = Button(frame,text='Go',command=self.go)
        self.gobu.pack(fill = X)
        
        self.text = Text(frame,bg='#FFFFFF')
        
        hbar = Scrollbar(frame,orient=HORIZONTAL)
        hbar.pack(side = BOTTOM,fill = X)
        hbar.config(command = self.text.xview)
        vbar = Scrollbar(frame,orient = VERTICAL)
        vbar.pack(side = RIGHT,fill = Y)
        vbar.config(command = self.text.yview)
        self.text.config(xscrollcommand = hbar.set, yscrollcommand = vbar.set)
        self.text.pack(side = BOTTOM,expand=True,fill = BOTH)
        
        prev = Button(master,text = 'previous', command = self.previous)
        prev.pack(side = LEFT)
        
        next = Button(master,text = 'next', command = self.next)
        next.pack(side = LEFT)
        
        exit = Button(master,text = 'exit', command = self.quit)
        exit.pack(side = LEFT)
        
        save = Button(master,text = 'save', command = self.save)
        save.pack(side = LEFT)

    def previous(self):
        pass

    def next(self):
        pass

    def save(self):
        pass

    def quit(self):
        self.master.destroy()
    
    def go(self):
        url = self.add.get()
        visible_texts = get_text(url)
        self.text.delete(1.0,END)
        self.text.insert(END,visible_texts) 
        '''for text in visible_texts:
            #print text
            self.text.create_text(x, y, anchor=W, font="Purisa",
                           text=text) 
            y+=10'''
if __name__ == '__main__':
    root = Tk()
    browser = Browser(root)
    root.mainloop()
