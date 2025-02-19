import turtle

def obluk(d):
    for i in range(9):
        t.fd(d)
        t.rt(10)

def lupen(d):
    for i in 1, 2:
        obluk(d)
        t.rt(90)

def kvet(n, d):
    for i in range(n):
        lupen(d)
        t.rt(360 / n)

turtle.delay(0)
t = turtle.Turtle()
kvet(10, 20)
turtle.done()