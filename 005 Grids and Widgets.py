from tkinter import *

root = Tk()
root.geometry("440x250")

def getval():
    print(uservalue.get())
    print(passvalue.get())

Label(root, text="Enter Credentials", font="PerpetuaTitlingMT 25 bold underline", pady=4, padx=25, fg="white", bg="black", relief=SUNKEN).grid(column=1)


user = Label(root, text="username")
password = Label(root, text="password")
user.grid(row=8,column=0)                 
password.grid(row=9,column=0)

##VARIABLE CLASSES IN TKINTER
# 1.booleanvar, doublevar, intvar, stringvar

uservalue = StringVar()
passvalue = StringVar()

userentry = Entry(root, textvariable= uservalue)
passentry = Entry(root, textvariable= passvalue)

userentry.grid(row=8, column=1)
passentry.grid(row=9, column=1)


Button(text="SUBMIT", command=getval).grid(column=1)

root.mainloop()