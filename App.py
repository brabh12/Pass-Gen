from tkinter import * 
import random, string
import pyperclip

root =Tk()
root.geometry("400x250")
root.resizable(0, 0)
root.title("Pass Gen By Rabah.bct")
root.config(bg="#02EBAB")

heading = Label(root, text = 'Pass Gen By Rabah.bct', font='arial 15 bold', bg='#02EBAB').pack()
Label(root, text='Rabah.bct', font='arial 15 bold', bg='#02EBAB').pack(side = BOTTOM)

pass_len = IntVar()
pass_str = StringVar()

Label(root, text= 'Password Length', font='arial 10 bold', bg='#02EBAB').place(x = 50, y= 50)
Length = Spinbox(root, from_= 8, to_= 32, textvariable= pass_len, width= 15).place(x = 200, y = 50)
Label(root, text = 'Your Pass', font= 'arial 10 bold', bg='#02EBAB').place(x = 50, y = 80)
Entry(root, textvariable = pass_str).place(x = 200,y = 80)

def Generator():
    password = ''
    for x in range (0, 4):
        password = random.choice(string.ascii_uppercase)+\
                   random.choice(string.ascii_lowercase)+\
                   random.choice(string.digits)+\
                   random.choice(string.punctuation)
    for y in range(pass_len.get() -4):
        password = password+random.choice(string.ascii_uppercase + 
                                          string.ascii_lowercase + 
                                          string.digits + 
                                          string.punctuation)
    pass_str.set(password)

def Copy_password():
    pyperclip.copy(pass_str.get())

Button(root, text = "Gen Your Pass", command= Generator).place(x = 50, y =120)
Button(root, text= "Copy", command= Copy_password).place(x = 200, y= 120)


root.mainloop()