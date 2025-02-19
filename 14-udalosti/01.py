import tkinter
import random

def vypis():
    text = 'PYTHON'
    x = random.randrange(50, 330)
    y = random.randrange(20, 240)
    canvas.create_text(x, y, text=text, font='arial 20')

def zmaz():
    canvas.delete('all')

canvas = tkinter.Canvas()
canvas.pack()
tkinter.Button(text='Vypíš text', command=vypis).pack()
tkinter.Button(text='Zmaž plochu', command=zmaz).pack()

vstup = tkinter.Entry(width=10)
vstup.pack()

tkinter.mainloop()