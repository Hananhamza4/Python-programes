from tkinter import*
from tkinter import ttk

root=Tk()
root.geometry("768x1152")


root.title("Mynthra")
path=PhotoImage(file="Screenshot 2025-05-09 at 11.16.17 AM.png")
lb11=Label(root,image=path,width=804,height=328)
lb11.pack()


Label(root, text="Login", font=("Helvetica", 18, "bold"), fg="#333",).place(x=60, y=350)
Label(root, text="or", font=("Helvetica", 18), fg="#333",).place(x=125, y=350)
Label(root, text="Signup", font=("Helvetica", 18, "bold"), fg="#333",).place(x=160, y=350)

Label(root, text="+91", font=("Helvetica", 14), fg="#333",).place(x=60, y=400)


Entry(root, font=("Helvetica", 14), width=80).place(x=100, y=400)

agree = IntVar()
Checkbutton(
    root,
    text="By continuing, I agree to the Terms of Use & Privacy Policy\nand I am above 18 years old.",
    variable=agree,
    font=("Helvetica", 9),
    fg="#333",
    wraplength=300,
    justify="left",
    activebackground="white",
    activeforeground="#333",
    selectcolor="white"
).place(x=60, y=450)

btn=Button(root,text="Countinue",fg="red",bg="black",bd=6,width=20,height=2)
btn.place(x=300,y=500)





root.mainloop()