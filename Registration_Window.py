from tkinter import *
from firebase import firebase
from simplecrypt import encrypt, decrypt
import time
from tkinter import messagebox as messagebox
import gif_script as GIF

registration_window = Tk()
registration_window.minsize(400, 400)
registration_window.maxsize(400, 400)

username = ""
password = ""

firebase = firebase.FirebaseApplication(
    "https://data-3033d-default-rtdb.firebaseio.com/", None)


def change1():
    if(password_entry['show'] == "*"):
        password_entry['show'] = ""
    else:
        password_entry['show'] = "*"


def login_window():
    import Login_Window
    registration_window.destroy()


def register():
    label_e.place(relx=0.5, rely=0.6, anchor=CENTER)
    global username
    global password
    username = username_entry.get()
    password = password_entry.get()
    if (len(username) != 0 and len(password) != 0):
        cipher_code_2 = encrypt('TREE', password)
        hex_2 = cipher_code_2.hex()
        firebase.put('/', username, hex_2)
        username_entry.delete(0, END)
        password_entry.delete(0, END)
        messagebox.showinfo(
            'Success', 'Successfully Registered,you may now Log-In')
        time.sleep(3)
        login_window()
    else:
        messagebox.showinfo(
            'Error', 'Please try the password or username again!')
    label_e.place(relx=10, rely=10, anchor=CENTER)


label_e = Label(registration_window)

gif = GIF.gifplay(label_e, 'icon.gif', 0.08)
gif.play()

heading_label = Label(registration_window,
                      text="Register", font='arial 18 bold')
heading_label.place(relx=0.5, rely=0.2, anchor=CENTER)

username_label = Label(registration_window,
                       text="Username : ", font='arial 13')
username_label.place(relx=0.3, rely=0.4, anchor=CENTER)

username_entry = Entry(registration_window)
username_entry.place(relx=0.6, rely=0.4, anchor=CENTER)

password_label = Label(registration_window,
                       text="Password :  ", font='arial 13')
password_label.place(relx=0.3, rely=0.5, anchor=CENTER)

password_entry = Entry(registration_window, show="*")
password_entry.place(relx=0.6, rely=0.5, anchor=CENTER)

btn_reg = Button(registration_window, text="Sign Up",
                 font='arial 13 bold', command=register, relief=FLAT, padx=10)
btn_reg.place(relx=0.5, rely=0.75, anchor=CENTER)

btn_login_window = Button(registration_window, text="Log In",
                          font='arial 10 bold',  command=login_window, relief=FLAT)

btn_login_window.place(relx=0.9, rely=0.06, anchor=CENTER)
b = Checkbutton(registration_window, command=change1)
b.place(relx=0.8, rely=0.5, anchor=CENTER)
registration_window.mainloop()
