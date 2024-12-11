import tkinter

x = 100
y = 100
dlzka = 100

pocet = 5
canvas_height = int(input("Zadaj výšku plátna:"))
canvas_width = int(input("Zadaj šírku plátna:"))

canvas = tkinter.Canvas(width=canvas_width, height=canvas_height)
canvas.pack()


def dom(x, y, dlzka, farba):
    stvrtina = dlzka / 4
    #canvas.create_polygon(x0,y0,x1,y1,x2,y2) # vykresli mnohouholník v tomto prípade trojuholník, lebo prejde cez 3 body (x,y)
    canvas.create_polygon(x/2, y/3 + dlzka / 2, x/2 + dlzka / 2, y/3, x/2 + dlzka, y/3 + dlzka / 2, fill = "red")
    canvas.create_rectangle(x/2, y/3 + dlzka / 2, x/2 + dlzka, y/3 + dlzka / 2 + dlzka,fill = farba)
    canvas.create_rectangle(x/2 + stvrtina, y/3 + dlzka/2 + stvrtina, x/2 + stvrtina * 3, y/3 + dlzka/2 + stvrtina * 3, fill = "light blue")
    canvas.create_line(x/2 + stvrtina, y/3 + dlzka, x/2 + stvrtina * 3, y/3 + dlzka)
    canvas.create_line(x/2 + dlzka / 2, y/3 + dlzka / 2 + stvrtina, x/2 + dlzka / 2, y/3 + dlzka + dlzka/2 - stvrtina)
    
    
    
    
    #canvas.create_line(x + stvrtina, y + dlzka, x + stvrtina * 3, y + dlzka)
    #canvas.create_line(x + dlzka / 2, y + dlzka / 2 + stvrtina, x + dlzka / 2, y + dlzka + dlzka/2 - stvrtina) pomocou ciar urobene okno
    
    #canvas.create_rectangle(x + stvrtina, y + dlzka/2 + stvrtina, x + dlzka/2, y + dlzka)
    #canvas.create_rectangle(x + stvrtina, y + dlzka + stvrtina, x + dlzka/2, y + dlzka  )
    #canvas.create_rectangle(x + dlzka/2, y + dlzka/2 + stvrtina, x + stvrtina * 3, y + dlzka) pomocou stvorcou urobene okno

def ulica(x,y,dlzka,pocet):
    farba1, farba2 = "red","blue"
    for i in range (5):
        dom(x,y,dlzka,farba1)
        x = x + dlzka + 120
        farba1, farba2 = farba2, farba1

def stlpec(x,y,dlzka,pocet):
    farba1, farba2 = "red","blue"
    for i in range(5):
        ulica(x,y,dlzka,farba1)
        y = y + dlzka + 380

stlpec(0,0,dlzka,5)
ulica(0,0,dlzka,5)
canvas.mainloop()