from tkinter import *
from firebase import firebase
from simplecrypt import encrypt, decrypt
from tkinter import messagebox as messagebox
import time
import gif_script as GIF

username = ""
password_entered = ""
password_real = ""

firebase = firebase.FirebaseApplication(
    "https://data-3033d-default-rtdb.firebaseio.com/", None)


def signup_window():
    import Registration_Window
    login_window.destroy()


def change1():
    if(login_password_entry['show'] == "*"):
        login_password_entry['show'] = ""
    else:
        login_password_entry['show'] = "*"


def login():
    label_j.place(relx=0.5, rely=0.6, anchor=CENTER)
    global username
    global password_entered
    global password_real
    username = login_username_entry.get()
    password_entered = login_password_entry.get()
    if(len(username) != 0 and len(password_entered) != 0):
        try:
            hex_2 = firebase.get('/', username)
            cipher_2 = bytes.fromhex(hex_2)
            passw = decrypt('TREE', cipher_2)
            password_real = passw.decode('utf-8')
            if(password_real == password_entered):
                messagebox.showinfo('Success', 'Successfully Logged In')
                login_username_entry.delete(0, END)
                login_password_entry.delete(0, END)
                time.sleep(3)
                login_window.destroy()
                root = Tk()
                root.minsize(600, 400)
                root.maxsize(600, 400)

                label_a = Label(root, text="Welcome " + username+"!",
                                font=("Comic Sans MS", 18, 'bold'), fg="black")
                label_a.place(relx=0.5, rely=0.5, anchor=CENTER)

                root.mainloop()

            else:
                messagebox.showinfo(
                    'Error', 'Please check the username and password again!')
        except:
            messagebox.showinfo('Error', 'No username found')
    else:
        messagebox.showinfo(
            'Error', 'Please check the username and password again!')
    label_j.place(relx=10, rely=10, anchor=CENTER)


login_window = Tk()
login_window.geometry("400x400")

label_j = Label(login_window)

gif = GIF.gifplay(label_j, 'icon.gif', 0.08)
gif.play()

log_heading_label = Label(
    login_window, text="Log In", font='arial 18 bold')
log_heading_label.place(relx=0.5, rely=0.2, anchor=CENTER)

login_username_label = Label(
    login_window, text="Username : ", font='arial 13')
login_username_label.place(relx=0.3, rely=0.4, anchor=CENTER)

login_username_entry = Entry(login_window)
login_username_entry.place(relx=0.6, rely=0.4, anchor=CENTER)

login_password_label = Label(
    login_window, text="Password : ", font='arial 13')
login_password_label.place(relx=0.3, rely=0.5, anchor=CENTER)

login_password_entry = Entry(login_window, show="*")
login_password_entry.place(relx=0.6, rely=0.5, anchor=CENTER)

btn_login = Button(login_window, text="Log In",
                   font='arial 13 bold', relief=FLAT, command=login)
btn_login.place(relx=0.5, rely=0.7, anchor=CENTER)

btn_singup_window = Button(login_window, text="Sign Up",
                           font='arial 10 bold',  command=signup_window, relief=FLAT)

btn_singup_window.place(relx=0.9, rely=0.06, anchor=CENTER)
b = Checkbutton(login_window, command=change1)
b.place(relx=0.8, rely=0.5, anchor=CENTER)
login_window.mainloop()
