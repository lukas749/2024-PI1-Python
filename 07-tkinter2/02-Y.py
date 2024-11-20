import tkinter

canvas = tkinter.Canvas(width=600, height=600)
canvas.pack()

def yčko(x,y):
    canvas.create_rectangle(x,y,x+10,y+10,fill="yellow")
    canvas.create_rectangle(x,y+10,x+10,y+20,fill="yellow")
    canvas.create_rectangle(x+10,y+20,x+20,y+30,fill="yellow")
    canvas.create_rectangle(x+30,y+20,x+40,y+30,fill="yellow")
    canvas.create_rectangle(x+40,y,x+50,y+10,fill="yellow")
    canvas.create_rectangle(x+40,y+10,x+50,y+20,fill="yellow")
    canvas.create_rectangle(x+20,y+30,x+30,y+40,fill="yellow")
    canvas.create_rectangle(x+20,y+40,x+30,y+50,fill="yellow")
    canvas.create_rectangle(x+20,y+50,x+30,y+60,fill="yellow")
    canvas.create_rectangle(x+20,y+60,x+30,y+70,fill="yellow")
x=10
y=10
def riadok_x(x,y,pocet):
    for i in range (pocet):
        yčko(x,y)
        x +=60

def riadky_x(x,y,pocet_riadkov,pocet_stlpcov):
    for i in range(pocet_riadkov):
        riadok_x(x,y,pocet_stlpcov)
        y +=80

yčko(10,10)
riadok_x(10,100,3)
riadky_x(10,180,3,5)



canvas.mainloop()