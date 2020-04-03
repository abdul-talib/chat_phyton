from threading import Thread
import socket
import sys


#broadcast all the message to all the client except the client itself
def broadcast(message, connect):
    sender = ""
    for name, client in list_of_clients.items():
        if client == connect:
            sender = name
    for name, client in list_of_clients.items():
        if client != connect:
            try:
                if "has joined the chat" not in message:
                    newMessage = sender + "->" + message
                    client.send(newMessage.encode('utf-8'))
                else:
                    client.send(message.encode('utf-8'))
            except:
                client.close()

def sending():
    while True:
        message = input("")
        for clients in list_of_clients.values():
            try:
                newMessage = Name + "->" + message
                clients.send(newMessage.encode('utf-8'))
            except:
                clients.close()

def receiving(connection , name):
    while True:
        #receive message
        msg = connection.recv(1024).decode('utf-8')
        if "has joined the chat" not in msg:
            print(name, "->", msg)
            broadcast(msg, connection)
        else:
            #receive the message on who join the chat
            print(msg)
            broadcast(msg, connection)


def accept():
    while True:
        print('Waiting for incoming connections....')
        connection, client_address = sock.accept()
       # connection.settimeout(60)
        print('Received connection from', serverName, port)
        print('Connection Established. Connected from', serverName)
        newName = connection.recv(1024).decode()
        JoinMessage = newName + " has joined the chat."

        list_of_clients[newName] = connection
        print(JoinMessage)
        connection.send(JoinMessage.encode())  # send message
        broadcast(JoinMessage, connection)
        #Create a thread for sending
        sending_thread = Thread(target=sending)
        sending_thread.start()
        #Create a thread for receiving
        receiving_thread = Thread(target=receiving, args=(connection, newName))
        receiving_thread.start()





serverName = input('Hello. this is CSC1010 Chat server, please enter the listening port: ')
port = int(input('port'))
Name = input("Enter Name")

print("Trying to connect to the server: ", serverName, port)

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.bind((serverName, port))
#dictionary to store the client name and connection
list_of_clients = {}

# Listen for incoming connections
if __name__ == "__main__":
    sock.listen(1)
    # Wait for a connection
    new_thread = Thread(target=accept)
    new_thread.start()
    new_thread.join()
    sock.close()


