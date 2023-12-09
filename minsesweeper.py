from tkinter import*
from tkinter import ttk
import random
import tkinter as tk

grid_coordinates = {
    '(1, 1)': 1, '(1, 2)': 2, '(1, 3)': 3, '(1, 4)': 4, '(1, 5)': 5, '(1, 6)': 6, '(1, 7)': 7, '(1, 8)': 8, '(1, 9)': 9, '(1, 10)': 10, 
    '(2, 1)': 11, '(2, 2)': 12, '(2, 3)': 13, '(2, 4)': 14, '(2, 5)': 15, '(2, 6)': 16, '(2, 7)': 17, '(2, 8)': 18, '(2, 9)': 19, '(2, 10)': 20, 
    '(3, 1)': 21, '(3, 2)': 22, '(3, 3)': 23, '(3, 4)': 24, '(3, 5)': 25, '(3, 6)': 26, '(3, 7)': 27, '(3, 8)': 28, '(3, 9)': 29, '(3, 10)': 30,
    '(4, 1)': 31, '(4, 2)': 32, '(4, 3)': 33, '(4, 4)': 34, '(4, 5)': 35, '(4, 6)': 36, '(4, 7)': 37, '(4, 8)': 38, '(4, 9)': 39, '(4, 10)': 40, 
    '(5, 1)': 41, '(5, 2)': 42, '(5, 3)': 43, '(5, 4)': 44, '(5, 5)': 45, '(5, 6)': 46, '(5, 7)': 47, '(5, 8)': 48, '(5, 9)': 49, '(5, 10)': 50, 
    '(6, 1)': 51, '(6, 2)': 52, '(6, 3)': 53, '(6, 4)': 54, '(6, 5)': 55, '(6, 6)': 56, '(6, 7)': 57, '(6, 8)': 58, '(6, 9)': 59, '(6, 10)': 60, 
    '(7, 1)': 61, '(7, 2)': 62, '(7, 3)': 63, '(7, 4)': 64, '(7, 5)': 65, '(7, 6)': 66, '(7, 7)': 67, '(7, 8)': 68, '(7, 9)': 69, '(7, 10)': 70, 
    '(8, 1)': 71, '(8, 2)': 72, '(8, 3)': 73, '(8, 4)': 74, '(8, 5)': 75, '(8, 6)': 76, '(8, 7)': 77, '(8, 8)': 78, '(8, 9)': 79, '(8, 10)': 80, 
    '(9, 1)': 81, '(9, 2)': 82, '(9, 3)': 83, '(9, 4)': 84, '(9, 5)': 85, '(9, 6)': 86, '(9, 7)': 87, '(9, 8)': 88, '(9, 9)': 89, '(9, 10)': 90, 
    '(10, 1)': 91, '(10, 2)': 92, '(10, 3)': 93, '(10, 4)': 94, '(10, 5)': 95, '(10, 6)': 96, '(10, 7)': 97, '(10, 8)': 98, '(10, 9)': 99, '(10, 10)': 100
}

click_coordinate = []
bomb_coordinates = []
bombs_location = []
buttons = []

bomb_row = [random.randint(1, 10) for n in range(12)]
bomb_col = [random.randint(1, 10) for n in range(12)]

bomb_coordinates = [(item1, item2) for item1, item2 in zip(bomb_row, bomb_col)]

for coordinate in bomb_coordinates:
    bombs_location.append(grid_coordinates[f"{coordinate}"])


def create_board():
    window = Tk()
    window.title("Minesweeper")
    window.geometry("570x520")
    window.config(background="#222e40")

    frame = Frame(window)
    frame.pack()

    for row in range(1, 11):
        button_row = []
        for col in range(1, 11):
            button = Button(frame,
                            fg= "black",
                            bg= "grey",
                            text= " ",
                            height= 2, 
                            width= 5, 
                            font= 10, 
                            command=lambda r=row, c=col: button_click(r, c), 
                            activebackground= "grey",
                            activeforeground= "grey"
                            )
            button.grid(row=row, column=col, padx=1, pady=1)
            button_row.append(button)
        buttons.append(button_row)

    window.mainloop()

def minesweeper_break():
    pass

def button_click(row, col):
    print(f"Button clicked at ({col}, {row})")
    click_coordinate.append((col, row))

    def check_for_bomb():
        if click_coordinate[-1] in bomb_coordinates:
            buttons[row-1][col-1].config(bg = "red", fg = "white")
            #print("youve stepped on a bomb")
        else:
            buttons[row-1][col-1].config(bg = "blue", fg = "white")
            #print("There isnt a bomb here")
        for coordinate in bomb_coordinates:
            bombs_location.append(grid_coordinates[f"{coordinate}"])

    def proximity():
        y = str(click_coordinate[-1])
        x = grid_coordinates[y]
        
        proxlist = [x-11, x-10, x-9, x-1, x+1, x+9, x+10, x+11]
        
        bombs_in_proximity = 0

        for i in bombs_location and proxlist:
            if i in bombs_location and proxlist:
                bombs_in_proximity += 1

        z = bombs_in_proximity

        if bombs_in_proximity == z:
            buttons[row-1][col-1].config(text = f"{z}")
            print(f"bombs in proximity: {z}")
            z = 0
            
    check_for_bomb()
    proximity()
     
create_board()
    
