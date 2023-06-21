from tkinter import *
import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk,Image



#create window
root1 = tk.Tk()
root1.geometry("500x500")
root1.title("Image Upload")
root1.config(bg="#38B6FF")

#choose file function and resized the image
def openFile():
    global image_used
    f_types = [('Jpg Files', '*.jpg'),('PNG Files','*.png')]
    image_used = filedialog.askopenfilename(filetypes=f_types)
    imgForpg2 = Image.open(image_used)
    imgForpg2_resized = imgForpg2.resize((400, 400), Image.ANTIALIAS)
    imgForpg2 = ImageTk.PhotoImage(imgForpg2_resized)
    my_label = tk.Label(root1)
    my_label.grid(row=3,column=2)
    my_label.image = imgForpg2
    my_label['image'] = imgForpg2
    fh = open('fileAddress.txt','w')
    fh.write(image_used)
    fh.close()
    label = tk.Label(root1, text="Your image will be displayed below", bg="#38B6FF", borderwidth=4)
    label.grid(row=1, column=2)
    Button4Drones = tk.Button(root1, text="4 Drones", command=FDronePage).place(x=305,y=450)

    Button2Drones = tk.Button(root1, text="2 Drones", command=TDronePage).place(x=385,y=450)


#if want four drones then do this function
def FDronePage():
    root1.destroy()
    import FourDronesSplitPage
#if want two drones then do this function
def TDronePage():
    root1.destroy()
    import TwoDroneSplitPage


#upload button image
btu = Image.open("upload.png")
resized_image_up = btu.resize((30, 30), Image.ANTIALIAS)
new_image_upload = ImageTk.PhotoImage(resized_image_up)

global label
#using grid from tkinter,pack() sometimes not show image
labelButton = tk.Button(root1,image=new_image_upload,command=lambda:openFile(),borderwidth=2,bg="#289DD2",border=3)
labelButton.grid(row=1,column=1)
label = tk.Label(root1,text="Please Upload File",bg="#38B6FF",borderwidth=4)
label.grid(row=1,column=2)





root1.mainloop()











