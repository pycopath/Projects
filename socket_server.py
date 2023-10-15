import socket
import select

HEADER = 10
IPADDR = ""#server ip
PORT = 1234

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Allows us to raconnect
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1 )
# Bind addr to server
s.bind((IPADDR, PORT))
# List of clients in server (including our socket)
socket_list = [s]
# Client names/alias
clients = {}

def recv_msg(client_conn):
    try:
        # Get message header length
        msg_header = client_conn.recv(HEADER)
        # If we didn't get a mesage header, the client closed the connection
        if not len(msg_header):
            return False
        # Converting the message into the actual length of the message
        msg_len = int(msg_header.decode("utf-8").strip())
        # Retuen a dictionary with the header value as 'header' and the msg length being recieved as 'data'
        return {'header': msg_header, 'data': client_conn.recv(msg_len)}
    except:
        return False

while True:
    # Start listening for connections
    s.listen()
    print("[LISTENING FOR CLIENTS]")
    while True:
        try:
            # Only really need data from the first list
            read_sockets, _, exception_sockets = select.select(socket_list, [], socket_list)
        except Exception:
            print("[CONNECTION CLOSED ABRUPTLY]")
            break
        for notified_socket in read_sockets:    
            # If this is true, someone is trying to connect and we have to accept them
            if notified_socket == s:
                client_conn, addr = s.accept()

                user = recv_msg(client_conn)
                # If the user disconnects/cannot be found, then ignore
                if user is False:
                    continue
                # Append the new client to the list of active clients
                socket_list.append(client_conn)
                # Add the new client to the client dictionary
                clients[client_conn] = user
                # Print new connection's ip address, and username from 'recv_msg' returned dictionary
                print(f"[NEW CONNECTION] {addr} [USERNAME]\
    {user['data'].decode('utf-8')}")
            # Else 
            else:
                # Whichever socket was notified will receive the message???
                msg = recv_msg(notified_socket)
                # If there is no message, print a closed connection from idkwtfgo...
                    
                try:
                    user = clients[notified_socket]
                    print(f"[RECIEVED MESSAGE] {user['data'].decode('utf-8')} >>> {msg['data'].decode('utf-8')}")
                except Exception:
                    print(f"[CLOSED CONNECTION] {client_conn}")
                    client_conn.close()
                    #If they're disconnected, we have to delete them from our dictionary
                    #del clients[notified_socket]
                    print(Exception)
                    break
                # For every connected client in the server
                for client_conn in clients:
                    if client_conn != notified_socket:
                        # Send user header with its info, then the message header with its info
                        client_conn.send(user['header'] + user['data'] + msg['header'] +msg['data'])
        # Handle errors   
        for notified_socket in exception_sockets:
            socket_list.remove(notified_socket)
            del clients[notified_socket]