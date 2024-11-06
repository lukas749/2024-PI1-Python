import tkinter

canvas = tkinter.Canvas() # vytvorenie plátna a jeho priradenie do premennej canvas
canvas.pack() # umiestenie plátna do okna

canvas.create_text(100, 75, text="Ahoj")
# vypíše text "Ahoj" na pozícii x=100 y=100
# súradnice zadávame vždy v poradí x,y
# x rastie smerom doprava
# y raste smerom dole

canvas.create_rectangle(50, 50, 150, 100)
# vykreslenie štvorca / obdlžníka
# prvé 2 čísla určujú pozíciu začiatočného bodu
# druhé 2 čísla určujú pozíciu koncového bodu

canvas.create_oval(50, 50, 150, 100)
# vykreslenie kruhu / oválu
# prvé 2 čísla určujú pozíciu začiatočného bodu
# druhé 2 čísla určujú pozíciu koncového bodu

tkinter.mainloop() # aby zostalo okno otvorené, aby sa nezavrelo