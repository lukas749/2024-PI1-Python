import tkinter
import random

def kresli():
    while True:
        x = random.randint(10, 370)
        y = random.randint(10, 250)
        canvas.create_oval(x - 10, y - 10, x + 10, y + 10, fill='red')
        canvas.update()
        canvas.after(100)

canvas = tkinter.Canvas()
canvas.pack()

kresli()
print('hotovo')

tkinter.mainloop()