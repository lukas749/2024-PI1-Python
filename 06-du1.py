import tkinter

canvas = tkinter.Canvas(width=300, height=300)
canvas.pack()


canvas.create_rectangle(10, 20, 20, 10, fill="blue")
canvas.create_rectangle(10,30, 20, 20, fill="blue")
canvas.create_rectangle(10, 40, 20, 30, fill="blue")
canvas.create_rectangle(10, 50, 20, 40, fill="blue")
canvas.create_rectangle(10, 60, 20 ,50, fill="blue")
canvas.create_rectangle(10, 70, 20, 60, fill="blue")

canvas.create_rectangle(20, 70, 30 ,60, fill="blue")
canvas.create_rectangle(20 ,70, 40 ,60, fill="blue")

canvas.create_rectangle(50, 70 ,60 ,60, fill="blue")
canvas.create_rectangle(50, 60,60 ,50, fill="blue")
canvas.create_rectangle(50,50 ,60, 40, fill="blue")
canvas.create_rectangle(50, 40 ,60 ,30, fill="blue")
canvas.create_rectangle(50, 30 ,60 , 20, fill="blue")
canvas.create_rectangle(50, 20 ,60 ,10, fill="blue")

canvas.create_rectangle(60, 30 ,70 ,20, fill="blue")
canvas.create_rectangle(70 ,40 ,80, 30, fill="blue")
canvas.create_rectangle(80, 30 ,90 ,20, fill="blue")
canvas.create_rectangle(90, 30 ,100 ,20, fill="blue")
canvas.create_rectangle(90, 20 ,100, 10, fill="blue")
canvas.create_rectangle(90, 40 ,100, 30, fill="blue")
canvas.create_rectangle(90, 50 ,100, 40, fill="blue")
canvas.create_rectangle(90, 60 ,100, 50, fill="blue")
canvas.create_rectangle(90, 70, 100, 50, fill="blue")


canvas.mainloop()