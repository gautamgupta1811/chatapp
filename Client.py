#!C:/Python36/python.exe

import socket
 
def Main():
        # in case of muliple devices connected over same network change loacalhost to ip of the network
        host = 'localhost'
        port = 80
         
        mySocket = socket.socket()
        mySocket.connect((host,port))
         
        message = input(" -> ")
         
        while message != 'q':
                mySocket.send(message.encode())
                data = mySocket.recv(1024).decode()
                 
                print ('Received from server: ' + data)
                 
                message = input(" -> ")
                 
        mySocket.close()
 
if __name__ == '__main__':
    Main()
