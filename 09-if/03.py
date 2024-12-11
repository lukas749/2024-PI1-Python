import tkinter
import random

pocet = int(input("Zadaj počet kruhov:"))
canvas_height = int(input("Zadaj výšku plátna:"))
canvas_width = int(input("Zadaj šírku plátna:"))
canvas = tkinter.Canvas(height = canvas_height, width = canvas_width)
canvas.pack()
for i in range(pocet):
    a =10
    x = random.randint(3,canvas_width-3-a)
    y =random.randint(3,canvas_height - 3 -a)
    if (x < canvas_width/2) and (y < canvas_height/2):
        farba = "blue"
    elif (x>canvas_width/2) and (y < canvas_height/2):
        farba = "yellow"
    if (x<canvas_width/2) and (y > canvas_width/2):
        farba = "red"
    elif (x>canvas_width/2) and (y>canvas_width/2):
        farba = "green"

    
    canvas.create_oval(x,y,x+a,y+a, fill= farba)

tkinter.mainloop()