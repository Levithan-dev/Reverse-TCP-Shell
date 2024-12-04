import os
import shutil
import colorama as clr
import time
parent_dir = os.path.dirname(os.getcwd())
def tm():
    time.sleep(0)
def pdir():
    tm()
    print(clr.Fore.GREEN+"Current Working directory:",os.getcwd())
def odir():
    tm()
    os.chdir("..")
    print(clr.Fore.BLUE+"Gone one step back")
def ls():
    tm()
    stuff=os.listdir(os.getcwd())
    print(f"{clr.Fore.YELLOW}Stuff inside current dir: {stuff}")
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
print(clr.Fore.LIGHTMAGENTA_EX+"On the root directory!!!")

#W commands
def commandls(command):
    path=trim(3,len(command),command)
    if command=="ls":
        print(clr.Fore.YELLOW,os.listdir(os.getcwd()))
    else:
        print(clr.Fore.YELLOW,os.listdir(path))
def commandcd(command):
    path=trim(3,len(command),command)
    try:
        os.chdir(path)
    except:
        print("No such directory!")
def commandrm(command):
    path1=trim(3,len(command),command)
    try:
        os.remove(path1)
    except:
        print("Not a file!")
def commandrmdir(command):
    path=trim(6,len(command),command)
    try:
        shutil.rmtree(path)
    except:
        print("Not a directory!")
while True:
    command=input(f"{clr.Fore.LIGHTMAGENTA_EX}{os.getcwd()}>> ")
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
print(clr.Fore.RED+"Shell closed!!!")