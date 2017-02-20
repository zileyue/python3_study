#! /usr/bin/python3
#coding=utf-8

import random

def get_int(msg,minimun,default):
    line = input(msg)
    try:
        if not line and default is not None:
            return int(default)
        i = int(line)
        if i < int(minimun):
            return int(minimun)
        return i
    except ValueError as err:
        print(err)


rows = get_int("Please input rows:",4,4)
columns = get_int("Please input columns:",4,4)
minimun = get_int("Please input minimun:",-10000,0)
maximun = get_int("Please input maximun:",minimun,1000)

print(rows,columns,minimun,maximun)

row = 0
while row < rows:
    column = 0
    line = ""
    while column < columns:
        i = random.randint(minimun,maximun)
        s = str(i)
        while len(s) < 10:
            s = " " + s
        line += s
        column += 1
    print(line)
    row += 1
