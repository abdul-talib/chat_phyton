import socket
import sys
from threading import Thread


def receiving(sock):
    while True:
        #receive the data from the server
        msg = sock.recv(1024).decode('utf-8')
        if msg:
            #print the message if there is message
            print(msg)



print('Client Server...')
# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#Prompt user to enter server ip address, port and name
ServerName = input("Enter chats server's ip address:")
port = int(input('port:'))
Name = input("Enter Client's Name")
server_address = (ServerName, port)
print('Trying to connect to {} the server port {}' .format(*server_address))


try:
    #connect to the server address
    sock.connect(server_address)
    print("Connected...")
    #send the name to the server
    data = Name
    sock.send(data.encode())

    #Call the receiving function
    receive_thread = Thread(target=receiving, args=(sock,))
    receive_thread.start()



    while True:
        newMessage = input("")
        if newMessage:
            #if there is new message
            print("me->", newMessage)
            sock.send(newMessage.encode('utf-8'))  # send message to the server
            sys.stdout.flush() # Push out all the data and buffer

finally:
    print('closing socket')
    sock.close()

