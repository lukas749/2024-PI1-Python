import turtle



t = turtle.Turtle()
pocet = 1
dlzka = 100
turtle.delay(0)
t.speed(0)

def dom(pocet, dlzka):
    t.lt(90)
    t.fillcolor("yellow")
    t.begin_fill()
    t.fd(100)
    t.rt(90)
    t.fd(140)
    t.rt(90)
    t.fd(100)
    t.rt(90)
    t.fd(140)
    t.end_fill()
    t.rt(90)
    t.fd(100)
    t.fillcolor("red")
    t.begin_fill()
    t.rt(45)
    t.fd(100)
    t.rt(90)
    t.fd(100)
    t.rt(45)
    t.end_fill()
    t.penup()
    t.fd(75)
    t.rt(90)
    t.penup()
    t.fd(45)
    t.pendown()
    t.fillcolor("light blue")
    t.begin_fill()
    t.fd(50)
    t.rt(90)
    t.fd(50)
    t.rt(90)
    t.fd(50)
    t.rt(90)
    t.fd(50)
    t.rt(90)
    t.end_fill()
    t.fd(25)
    t.rt(90)
    t.fd(50)
    t.rt(90)
    t.fd(25)
    t.rt(90)
    t.fd(25)
    t.rt(90)
    t.fd(50)
    t.rt(180)
    
    

def ulica (pocet):
    for i in range(5):
        dom(pocet, dlzka)
        t.penup()
        t.fd(95)
        t.lt(90)
        t.fd(50)
        t.rt(90)
        t.fd(30)
        t.rt(90)
        t.fd(100)
        t.lt(90)
        t.pendown()
def dedina (pocet):
    for i in range(3):
        ulica(1)
        t.penup()
        t.rt(90)
        t.fd(200)
        t.rt(90)
        t.fd(855)
        t.rt(180)
        t.pendown


t.rt(180)
t.penup()
t.fd(400)
t.rt(90)
t.fd(200)
t.rt(90)
t.pendown()

dedina(pocet)


turtle.done()