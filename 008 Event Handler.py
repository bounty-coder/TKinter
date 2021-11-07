from tkinter import *

root = Tk()

def abc(event):
    print(f'You clicked here {event.x},{event.y}')

canvas_width = 600
canvas_height = 400

root.geometry(f"{canvas_width}x{canvas_height}")

wg =Button(root,text='Click me Please')  #this will create a button
wg.pack()

wg.bind('<Button-1>',abc)     #applying event on button. abc function will executes as a event handler
#More description about event handler is given on official website. Please refer. 

root.mainloop()