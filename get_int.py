
#! /usr/bin/python3
#coding=utf-8

def get_int(msg):
    while True:
        try:
            i = int(input(msg))
            return i
        except ValueError as err:
            print(err)
            continue
        except EOFError:
            print('Get EOF!')
            break