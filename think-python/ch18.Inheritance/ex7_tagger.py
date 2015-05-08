'''exercise 18.7 Make the turtles Play tag'''
from math import *
from Wobbler import *
from random import *

class Tagger(Wobbler):
    '''plays tag'''

    def __init__(self, world, speed=1, clumsiness=60, color='red'):
        Wobbler.__init__(self, world)
        self.delay = 0
        self.speed = speed
        self.clumsiness = clumsiness
        self.color = color
        self.it = False
        self.stall = 0
        # move to the starting position
        self.pu() 
        self.rt(randint(0,360))
        self.bk(150)

    def steer(self):
        #forces the taggers to be always in the boundary of the playground
        if self.outofbounds():
            self.turn()
        #just before being the it , the tagger stalls for some time
        if self.stall>0:
            self.stall -= 1
            if self.stall == 0:
                self.be_it()
            return
        #if the tagger is currently 'it', chase the nearest neighbour an try to tag it
        if self.it:
            self.turn_to_nearest()
            self.tag_it()
        elif not self.outofbounds():
            self.turn_away_from_it()

    def turn_to_nearest(self):
        nibor = self.nearest()
        self.turn(nibor.x,nibor.y)
    
    def turn_away_from_it(self):
        nibor = self.nearest()
        if nibor.it and self.distance(nibor)<15:
            self.turn(nibor.x,nibor.y,away = True)

    #finds the nearest neighbour         
    def nearest(self):
        others = [animal for animal in self.world.animals if animal is not self]
        nibor = others[0]
        for other in others[1:]:
            if self.distance(other) < self.distance(nibor):
                nibor = other
        return nibor
    
    def distance(self,other):
        sqx = self.x - other.x
        sqy = self.y - other.y
        return sqrt( sqx**2 + sqy**2 )

    #turns away or towards depending on the away parameter,towards by default
    def turn(self,x=0,y=0,away = False):
        dx = x - self.x
        dy = y - self.y
        theta = degrees(atan2(dy,dx))
        if away:
            theta = -theta
        self.heading = theta
        self.redraw()

    #return True if the turtle is out of the playground
    def outofbounds(self):
        if abs(self.x) >= 200 or abs(self.y)>=200:
            return True
        return False
    
    #setup the stalling process before making the turtle 'it'
    def make_it(self):
        self.oldcolor = self.color
        self.oldspeed = self.speed
        self.speed = 0
        self.color = 'blue'
        self.redraw()
        self.stall = 200
    
    #invoked from steer after the stalling period
    def be_it(self):
        self.it = True
        self.color = 'red'
        self.speed = self.oldspeed
        self.redraw()
    
    def unmake_it(self):
        self.it = False
        self.color = self.oldcolor
        self.redraw()
    
    def tag_it(self):
        nibor = self.nearest()
        if self.it and self.distance(nibor)<10:
            nibor.make_it()
            self.unmake_it()

#chooses the initial 'it'
def choose_it(world):
    it = choice(world.animals)
    it.make_it()

if __name__ == '__main__':
    world = make_world(Tagger)
    choose_it(world)
    world.mainloop()
