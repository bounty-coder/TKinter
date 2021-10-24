from tkinter import *

#Creating root
root = Tk()   

# GUI logic here

#Width x Height
root.geometry("1024x640")
#min width X height
root.minsize(400,150)
#max width x Height
root.maxsize(1380,1000)

first = Label(text="Hello World!! This is my first Tkinter app")
first.pack()

root.mainloop()