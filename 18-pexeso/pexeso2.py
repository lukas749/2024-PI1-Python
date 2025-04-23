import tkinter as tk
import random

okno = tk.Tk()
okno.title("Pexeso")
okno.geometry("500x500")

cisla = random.sample(range(1, 100), 4)
pary = cisla * 2
random.shuffle(pary)

otvorene = []

def klik(btn, cislo):
    if len(otvorene) >= 2 or btn["text"] != "?":
        return

    btn.config(text=str(cislo))
    otvorene.append((btn, cislo))

    if len(otvorene) == 2:
        btn1, val1 = otvorene[0]
        btn2, val2 = otvorene[1]
        if val1 != val2:
            okno.after(1000, lambda: skry(btn1, btn2))
        else:
            otvorene.clear()


def skry(btn1, btn2):
    btn1.config(text="?")
    btn2.config(text="?")
    otvorene.clear()


for i in range(8):
    riadok = i // 4
    stlpec = i % 4
    cislo = pary[i]
    tlacidlo = tk.Button(okno, text="?", width=12, height=3)
    tlacidlo.config(command=lambda btn=tlacidlo, c=cislo: klik(btn, c))
    tlacidlo.grid(row=riadok, column=stlpec, padx=10, pady=10)


okno.mainloop()