from turtle import*

pencolor('red')
pensize(5)
fillcolor('pink')
speed('fastest')
goto(-100,-100)
for i in range(20,0,-3):
    begin_fill()
    circle(i*10)
    rt(30)
    end_fill()
goto(140,140)
mainloop()