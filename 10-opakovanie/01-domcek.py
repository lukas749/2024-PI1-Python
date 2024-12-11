import tkinter

x = 100
y = 100
dlzka = 100
farba = "yellow"

canvas_height = int(input("Zadaj výšku plátna:"))
canvas_width = int(input("Zadaj šírku plátna:"))

canvas = tkinter.Canvas(width=canvas_width, height=canvas_height)
canvas.pack()


def dom(x, y, dlzka, farba):
    stvrtina = dlzka / 4
    #canvas.create_polygon(x0,y0,x1,y1,x2,y2) # vykresli mnohouholník v tomto prípade trojuholník, lebo prejde cez 3 body (x,y)
    canvas.create_polygon(x, y + dlzka / 2, x + dlzka / 2, y, x + dlzka, y + dlzka / 2, fill = "red")
    canvas.create_rectangle(x, y + dlzka / 2, x + dlzka, y + dlzka / 2 + dlzka,fill = farba)
    canvas.create_rectangle(x + stvrtina, y + dlzka/2 + stvrtina, x + stvrtina * 3, y + dlzka/2 + stvrtina * 3, fill = "light blue")
    canvas.create_line(x + stvrtina, y + dlzka, x + stvrtina * 3, y + dlzka)
    canvas.create_line(x + dlzka / 2, y + dlzka / 2 + stvrtina, x + dlzka / 2, y + dlzka + dlzka/2 - stvrtina)
    
    
    
    
    #canvas.create_line(x + stvrtina, y + dlzka, x + stvrtina * 3, y + dlzka)
    #canvas.create_line(x + dlzka / 2, y + dlzka / 2 + stvrtina, x + dlzka / 2, y + dlzka + dlzka/2 - stvrtina) pomocou ciar urobene okno
    
    #canvas.create_rectangle(x + stvrtina, y + dlzka/2 + stvrtina, x + dlzka/2, y + dlzka)
    #canvas.create_rectangle(x + stvrtina, y + dlzka + stvrtina, x + dlzka/2, y + dlzka  )
    #canvas.create_rectangle(x + dlzka/2, y + dlzka/2 + stvrtina, x + stvrtina * 3, y + dlzka) pomocou stvorcou urobene okno
dom(x, y, dlzka, farba)
canvas.mainloop()