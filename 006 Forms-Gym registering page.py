from tkinter import *

root = Tk()

def getval():
    print("Yayy welcome new member")
    print(f"{namevalue.get(),phonevalue.get(),gendervalue.get(),paymentmethodvalue.get(),addressvalue.get(),nutrientvalue.get()}")
    with open("record.csv","a") as f:
        f.write(f"{namevalue.get(),phonevalue.get(),gendervalue.get(),paymentmethodvalue.get(),addressvalue.get(),nutrientvalue.get()}\n")
    
root.geometry("450x280")

#Heading
Label(root,text="Welcome to SHER🦁 GYM", font="comicsansms 14 bold",pady=18,fg="#ffc800").grid(row=0, column=3)

#Text for the form
name=Label(root,text="Name")
phone=Label(root,text="Phone")
gender=Label(root,text="Gender")
paymentmethod=Label(root,text="Payment Method")
address=Label(root,text="Address")

#packing grids
name.grid(row=2,column=2,pady=2)
phone.grid(row=3,column=2,pady=2)
gender.grid(row=4,column=2,pady=2)
paymentmethod.grid(row=5,column=2,pady=2)
address.grid(row=6,column=2,pady=2)

#Tkinter variables for storing entries
namevalue = StringVar()
phonevalue = StringVar()
gendervalue = StringVar()
paymentmethodvalue=StringVar()
addressvalue=StringVar()
nutrientvalue=IntVar()

#Entries for our form
nameentry=Entry(root, textvariable=namevalue)
phoneentry=Entry(root, textvariable=phonevalue)
genderentry1=Radiobutton(root,text="Male",variable=gendervalue,value="M",activebackground="#AB3456")
genderentry2=Radiobutton(root,text="Female",variable=gendervalue,value="F",activebackground="#AB3456")
paymentmethodentry=Entry(root, textvariable=paymentmethodvalue)
addressentry=Entry(root, textvariable=addressvalue)

#Packing the Entries
nameentry.grid(row=2,column=3,pady=2)
phoneentry.grid(row=3,column=3,pady=2)
genderentry1.grid(row=4,column=3,columnspan=2,sticky=N)
genderentry2.grid(row=4,column=3,columnspan=2,sticky=E)
paymentmethodentry.grid(row=5,column=3,pady=2)
addressentry.grid(row=6,column=3,pady=2)

#checkbox
nutvalue=Checkbutton(text="Want to prebook your protein and nutrients?",variable=nutrientvalue,pady=10)
nutvalue.grid(row=7,column=3)

#Button
Button(text="Submit",command=getval).grid(row=8,column=3)
root.mainloop()