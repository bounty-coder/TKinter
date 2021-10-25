from tkinter import *

#Creating root
root = Tk()   

# GUI logic here

#Width x Height
root.geometry("1024x450")
#min width X height
root.minsize(400,150)

#text-> adds the text
#bd-> background 
#fg-> foreground
#font-> sets the font     font=("font-name",fontsize,"bold/italic")
#padx-> x-padding
#pady-> y-padding
#Relief->border style-[SUNKEN,RAISED,GROOVE,RIDGE]

##  Pack attributes
##  anchor = [nw,se,sw,ne as per north,east,west south directions]
##  side = top,right,left,bottom

t_label_head= Label(text="Python GUI-tKinter ",padx=15,pady=15,font=("calibri 24 bold"))
t_label_head.pack(fill=X)

t_label = Label(text='''Python offers multiple options for developing GUI (Graphical User Interface).\n Out of all the GUI methods, tkinter is the most commonly used method. \nIt is a standard Python interface to the Tk GUI toolkit shipped with Python.\n Python with tkinter is the fastest and easiest way to create the GUI applications. \nCreating a GUI using tkinter is an easy task.

To create a tkinter app:
1.Importing the module – tkinter
2.Create the main window (container)
3.Add any number of widgets to the main window
4.Apply the event Trigger on the widgets.''',bg="light blue", fg="black", padx=15,pady=15,font=("sans-serif",18,"italic"), borderwidth=3,relief=SUNKEN)


t_label.pack(anchor="ne",fill=X)

root.mainloop()