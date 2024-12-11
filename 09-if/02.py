import tkinter
import random
pocet = int(input("Zadaj počet kruhov:"))
canvas_height = int(input("Zadaj výšku"))
canvas_width = int(input("zadaj šírku"))

canvas = tkinter.Canvas(height = canvas_height , width = canvas_width)
canvas.pack()




for i in range (pocet):
    a = 10
    x = random.randint(3, canvas_width -3 - a)
    y = random.randint( 3, canvas_height -3 - a)
#    if (x < canvas_width /2) and (y < canvas_height /2): # zlozena podmienka (testujeme viac vlastnosti)
        # medzi zlozene podmienky vkladame logicke operatory ( and = a zaroven, or = alebo)
#        farba = "yellow"
#    elif (x > canvas_width /2) and (y> canvas_height/2):
#        farba = "blue"
#    elif (x> canvas_width/2) and (y < canvas_height/2):
#        farba = "red"
#    elif (x< canvas_width/2) and (y> canvas_height/2):
#        farba = "green"

    if x < canvas_width /2:
        if y< canvas_height/2:
            farba="blue"
        else:
            farba= "green"
    else:
        if x > canvas_width /2:
            farba = "red"
        else:
            farba="yellow"
        canvas.create_oval(x,y,x+a,y+a, fill=farba)


canvas.mainloop()