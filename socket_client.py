import socket
import select
import errno


HEADER = 10
IPADDR = ''#server ip
PORT = 1234

uname  = input("[ENTER USERNAME]: ")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((IPADDR, PORT))
# So the received function will not be blocked
s.setblocking(False)
# Encode username to be sent
username = uname.encode('utf-8')
# Length of username
user_header = f"{len(username):<{HEADER}}".encode('utf-8')
# Send unsername length and name
s.send(user_header + username)


while True:
    # Get message
    msg = input(f"{uname} >>> ")
    
    if msg:
        # Encode message to be sent
        msg = msg.encode('utf-8')
        # Get length of message
        msg_header = f"{len(msg):<{HEADER}}".encode('utf-8')
        # Send the message
        s.send(msg_header + msg)
    
    
    try:
        while True:
            #receive message
            user_header = s.recv(HEADER)
            #If no message, exit and close connection
            if not len(user_header):
                print("[CONNECTION CLOSED BY SERVER]")
                SystemExit()
            
            user_length = int(user_header.decode('utf-8').strip())
            username = s.recv(user_length).decode('utf-8')

            msg_header = s.recv(HEADER)
            msg_length = int(msg_header.decode('utf-8').strip())
            msg = s.recv(msg_length).decode('utf-8')

            print(f"{username} > {msg}")
    except IOError as e:
        if e.errno != errno.EAGAIN or e.errno != errno.EWOULDBLOCK:
            #print("[READING ERROR]", str(e))
            SystemExit()
    
    except Exception as e:
        print('[GENERAL ERROR]', str(e))
        SystemExit()