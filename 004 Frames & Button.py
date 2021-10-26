from tkinter import *

root = Tk()
root.geometry("1024x450")

def com():
    print("Button clicked")

f1 = Frame(root, bg='light blue',borderwidth=8,relief=RAISED)
f1.pack(side='left',anchor='nw')

l = Label(f1, text= 'Explorer')
l.pack(pady=100,padx=100,fill=Y)

b1 = Button(f1, fg='grey',text='Button', command=com)
b1.pack(fill=Y)

f2 = Frame(root, bg='red', borderwidth=4,relief=SUNKEN)
f2.pack(side='right',fill=X)

l = Label(f2, text= " Code here", font=("Helvetica 20 bold"))
l.pack(pady=200,fill=Y)

root.mainloop()