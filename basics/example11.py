from turtle import*
import random
s=Screen()
s.setup(500,500)
colors=['blue','red']
speed('fastest')
for i in range(30):
    x=random.randint(-200,200)
    y=random.randint(-200,200)
    penup()
    goto(x,y)
    pendown()
    pensize(random.randint(1,2))
    pencolor(colors[random.randint(0,1)])
    radius=random.randint(15,30)
    fillcolor('yellow')
    begin_fill()
    for i in range(9):
        circle(radius)
        left(40)
    end_fill()
mainloop()