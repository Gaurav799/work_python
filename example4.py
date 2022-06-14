from turtle import *

t = Turtle()
t.speed('fast')
bgcolor('red')
t.color('blue')
t.pensize(14)
for i in range(1,201,3):
    t.fd(i)
    t.lt(60)

mainloop()