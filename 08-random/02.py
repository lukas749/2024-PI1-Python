import tkinter
import random

dlzka = int(input("Zadaj dĺžku hrany štvorca:"))
pocet = int(input("Zadaj počet štvorcov:"))
canvas = tkinter.Canvas(width=500, height=400)
canvas.pack()


for i in range(pocet):
    nahodne_x = random.randint(3,500-dlzka-3)
    nahodne_y = random.randint(3,400-dlzka-3)
    canvas.create_rectangle(nahodne_x,nahodne_y,nahodne_x+dlzka, nahodne_y+dlzka,fill =random.choice (["red", "green", "blue", "yellow"]))




canvas.mainloop()