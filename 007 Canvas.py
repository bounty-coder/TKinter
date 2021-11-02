from tkinter import *

root = Tk()

canvas_width = 600
canvas_height = 400

root.geometry(f"{canvas_width}x{canvas_height}")

# Canvas is a rectangular area intended for drawing pictures or other complex layouts.
# You can place graphics, text, widgets or frames on a Canvas.
can_widget = Canvas(root, width=canvas_width, height=canvas_height)
can_widget.pack()

#To create a line specify parameters
# (x1,x2,y1,y2,fill="color-name")
can_widget.create_line(0,0,200,400,fill='red')
can_widget.create_line(0,400,900,63,fill='blue')

#To create a rectangle specify
can_widget.create_rectangle(40,40,200,200,fill='green')

#to write a text
can_widget.create_text(125,125,text="Canvas")

#to create an oval
can_widget.create_oval(400,200,250,400,fill='#123456')

#function written more down will be at top frame in GUI or will overwrite the previous function.

#There are many more create widget functions in tkinter for ex. window, polygon, image, bitmap. They just work the similar
root.mainloop()