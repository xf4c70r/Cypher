from tkinter import *
from tkinter import messagebox
win = Tk()


def con():
    e3.delete(0,END)
    key = e2_value.get()
    string = e1_value.get()
    e = encode(key, string)
    e3.insert(END, e)
    e2.delete(0, END)
    e1.delete(0, END)

def con2():
    e3.delete(0,END)
    key = e2_value.get()
    e = e1_value.get()
    d = decode(key, e)
    e3.insert(END, d)
    e2.delete(0, END)
    e1.delete(0, END)

def encode(key, string):
    if key.isdigit():
        messagebox.showerror('Error','Key should be alphabetic!!!')
    else:    
        encoded_chars = []
        for i in range(len(string)):
            key_c = key[i % len(key)]
            encoded_c = chr(ord(string[i]) + ord(key_c) % 256)
            encoded_chars.append(encoded_c)
            encoded_string = ''.join(encoded_chars)
            l = encoded_string
        return l
       

def decode(key, string):
    if key.isdigit():
        messagebox.showerror('Error','Key should be alphabetic!!!')
    else:    
        key = e2_value.get()
        string = e1_value.get()
        encoded_chars = []
        for i in range(len(string)):
            key_c = key[i % len(key)]
            encoded_c = chr((ord(string[i]) - ord(key_c)) % 256)
            encoded_chars.append(encoded_c)
            encoded_string = ''.join(encoded_chars)
            l = encoded_string
        return l
        

def exit():
    win.destroy()


def clear():
    e1.delete(0, END)
    e3.delete(0, END)
    e2.delete(0, END)


win.title("VIGNERE CYPHER")
win.geometry("800x700")
win.config(background="#000088")

l1 = Label(win, text="THIS IS PROGRAM WHICH ENCRYPT OR DECRYPT THE TEXT", font=('times new roman', 15),bg="#2bff0a")
l1.place(x=100, y=5, width=600, height=80)

b1 = Button(win, command=con, text="ENCRYPT", font=('times new roman', 20), activebackground="#FF0000",bg="#ffc30f")
b1.place(x=100, y=345, width=200, height=50)

b2 = Button(win, command=con2, text="DECRYPT", font=('times new roman', 20), activebackground="#FF0000",bg="#ffc30f")
b2.place(x=500, y=345, w=200, height=50)

l2 = Label(win, text="Enter 'SECRET' Message: ", font=('times new roman', 15),bg="#faff9e")
l2.place(x=175, y=100, width=220, height=50)

l3=Label(win, text="Remember Key Should Be Alphabetic", font=('times new roman', 15),bg="#d6ffad")
l3.place(x=100, y=165, width=600, height=80)

e1_value = StringVar()
e1 = Entry(win, font=('times new roman', 15), textvariable=e1_value,bg="#fdffa1")
e1.place(x=405, y=100, width=195, height=50)

l4 = Label(win, text="Enter key:", font=('times new roman', 15),bg="#faff9e")
l4.place(x=175, y=270, width=220, height=50)

e2_value = StringVar()
e2 = Entry(win, font=('times new roman', 15), textvariable=e2_value,bg="#fdffa1")
e2.place(x=405, y=270, width=195, height=50)

l5 = Label(win, text="Your encrypted/decrypted message is:", font=('times new roman', 15),bg="#d6ffad")
l5.place(x=100, y=415, width=600, height=60)

e3 = Entry(win, font=('times new roman', 20),bg="#fdffa1")
e3.place(x=100, y=515, width=600, height=50)

b3 = Button(win, text="CLEAR", command=clear, font=('times new roman', 15), activebackground="#FF0000",bg="#f49eff")
b3.place(x=50, y=615, width=200, height=50)

b4 = Button(win, command=exit, text="EXIT", font=('times new roman', 15), activebackground="#FF0000",bg="#f49eff")
b4.place(x=550, y=615, width=200, height=50)

win.mainloop()