import turtle

t = turtle.Turtle()
t.lt(30)
for i in range(2, 200, 4):
    t.fd(i)
    t.rt(90)
turtle.done()