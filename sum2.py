#! /usr/bin/python
#coding=utf-8

print("Type integers,each followed by enter,or ^d,or ^z to finish.")

total =  0
count =  0

while True:
    try:
        line = input()
        if line:
            number = int(line)
            count += 1
            total += number
    except ValueError as err:
        print(err)
        continue
    except EOFError:
        break

if count:
    print("count = ",count,"total = ",total,"mean = ",total/count)
