import os
import ctypes
from tkinter import *
from tkinter import messagebox

def fib(n):
    a=0
    b=1
    print(a)
    print(b)
    for i in range(1,n+1):
        c = a+b
        print(c)
        a=b
        b=c

def evenorodd(n):
    if n%2 == 0:
        print("number is even")
    else:
        print("number is odd")

def infinity():
    i = 10
    while i >=1:
        print(i)
        i+=1

def say(string):
    print(string)

def opensite(string):
    os.system("start chrome {}".format(string))

def factorl(n):
    f =1
    
    for i in range(1,n+1):
        f = f*i
        
    print(f)


def changeWallpaper(string):
    path = string
    ctypes.windll.user32.SystemParametersInfoW(20,0,path,3)

def shutdown():
    os.system('shutdown /p')

def prompt(title,content):
    root = Tk()
    root.withdraw()
    messagebox.showinfo('{}'.format(title),'{}'.format(content))
    root.mainloop()

def prompterror(title,content):
    root = Tk()
    root.withdraw()
    messagebox.showerror('{}'.format(title),'{}'.format(content))
    root.mainloop()

