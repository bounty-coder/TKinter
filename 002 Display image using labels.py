from tkinter import *
from PIL import Image, ImageTk  
#Python Imaging library
#adds support for opening, manipulating, and saving various image formats 

#Creating root
root = Tk()   

# GUI logic here

#Width x Height
root.geometry("1024x640")
#min width X height
root.minsize(400,150)
#max width x Height
root.maxsize(1380,1000)

#importing image
#comment out below line for basic tKinter importing(remove or comment line 22-23 for the same)
#photo = PhotoImage(file="assets/002 1.png")

image = Image.open("assets/002 2.jpg")      #PIL modules
photo = ImageTk.PhotoImage(image)

first = Label(image = photo)
first.pack()

root.mainloop()