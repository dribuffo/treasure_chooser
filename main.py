import tkinter as tk
import random
import time

#global variables
HEIGHT = 349
WIDTH = 680


root = tk.Tk()
root.title("FFXI AMAN Trove Treasure Chooser")

#create canvas
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

#set background image
background_image = tk.PhotoImage(file='background.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

#load in treasure chests
#randomly assign numbers over the treasure chests
#add click events, L => Good, R => Bad
#reset button

#run commands
root.mainloop()
