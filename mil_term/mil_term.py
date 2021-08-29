import os
import sys
import time

print("mil-term, version 0.0.1")

def fileopen():
    return "sorry this is version 0.0.1 mil-term, the option will be there in version 0.0.2 of mil-term"

def pswd():
    ans = "hewlman12%"
    print("BIT BOOTING...")
    time.sleep(3)
    pswd = input("Type password: ")
    if pswd == ans:
        print("DONE")
    else:
        print("WRONG CODE/PSWD")

def mine():
    print("BOOTING")

commands = {
    "pswd": pswd(),
    "ls": os.listdir(),
    "open": fileopen(),
    "dir": os.getcwd()
}


while 1:
    term = input("C~bin/bash~{0} ".format(os.getcwd()))
    if term:
        print(commands[term])


def start():
    print("START")
    time.sleep(1)
    print("booting..")
    time.sleep(2)
    print("decoded")

start()



