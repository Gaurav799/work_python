from turtle import *

t= Turtle()
t.speed('slow')
s=getscreen()
for i in range(4):
    t.fd(100)
    t.lt(360//4)
    t.circle(100,100)

mainloop()