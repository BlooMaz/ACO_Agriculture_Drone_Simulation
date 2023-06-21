from tkinter import *
from tkinter import filedialog

from PIL import Image, ImageTk


def subOpenPage1():
    #go to next page which is choose the file image
    window.destroy()
    import pageAfter


#test image
fileimg1 = "paddy.jpg"

window = Tk()
#size of window
window.geometry("500x500")
window.title("HomePage")




bg = PhotoImage(file="homepage background.png")
#login button image
bts = Image.open("start_button_home.png")
resized_image1 = bts.resize((100, 50), Image.ANTIALIAS)
new_image1 = ImageTk.PhotoImage(resized_image1)


#login button image
bts_exit = Image.open("logout.png")
resized_image1_exit = bts_exit.resize((50, 50), Image.ANTIALIAS)
new_image1_exit= ImageTk.PhotoImage(resized_image1_exit)

# Create Canvas
canvas1 = Canvas(window, width=500,
                     height=500)

canvas1.pack(fill="both", expand=True)

# Display image
canvas1.create_image(0, 0, image=bg,
                         anchor="nw")


#create button
buttonStart = Button(window,image=new_image1,height= 50, width=100,borderwidth=0,bg="#204050",command=subOpenPage1)
buttonExit = Button(window,image=new_image1_exit,bg="#FFFFFF",text="Exit",command = window.quit,borderwidth=0)



#display button
canvas1.create_window(15,265,anchor="nw",window=buttonStart)
canvas1.create_window(430, 430, anchor="nw", window=buttonExit)


window.mainloop()