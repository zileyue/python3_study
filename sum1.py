#! /usr/bin/python
#coding=utf-8

print("Type integers,each follow by enter,or just enter to exit.")

total = 0
count  = 0

while True:
    line = input("Input integers: ")
    if line:
        try:
            number = int(line)
            total += number
            count += 1
        except ValueError as err:
            print(err)
            continue

    else:
        break


if count:
    print("count = ",count,"total = ",total,"mean = ",total/count)
