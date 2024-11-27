import tkinter
import random
canvas_width = int(input("Zadaj šírku plátna:"))
canvas_height = int(input("Zadaj výšku plátna:")) # zadame vysku a sirku platna

pocet = int(input("zadaj počet štvorcov:"))
canvas = tkinter.Canvas(height = canvas_height, width = canvas_width)

canvas.pack()

for i in range(pocet):
    a = random.randint(1,30) # velkost stvorca
    x = random.randint(3,canvas_width - 3-a)
    y = random.randint(3, canvas_height - 3-a) # polohy stvorca
    

    if a< 10:
        farba = "red"
    elif a <= 20:
        farba = "green"
    else :
        farba="blue"
    canvas.create_rectangle(x , y, x+a,y+a,fill = farba, width = 0)










canvas.mainloop()