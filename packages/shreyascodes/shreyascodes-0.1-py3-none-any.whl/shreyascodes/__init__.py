import time
from os import *

def fib(n):
    a = 0
    b = 1
    print(a)
    print(b)
    for i in range(1,n+1):
        c = a+b
        time.sleep(0.5)
        print(c)
        a = b
        b = c

def say(string):
    print(string)

def add(i,n):
    return i+n

def sub(i,n):
    return i-n

def multi(i,n):
    return i*n

def div(i,n):
    return i/n

def evenorodd(n):
    if n%2 == 0:
        return 'even'
    else:
        return 'odd'

def infinity():
    i = 10
    while i>=1:
        print(i)
        i+=1

def factorl(n):
    f = 1
    for i in range(1,n+1):
        f = f*i
    return(f)

def table(n):
    for i in range(1,11):
        print(n*i)

def opensite(string):
    system(f"start chrome {string}")