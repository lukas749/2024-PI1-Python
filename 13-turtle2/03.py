import turtle

def n_uholnik(n, d):
    for i in range(n):
        t.fd(d)
        t.lt(360 / n)
turtle.delay(0)
t = turtle.Turtle()
for n in range(3, 16):
    t.clear()
    n_uholnik(n, 50)
turtle.done()