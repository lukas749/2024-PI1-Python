import turtle
turtle.delay(0)

t = turtle.Turtle()
def obluk(d):
    for i in range(9):
        t.fd(d)
        t.rt(10)

def lupen(d):
    for i in 1, 2:
        obluk(d)
        t.rt(90)

def kvet(d):
    for i in range(12):
        lupen(d)
        t.rt(30)
kvet(50)
turtle.done()
