import tkinter as tk
from PIL import Image, ImageTk
import random
import time

#global variables
# dsply = False

#Functions

#randomly assign numbers over the treasure chests
# def display(dsply):

#reset function: resets the numbers that display on top of the treasure chests
# def reset():
#     global dsply
#     dsply = True
#     display(dsply)


#creates frame and titles app
root = tk.Tk()
root.title("FFXI AMAN Trove Treasure Chooser")
root.geometry("680x339")

#create canvas to work on
canvas = tk.Canvas(root, height=339, width=680)


#loads background image and places it on the canvas
background_image = tk.PhotoImage(file='background.png')
background_label = tk.Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

#load in treasure chests
#normal
normal_treasure = Image.open("normal_treasure.png")
normal_treasure = normal_treasure.resize((112, 86), Image.ANTIALIAS)
normal_treasure = ImageTk.PhotoImage(normal_treasure)
#good
good_treasure = Image.open("good_treasure.png")
good_treasure = good_treasure.resize((112, 86), Image.ANTIALIAS)
good_treasure = ImageTk.PhotoImage(good_treasure)
#bad
bad_treasure = Image.open("bad_treasure.png")
bad_treasure = bad_treasure.resize((112, 86), Image.ANTIALIAS)
bad_treasure = ImageTk.PhotoImage(bad_treasure)

#places treasures on the canvas
#top row
treasure_one = tk.Label(root, image=normal_treasure, bg="black").place(x=20, y=50)
treasure_two = tk.Label(root, image=normal_treasure, bg="black").place(x=150, y=50)
treasure_three = tk.Label(root, image=normal_treasure, bg="black").place(x=280, y=50)
treasure_four = tk.Label(root, image=normal_treasure, bg="black").place(x=410, y=50)
treasure_five = tk.Label(root, image=normal_treasure, bg="black").place(x=540, y=50)
#bottom row
treasure_six = tk.Label(root, image=normal_treasure, bg="black").place(x=20, y=220)
treasure_seven = tk.Label(root, image=normal_treasure, bg="black").place(x=150, y=220)
treasure_eight = tk.Label(root, image=normal_treasure, bg="black").place(x=280, y=220)
treasure_nine = tk.Label(root, image=normal_treasure, bg="black").place(x=410, y=220)
treasure_ten = tk.Label(root, image=normal_treasure, bg="black").place(x=540, y=220)

#add click events, L => Good, R => Bad

#reset button: adds reset button to frame
# button1 = tk.Button(root, text="Reset", command=reset)
button1 = tk.Button(root, text="Reset")
button1.place(relx=0, rely=0, relwidth=1, relheight=0.1)

#run commands
root.mainloop()
