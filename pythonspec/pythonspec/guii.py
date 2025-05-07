# from tkinter import *

# root = Tk()

# root.title("Hanan Window")
# root.geometry("1000x200")
# def clicked():
#     print("button clicked")
# lbl = Label(
#     root,
#     text='hello my name is hanan',
#     font=("Helvetica", 12),
#     fg='white',
#     bg='black'  # Set background to make white text visible
# )
# lbl.pack()
# lbl1= Label(root,text="macbook",font=("Helvetica",12),fg="white",bg="black")
# lbl1.pack()
# lbl2= Label(root,text="windows",font=("Helvetica",12),fg="white",bg="black")
# lbl2.pack()
# en=Entry(root)
# en.pack()
# btn=Button(root,text="Click Me",fg="red",bg="black",bd=6,command=clicked)
# btn.pack()
# root.mainloop()

# from tkinter import*
# root=Tk()

# root.title("LogIn")
# root.geometry('1000x200')
# def pasas():
#     print("Password changed")
# lb1=Label(root,text="username",font=("Helvetica",12),fg="white",bg="black")
# lb1.place(x=2,y=20)
# ent=Entry(root)
# ent.place(x=70,y=15)
# lb2=Label(root,text="Password",font=("Helvetica",12),fg="white",bg="black")
# lb2.place(x=2,y=60)
# ent=Entry(root)
# ent.place(x=70,y=55)
# bt=Button(root,text="Update",fg="red",bg="black",bd=6,command=pasas)
# bt.place(x=2,y=80)

# root.mainloop()

# from tkinter import*

# root=Tk()
# root.title("Color")

# lb=Label(root,text="Color plate",font="60")
# lb.pack()

# fr1=Frame(root,bg="green",width=120,height=100)
# fr1.pack(side=LEFT,padx=20)

# fr2=Frame(root,bg="red",width=120,height=100)
# fr2.pack(side=LEFT)

# root.geometry("300x150")
# root.mainloop()

# from tkinter import*
# root=Tk()

# root.title("Image")
# lb=Label(root,text="this is image").pack(side=TOP,pady=10)

# path=PhotoImage(file="dolphin-2708695_1280.png")
# lb11=Label(root,image=path,width=2500,height=2500)
# lb11.pack()

# root.geometry("4000x4000")
# root.title("IMG")
# root.mainloop()

from tkinter import*

root=Tk()
root.title("PythonLobby")
w=Label(root,text="pythonLobby.com",font="60")
w.pack()

qa1=IntVar()
qa2=IntVar()

but0=Checkbutton(root,text="Learning",variable=qa1,onvalue=1,offvalue=0,height=3,width=12)
but1=Checkbutton(root,text="Tutorial",variable=qa2,onvalue=1,offvalue=0,height=3,width=12)

but0.pack()
but1.pack()

mainloop()