import tkinter as tk
import random

root = tk.Tk()
root.geometry("200x200")

cisloPC = random.randint(0,9)
pokus = 0 
def akciaTlacidla():
    global pokus
    MojeCislo = int(textbox.get())
    if MojeCislo < cisloPC:
        label.config(text = "Dal si menšie číslo")
        pokus = pokus+1
    elif MojeCislo > cisloPC:
        label.config(text = "Dal si väčšie číslo")
        pokus = pokus+1
    else:
        label.config(text = "Uhádol si")
        pokus = pokus+1

label = tk.Label (root, text = "CisloPC")
label.pack()

textbox = tk.Entry(root)
textbox.pack()

button = tk.Button(root, text = "Hádaj",command = akciaTlacidla)
button.pack()

root.mainloop()
print (f"Počet tvojich pokusov bol:{pokus}")