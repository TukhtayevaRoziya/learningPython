from pydoc import doc
from turtle import begin_fill, bgcolor, color, done, end_fill, goto, pendown, penup, speed, width

speed(1)
bgcolor("black")
penup()
goto(-50, 60)
pendown()
color('blue')
begin_fill()
goto(100, 100)
goto(100, -100)
# Draw windows
goto(-50, -60)
goto(-50, 60)
end_fill()
color('black')
goto(15, 100)
# cut 2 equal parts
color('black')
width(10)
goto(15, -100)
penup()
goto(100, 0)
pendown()
goto(-100, 0)
color('black')

done()
