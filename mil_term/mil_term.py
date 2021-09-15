import json
import os
import sys
import time
import getpass
import time

print("mil-term, version 0.0.2")



def pswd():
    ans = "shinxatjg90%"
    print("BIT BOOTING...")
    time.sleep(3)
    pswd = getpass.getpass(prompt="Type password: ")
    if pswd == ans:
        print("DONE")
    else:
        print("WRONG CODE/PSWD")
        quit()







def edit():
    ask = input("file name: ")
    choose = input("WARNING! do you want to remove all the content or append content: ")  
    if choose == "append":
        f = open(ask, "a")
        content = input("CONTENT: ")
        f.write(content)
        f.close()
    elif choose == "remove":
        d = open(ask, "w")
        content = input("CONTENT: ")
        d.write(content)
        d.close()
    

def fileopen():
    print("FILE MIL")
    name = input("type file name: ")
    op = open(name, "r")
    op.seek(0)
    print(op.read())

def echo():
    echo = input("Type echo <inter> Some text to echo some text in mil_term\n: ")
    echo_text = echo.split('<inter>')
    print(echo_text[1])

def credits():
    print("credits for mil_term")
    time.sleep(2)
    credits = {
        "Rigved": "code",
        "Aneesh": "ideas"
    }
    for i in credits:
        credits[i] = str(credits[i])
    print(credits)

commands = {
    "pswd": pswd(),
    "ls": os.listdir(),
    "dir": os.getcwd(),
    "credits": credits()

}

def mkd():
    mkd = input("make dir: ")
    folder = mkd.split("<inter>")
    os.mkdir(folder[1])

def rmd():
    rm = input("remove dir: ")
    sp  = rm.split("<inter>")
    os.rmdir(sp[1])

def rmf():
    rm = input("remove file: ")
    sp = rm.split("<inter>")
    os.remove(sp[1])

def mkf():
    new = input("make file : ")
    mkf = new.split("<inter>")
    new_file = open(mkf[1], "x")

while 1:
    dir = os.getcwd()
    term = input("C~bin/bash~{0} ".format(os.getcwd()))
    if term in commands:
        print(commands[term])
    else:
        pass

    if term == "open":
        fileopen()
    elif term == "edit":
        edit()
    elif term == "find":
        ask = input("find: ")
        if os.path.exists(ask) == True:
            print("FILE/FOLDER EXISTS IN DIR " + os.getcwd())
    elif term == "echo":
        echo()
    elif term == "mkdir":
        mkd()
    elif term == "rmdir":
        rmd()
    elif term == "mkf":
        mkf()
    elif term == "rmf":
        rmf()
    else:
        pass


def start():
    print("START")
    time.sleep(1)
    print("booting..")
    time.sleep(2)
    print("decoded")

start()



