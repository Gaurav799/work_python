from turtle import *

s=Screen()
s.setup(1000,700)
colors=['blue','pink']
pencolor('black')
pensize(7)
speed('fastest')
for i in range(15,0,-1):
    penup()
    setpos(0,-20*i)
    pendown()
    fillcolor(colors[i%2])
    begin_fill()
    circle(20*i)
    end_fill()
mainloop()