import os
import time
from getpass import getuser
from tkinter import *
from tkinter import ttk
from threading import Thread
from cryptography.fernet import Fernet

root = Tk()
root.title('Login Info Storage')
root.geometry('500x200')
mainframe = ttk.Frame(root, padding='5 5 5 5')
mainframe.grid(row=0, column=0, sticky='N, E, W, S')
mainframe.rowconfigure(0, weight=1)
mainframe.columnconfigure(0, weight=1)
key = Fernet.generate_key()

if os.path.exists(f'C:\\Windows\\key.key'):
    pass
else:
    with open(f'C:\\Windows\\key.key', 'wb') as f:
        f.write(key)

with open(f'C:\\Windows\\key.key', 'rb') as f:
    key = f.read()

def decrypt():#DECRYPT
    with open(f'C:\\Windows\\passwords.txt', 'rb') as thedata:
        contents = thedata.read()
    decrypted = Fernet(key).decrypt(contents)
    with open(f'C:\\Windows\\passwords.txt', 'wb') as thedata:   
        thedata.write(decrypted)




def mkpsw(psw, i, u, y):
    psw = psw.get()
    if len(psw) > 5:
        
        with open(f'C:\\Windows\\security\\logs\\secinp.log', 'a') as pswfile:
            pswfile.write(str(f'{psw}'))
        
        v = ttk.Label(root, text="Password created successfully!", font=("Arial", 12), foreground="green")
        v.place(relx=0.3, rely=0.5)
        v.after(4000, lambda: v.destroy())
        try:
            i.destroy()
            u.destroy()
            y.destroy()
            a.destroy()
        except:
            pass
        main()
    else:
        a = ttk.Label(root, text="Password must be at least 6 or more characters.", font=("Arial", 12), foreground="red")
        a.place(relx=0.15, rely=0.5)
        a.after(4000, lambda: a.destroy())


def chkpsw(password_att, p, g, q):
    
    with open(f'C:\\Windows\\security\\logs\\secinp.log', 'r') as file:
        correct_pass = file.readline().split()[0]
        
    
    password_att = password_att.get()
    if str(correct_pass) != str(password_att):
        t = ttk.Label(root, text="Incorrect Password. Please try again.", foreground="red")
        t.place(relx=0.32, rely=0.5)
        t.after(5000, lambda: t.destroy())
    else:
        try:
            decrypt()
        except:
            pass
        store_psw(user_entry, pass_entry, p,g,q)


user_entry = StringVar()
pass_entry = StringVar()

def store_psw(user_entry, pass_entry, p,g,q):
    try:
        p.destroy()
        g.destroy()
        q.destroy()
    except:
        pass

    w = ttk.Label(root, text='Username')
    w.place(relx=0.25, rely=0.2)
    e = ttk.Entry(root, width=30, textvariable=user_entry)
    e.place(relx=0.15, rely=0.3)
    n = ttk.Label(root, text='Password')
    n.place(relx=0.65, rely=0.2)
    m = ttk.Entry(root, width=30, textvariable=pass_entry)
    m.place(relx=0.55, rely=0.3)
    s = ttk.Button(root, text="Add to password storage", command=lambda: add_entries(user_entry, pass_entry))
    s.place(relx=0.38, rely=0.5)
    c = ttk.Button(root, text='See all passwords', command=lambda: seefile())
    c.place(relx=0.42, rely=0.75)


def add_entries(user_entry, pass_entry):
        user_entry = user_entry.get()
        pass_entry = pass_entry.get()
        if len(user_entry) > 1 and len(pass_entry) > 1:
            
            with open(f'C:\\Windows\\passwords.txt', 'a') as f:
                f.write(f"\n{user_entry} : {pass_entry};")
            
            h = ttk.Label(root, text="Successfully Stored Info!")
            h.place(relx=0.38, rely=0.65)
            h.after(4000, lambda: h.destroy())

        else:
            l = ttk.Label(root, text="Please enter a valid user and password", foreground='red')
            l.place(relx=0.32, rely=0.7)
            l.after(4000, lambda: l.destroy())


def seefile():
    list = []
    
    with open(f'C:\\Windows\\passwords.txt', 'r') as file:
        alldata = file.readlines()[1:]
        for line in alldata:
            
            list.append(line)
        list = str(list)
        list = list.replace('[', '')
        list = list.replace(']', '')
        list = list.replace("'", "")
        list = list.replace(r"\n", '\n')
        list = list.replace(',', '')
    
    toot = Tk()
    text = ttk.Label(toot, text=str(list)).pack()
    toot.mainloop()    

def main():
    password_att = StringVar()
    psw = StringVar()

    path = f"C:\\Windows\\security\\logs"

    if os.path.exists(os.path.join(path, 'secinp.log')):
        p = ttk.Entry(mainframe, width=20, textvariable=password_att, show='*')
        p.grid(column=2, row=1, sticky="N, E")
        g = ttk.Label(mainframe, text="Enter your password", font=('Arial', 12))
        g.grid(column=1, row=1, sticky="N, E", padx=25) 
        q = ttk.Button(mainframe, text="Confirm", command=lambda: chkpsw(password_att, p, g, q))
        q.grid(row=2, column=2)
        
    else:
        y = ttk.Label(mainframe, text='Create the password you will use\n to access all of your passwords.', font=("Arial", 12))
        y.grid(column=1, row=1, sticky='N, E')
        u = ttk.Entry(mainframe, width=20, textvariable=psw)
        u.grid(row=1, column=2)
        i = ttk.Button(mainframe, text="Confirm", command=lambda: mkpsw(psw, y, u, i))
        i.grid(row=1, column=3, sticky="N, E", padx=5, pady=8)
main()
root.mainloop()
try:
    #ENCRYPT
    with open(f'C:\\Windows\\passwords.txt', 'rb') as thedata:
        contents = thedata.read()
    encrypted = Fernet(key).encrypt(contents)
    with open(f'C:\\Windows\\passwords.txt', 'wb') as thedata:   
        thedata.write(encrypted)
except Exception:
    print(Exception)
    pass
