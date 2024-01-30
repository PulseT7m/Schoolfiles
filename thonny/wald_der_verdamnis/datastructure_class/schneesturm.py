from p5 import *
from random import *
class Schneeflocke():
    def __init__(self):
        self.x_pos=randint(0,w)
        self.y_pos=randint(0,400)
        self.r=randint(1,10)
        self.farbe=randint(0,255)
        self.speed=randint(0,10)
    def fallen(self):
        if self.y_pos<500:
            self.y_pos+=2
            #self.x_pos+=1
            #self.r=randint(1,200)
        else:
            self.y_pos=0
            #self.x_pos=randint(0,w)
    def zeichnen(self):
        circle(self.x_pos,self.y_pos,self.r)
w=500
flocken=[]
def setup():
    global w
    size(w,400)
    for i in range(100):
        flocken.append("s"+str(i))
        flocken[i]=Schneeflocke()
def draw():
    background(0,255,0)
    for _ in flocken:
        _.zeichnen()
        _.fallen()
run()