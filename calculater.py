# from tkinter import*

# root=Tk()
# root.geometry("350x400")
# root.title("calculator")

# ent=Entry(root,bg="white",fg="black",bd=5,width=30,)
# ent.place(x=30,y=10)

# bt1=Button(root,text=" AC ",fg="blue",bd=10)
# bt1.place(x=30,y=80)

# bt2=Button(root,text=" +/- ",fg="gray",bd=10)
# bt2.place(x=100,y=80)

# bt3=Button(root,text=" %  ",fg="gray",bd=10)
# bt3.place(x=170,y=80)

# bt4=Button(root,text=" / ",bg="red",fg="red",bd=10)
# bt4.place(x=240,y=80)



# bt5=Button(root,text=" 7 ",fg="gray",bd=10)
# bt5.place(x=30,y=120)

# bt6=Button(root,text=" 8 ",fg="gray",bd=10)
# bt6.place(x=100,y=120)

# bt7=Button(root,text=" 9  ",fg="gray",bd=10)
# bt7.place(x=170,y=120)

# bt8=Button(root,text=" x ",bg="red",fg="red",bd=10)
# bt8.place(x=240,y=120)


# bt9=Button(root,text=" 4 ",fg="gray",bd=10)
# bt9.place(x=30,y=160)

# bt10=Button(root,text=" 5 ",fg="gray",bd=10)
# bt10.place(x=100,y=160)

# bt11=Button(root,text=" 6  ",fg="gray",bd=10)
# bt11.place(x=170,y=160)

# bt12=Button(root,text=" - ",bg="red",fg="red",bd=10)
# bt12.place(x=240,y=160)


# bt13=Button(root,text=" 1 ",fg="gray",bd=10)
# bt13.place(x=30,y=200)

# bt14=Button(root,text=" 2 ",fg="gray",bd=10)
# bt14.place(x=100,y=200)

# bt15=Button(root,text=" 3  ",fg="gray",bd=10)
# bt15.place(x=170,y=200)

# bt16=Button(root,text=" + ",bg="red",fg="red",bd=10)
# bt16.place(x=240,y=200)



# bt17=Button(root,text=" @ ",bg="red",fg="black",bd=10)
# bt17.place(x=30,y=240)

# bt18=Button(root,text=" 0 ",bg="red",fg="black",bd=10)
# bt18.place(x=100,y=240)

# bt19=Button(root,text=" .  ",fg="black",bg="black",bd=10)
# bt19.place(x=170,y=240)

# bt20=Button(root,text=" = ",bg="red",fg="red",bd=10)
# bt20.place(x=240,y=240)







# root.mainloop()

from tkinter import *

root = Tk()
root.geometry("350x400")
root.title("calculator")

ent = Entry(root, bg="white", fg="black", bd=5, width=30,)
ent.place(x=30, y=10)

# Store the current calculation
current_calculation = ""

def button_click(number):
    global current_calculation
    current_calculation += str(number)
    ent.delete(0, END)
    ent.insert(0, current_calculation)

def clear():
    global current_calculation
    current_calculation = ""
    ent.delete(0, END)

def calculate():
    global current_calculation
    try:
        # Replace 'x' with '*' for proper evaluation
        expression = current_calculation.replace('x', '*')
        result = str(eval(expression))
        ent.delete(0, END)
        ent.insert(0, result)
        current_calculation = result
    except:
        ent.delete(0, END)
        ent.insert(0, "Error")
        current_calculation = ""

def plus_minus():
    global current_calculation
    if current_calculation and current_calculation[0] == '-':
        current_calculation = current_calculation[1:]
    else:
        current_calculation = '-' + current_calculation
    ent.delete(0, END)
    ent.insert(0, current_calculation)

def percentage():
    global current_calculation
    try:
        value = float(current_calculation)
        current_calculation = str(value / 100)
        ent.delete(0, END)
        ent.insert(0, current_calculation)
    except:
        ent.delete(0, END)
        ent.insert(0, "Error")
        current_calculation = ""

# Number buttons
bt5 = Button(root, text=" 7 ", fg="gray", bd=10, command=lambda: button_click(7))
bt5.place(x=30, y=120)

bt6 = Button(root, text=" 8 ", fg="gray", bd=10, command=lambda: button_click(8))
bt6.place(x=100, y=120)

bt7 = Button(root, text=" 9  ", fg="gray", bd=10, command=lambda: button_click(9))
bt7.place(x=170, y=120)

bt9 = Button(root, text=" 4 ", fg="gray", bd=10, command=lambda: button_click(4))
bt9.place(x=30, y=160)

bt10 = Button(root, text=" 5 ", fg="gray", bd=10, command=lambda: button_click(5))
bt10.place(x=100, y=160)

bt11 = Button(root, text=" 6  ", fg="gray", bd=10, command=lambda: button_click(6))
bt11.place(x=170, y=160)

bt13 = Button(root, text=" 1 ", fg="gray", bd=10, command=lambda: button_click(1))
bt13.place(x=30, y=200)

bt14 = Button(root, text=" 2 ", fg="gray", bd=10, command=lambda: button_click(2))
bt14.place(x=100, y=200)

bt15 = Button(root, text=" 3  ", fg="gray", bd=10, command=lambda: button_click(3))
bt15.place(x=170, y=200)

bt18 = Button(root, text=" 0 ", bg="red", fg="black", bd=10, command=lambda: button_click(0))
bt18.place(x=100, y=240)

# Operation buttons
bt4 = Button(root, text=" / ", bg="red", fg="red", bd=10, command=lambda: button_click('/'))
bt4.place(x=240, y=80)

bt8 = Button(root, text=" x ", bg="red", fg="red", bd=10, command=lambda: button_click('x'))
bt8.place(x=240, y=120)

bt12 = Button(root, text=" - ", bg="red", fg="red", bd=10, command=lambda: button_click('-'))
bt12.place(x=240, y=160)

bt16 = Button(root, text=" + ", bg="red", fg="red", bd=10, command=lambda: button_click('+'))
bt16.place(x=240, y=200)

# Special buttons
bt1 = Button(root, text=" AC ", fg="blue", bd=10, command=clear)
bt1.place(x=30, y=80)

bt2 = Button(root, text=" +/- ", fg="gray", bd=10, command=plus_minus)
bt2.place(x=100, y=80)

bt3 = Button(root, text=" %  ", fg="gray", bd=10, command=percentage)
bt3.place(x=170, y=80)

bt19 = Button(root, text=" .  ", fg="black", bg="black", bd=10, command=lambda: button_click('.'))
bt19.place(x=170, y=240)

bt20 = Button(root, text=" = ", bg="red", fg="red", bd=10, command=calculate)
bt20.place(x=240, y=240)

# The @ button doesn't have a clear function, so I'll leave it without a command
bt17 = Button(root, text=" @ ", bg="red", fg="black", bd=10)
bt17.place(x=30, y=240)

root.mainloop()