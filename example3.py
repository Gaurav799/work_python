from turtle import *

t= Turtle()
t.speed('fast')
s=getscreen()
for i in range(10):
    t.fd(100)
    t.lt(360//10)
    t.circle(100,190)

mainloop()