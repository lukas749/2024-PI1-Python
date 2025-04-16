import tkinter as tk
import random

class PexesoGame:
    def __init__(self,root):
        self.root = root
        self.root.title("Pexeso")
        self.grid_size = 4 #veľkosť pexesa
        self.card_values = list(range(1,(self.grid_size**2//2+1))) * 2
        random.shuffle(self.card_values)
        self.buttons = {}
        self.flipped = [] # otočené karty
        self.matches = 0

        self.create_grid()
    
    def create_grid(self):
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                button = tk.Button(self.root, text="?", width=10, height=3, command=lambda i=i, j=j: self.flip_card(i,j))
                button.grid(row=i, column=j)
                self.buttons[(i,j)] = {"button": button, "value": self.card_values.pop()}

    def flip_card(self, i, j):
        button = self.buttons[(i,j)]["button"]
        card_value = self.buttons[(i,j)]["value"]


        if button["text"] == "?" and len(self.flipped) < 2:
            button.config(text=str(card_value))
            self.flipped.append((i,j,card_value)) # kontrolovanie toho či su karty otočené

            if len(self.flipped) ==2:
                self.check_match() # ak sú otočené 2 karty ktoré sa nezhodujú toto ich zresetuje po kliknutí na dalšiu

        elif len(self.flipped) ==2:
            self.reset_flipped()
            self.flip_card(i,j)

    def check_match(self): 
    # ak sú karty zhodné
        if self.flipped[0][2] == self.flipped[1][2]:
            self.matches += 1
            if self.matches == (self.grid_size**2) //2:
                self.show_win_message()
            self.flipped = []
        else:
            # Ak sa karty nezhodújú skryjú sa
            self.root.after(1000, self.hide_cards)

    def hide_cards(self):
        # skryjeme čísla na kartách ktoré sa nezhodovali
        for (i,j,_) in self.flipped:
            self.buttons[(i,j)]["button"].config(text="?")
        # po skrytí kariet zresetujeme výber
        self.flipped = []

    def reset_flipped(self):
        # Ak sú otočené 2 karty ktoré sa nezhodujú, resetujeme ich po kliknutí na inú kartu
        for (i,j,_) in self.flipped:
            self.buttons[(i,j)]["button"].config(text="?")
    def show_win_message(self):
        win_message = tk.Label(self.root, text="Vyhral si!!", font=("Times New Roman", 24), fg="green")
        win_message.grid(row=self.grid_size, column=0, columnspan=self.grid_size)

if __name__ == "__main__":
    root = tk.Tk()
    game = PexesoGame(root)
    root.mainloop()