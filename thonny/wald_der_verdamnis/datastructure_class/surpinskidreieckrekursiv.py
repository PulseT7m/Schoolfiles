from turtle import *
def dreieck(lan,tiefe):
    if tiefe==0:
        return
    else:
        for i in range(0,3):
            forward(lan)
            right(120)
            dreieck(lan/2,tiefe-1)
speed(10000)
dreieck(500,7)