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
# from tkinter import ttk
# root=Tk()

# root.title("Image")
# lb=Label(root,text="this is image").pack(side=TOP,pady=10)

# path=PhotoImage(file="dolphin-2708695_1280.png")
# lb11=Label(root,image=path,width=2500,height=2500)
# lb11.pack()

# root.geometry("4000x4000")
# root.title("IMG")
# root.mainloop()

# from tkinter import*

# root=Tk()
# root.title("PythonLobby")
# w=Label(root,text="pythonLobby.com",font="60")
# w.pack()

# qa1=IntVar()
# qa2=IntVar()

# but0=Checkbutton(root,text="Learning",variable=qa1,onvalue=1,offvalue=0,height=3,width=12)
# but1=Checkbutton(root,text="Tutorial",variable=qa2,onvalue=1,offvalue=0,height=3,width=12)

# but0.pack()
# but1.pack()

# mainloop()



# from tkinter import*
# root=Tk()

# Canv=Canvas(root,bg="yellow",width=150,height=250)
# Canv.pack()

# lin=Canv.create_line(70,150,140,6)

# root.geometry("300x220")
# root.title("python")
# root.mainloop()

# from tkinter import*
# root=Tk()

# Canv=Canvas(root,bg="yellow",width=150,height=250)
# Canv.pack()

# lin=Canv.create_line(70,150,140,5,23,30)

# root.geometry("300x220")
# root.title("python")
# root.mainloop()


# from tkinter import*
# root=Tk()

# Canvas=Canvas(root,bg="yellow",width=150,height=250)
# Canvas.pack()

# rect=Canvas.create_rectangle(30,20,140,90,fill="light green")
# root.geometry("350x200")
# root.title("hnhn")
# root.mainloop()

# from tkinter import*
# root=Tk()

# can=Canvas(root,bg="yellow",width=150,height=250)
# can.pack()

# rec=can.create_oval(30,20,140,90,fill="light green")
# root.geometry("350x250")
# root.title("pythonlobby.com")
# root.mainloop()

# from tkinter import*

# root=Tk()
# root.title("radio button")
# value=StringVar(root,"2")

# rb1=Radiobutton(root,text="radio button 1",variable=value, value=1)
# rb2=Radiobutton(root,text="radio button 2",variable=value, value=2)
# rb3=Radiobutton(root,text="radio button 3",variable=value, value=3)

# rb1.pack()
# rb2.pack()
# rb3.pack()

# root.geometry("250x200")
# root.mainloop()

# from tkinter import*
# from tkinter import ttk

# root=Tk()
# li=Listbox(root,width=45,height=15,selectmode=MULTIPLE)
# li.pack()
# li.insert(0,"C")
# li.insert(1,"C++")
# li.insert(2,"java")
# li.insert(3,"python")

# root.geometry("400x240")
# root.title("pythonlobby.com")
# root.mainloop()



# from tkinter import*
# root=Tk()
# def callback():
#     text=textEditor.get(0.1,END)
#     print(text)

# textEditor= Text(root,width=43,height=10)
# textEditor.pack()

# button1 = Button(root,text="Display Text ", command=callback)
# button1.pack(pady=12)

# root.geometry("350x218")
# root.title("pythonlobby")
# root.mainloop()


from tkinter import*
root=Tk()
tb=Text(root,width=40,height=13,wrap=WORD)
tb.grid(row=0,column=0)

scro=Scrollbar(root,orient=VERTICAL,command=tb.yview)
scro.grid(row=0,column=1,sticky=N+S)
tb.config(yscrollcommand=scro.set)

root.geometry("350x220")
root.title("python")
root.mainloop()




