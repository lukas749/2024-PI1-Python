import tkinter
import random
canvas = tkinter.Canvas(width=800, height=800)
canvas.pack()


x1 = random.randint(3, 797)
y1 = random.randint(3, 797)
x2 = random.randint(3, 797)
y2 = random.randint(3, 797)

R = f"#{random.randint(0,255):02x}"
G = f"#{random.randint(0,255):02x}"
B = f"#{random.randint(0,255):02x}"

O = canvas.create_oval(x1,y1,x2,y2)
R = canvas.create_rectangle(x1,y1,x2,y2)
L = canvas.create_line(x1,y1,x2,y2)

tvar = random.choice(["O", "R", "L"])


subor = open("tvary.txt", "w")
print(tvar, x1, y1, x2, y2, R, G, B, file=subor)




print(tvar, x1, y1, x2, y2, R, G, B)

subor.close()