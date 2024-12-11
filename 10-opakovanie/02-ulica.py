import tkinter
import random
x = 50
y = 50
dlzka = 100
pocet = 10


canvas_height = int(input("Zadaj výšku plátna:"))
canvas_width = int(input("Zadaj šírku plátna:"))

canvas = tkinter.Canvas(width=canvas_width, height=canvas_height)
canvas.pack()


def ulica (x, y, dlzka, pocet):
    farba1, farba2 = "red", "blue"
    
    stvrtina = dlzka / 4
    
    canvas.create_polygon(x , y + dlzka / 2, x + dlzka / 2 , y, x + dlzka , y + dlzka / 2, fill = "red")
    canvas.create_rectangle(x  , y + dlzka / 2, x + dlzka  , y + dlzka / 2 + dlzka,fill = farba2)
    canvas.create_rectangle(x + stvrtina, y + dlzka/2 + stvrtina, x + stvrtina * 3, y + dlzka/2 + stvrtina * 3, fill = "light blue")
    canvas.create_line(x + stvrtina, y + dlzka, x + stvrtina * 3, y + dlzka)
    canvas.create_line(x + dlzka / 2 , y + dlzka / 2 + stvrtina, x + dlzka / 2, y + dlzka + dlzka/2 - stvrtina)
    
    canvas.create_polygon(x + 150, y + dlzka / 2, x + dlzka / 2 + 150, y, x + dlzka + 150, y + dlzka / 2, fill = "red")
    canvas.create_rectangle(x + 150, y + dlzka / 2, x + dlzka + 150, y + dlzka / 2 + dlzka,fill = farba1)
    canvas.create_rectangle(x + stvrtina + 150, y + dlzka/2 + stvrtina, x + stvrtina * 3 + 150, y + dlzka/2 + stvrtina * 3, fill = "light blue")
    canvas.create_line(x + stvrtina + 150, y + dlzka, x + stvrtina * 3 + 150, y + dlzka)
    canvas.create_line(x + dlzka / 2 + 150, y + dlzka / 2 + stvrtina, x + dlzka / 2 + 150, y + dlzka + dlzka/2 - stvrtina)
    
    canvas.create_polygon(x + 300, y + dlzka / 2, x + dlzka / 2 + 300, y, x + dlzka + 300, y + dlzka / 2, fill = "red")
    canvas.create_rectangle(x + 300, y + dlzka / 2, x + dlzka + 300, y + dlzka / 2 + dlzka,fill = farba2)
    canvas.create_rectangle(x + stvrtina + 300, y + dlzka/2 + stvrtina, x + stvrtina * 3 + 300, y + dlzka/2 + stvrtina * 3, fill = "light blue")
    canvas.create_line(x + stvrtina + 300, y + dlzka, x + stvrtina * 3 + 300, y + dlzka)
    canvas.create_line(x + dlzka / 2 + 300, y + dlzka / 2 + stvrtina, x + dlzka / 2 + 300, y + dlzka + dlzka/2 - stvrtina)
    
    farba1, farba2 = farba2, farba1


def rad(x,y,dlzka,pocet):
    for i in range(pocet):
        ulica(x,y,dlzka,pocet)
        x += 150


def stlpec(x,y,dlzka,pocet):
    for i in range(pocet):
        rad(x, y, dlzka, pocet)
        y += 200

stlpec (x,y,dlzka,pocet)
rad(x, y, dlzka, pocet)
ulica(x, y, dlzka, pocet)

canvas.mainloop()