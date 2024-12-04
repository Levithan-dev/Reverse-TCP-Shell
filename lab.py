import colorama as clr
import os
import shutil









def trim(a,b,text):
    ran=b-a
    trimed=""
    for l in range(ran):
        trimed+=text[a]
        a+=1
    return trimed
print(clr.Fore.LIGHTMAGENTA_EX+"On the root directory!!!")









def filter(num, text):
    filtered = ""
    # Only iterate up to the length of the text to avoid index out of range
    for r in range(min(num, len(text))):
        filtered += text[r]
    return filtered











text="bruuuuuuuuuuuuuh"
print(filter(5,text))