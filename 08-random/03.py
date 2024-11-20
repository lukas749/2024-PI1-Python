import tkinter
import random


pocet = int(input("Zadaj koľko chceš mať jednotiek:"))

canvas = tkinter.Canvas(width=500, height=400)
canvas.pack()

x = 10
y = 10

def jednotka(x,y):
    x = random.randint(3, 500-33)
    y = random.randint(3, 400-73)
    
    canvas.create_rectangle(x,y+10,x+10,y+20,fill =random.choice(["blue","red","yellow","green"]),outline=random.choice(["yellow","black","red","green","brown"]))
    canvas.create_rectangle(x+10,y+20,x+20,y,fill =random.choice(["blue","red","yellow","green"]),outline=random.choice(["yellow","black","red","green","brown"]))
    canvas.create_rectangle(x+10,y+10,x+20,y,fill =random.choice(["blue","red","yellow","green"]),outline=random.choice(["yellow","black","red","green","brown"]))
    canvas.create_rectangle(x+10,y+20,x+20,y+30,fill =random.choice(["blue","red","yellow","green"]),outline=random.choice(["yellow","black","red","green","brown"]))
    canvas.create_rectangle(x+10,y+30,x+20,y+40,fill =random.choice(["blue","red","yellow","green"]),outline=random.choice(["yellow","black","red","green","brown"]))
    canvas.create_rectangle(x+10,y+40,x+20,y+50,fill =random.choice(["blue","red","yellow","green"]),outline=random.choice(["yellow","black","red","green","brown"]))
    canvas.create_rectangle(x+10,y+50,x+20,y+60,fill =random.choice(["blue","red","yellow","green"]),outline=random.choice(["yellow","black","red","green","brown"]))
    canvas.create_rectangle(x+10,y+60,x+20,y+70,fill =random.choice(["blue","red","yellow","green"]),outline=random.choice(["yellow","black","red","green","brown"]))
    canvas.create_rectangle(x+20,y+60,x+30,y+70,fill =random.choice(["blue","red","yellow","green"]),outline=random.choice(["yellow","black","red","green","brown"]))
    canvas.create_rectangle(x,y+60,x+10,y+70,fill =random.choice(["blue","red","yellow","green"]),outline=random.choice(["yellow","black","red","green","brown"]))

for i in range(pocet):
    jednotka(x,y)



canvas.mainloop()