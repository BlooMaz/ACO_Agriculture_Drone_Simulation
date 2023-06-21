import cv2
from tkinter import *
import tkinter as tk
from PIL import ImageTk,Image
from split_image import split_image
import os


window = tk.Tk()
window.geometry("1100x450")
window.title("Four Drones")

def readAndimage():
    global filename
    fh = open('fileAddress.txt', 'r')
    filename = fh.readline()
    fh.close()

    file_split = r'\Users\muhdm\PycharmProjects\pythonProject1\image_split'
    if not os.path.exists(file_split):
        os.makedirs(file_split)
    else:
        os.remove(file_split)
        os.makedirs(file_split)

    split_image(filename, 1, 2, False, False,False,file_split)
    col = 1  # start from column 1
    row = 3  # start from row 3
    #make loop to get image from image_split
    #double loop for grid 2x2

    f_types = [('Jpg Files', '*.jpg'),
               ('PNG Files', '*.png')]  # type of files to select
    file_dir = tk.filedialog.askopenfilename(initialdir=file_split,multiple=True, filetypes=f_types)
    col = 1  # start from column 1
    row = 1  # start from row 3

    col_button = 2
    row_button = 1
    for images in file_dir:

        img = Image.open(images)
        img = img.resize((400,400))
        img = ImageTk.PhotoImage(img)

        e1 = tk.Label(window)
        labelbutton = tk.Button(window,text = "Go to this section <-")
        e1.grid(row=row, column=col)

        e1.image = img  # keep a reference! by attaching it to a widget attribute
        e1['image'] = img  # Show Image
        labelbutton.grid(row=row_button, column=col_button)
        if (col == 1 and row == 1):
            col = 3
            col_button = 4





readAndimage()

window.mainloop()
