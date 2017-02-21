#! /usr/bin/python3
#coding=utf-8

numbers = []
while True:
    try:
        line = input("Enter a number or Enter to finish:")
        if not line:
            break
        number = int(line)
        numbers.append(number)
    except ValueError as err:
        print(err)


count = len(numbers)
sum = 0
for i in numbers:
    sum += i

lowest = min(numbers)
highest = max(numbers)
if count:
    mean = sum / count

print("count = ",count,"sum = ",sum,"lowest = ",lowest,"highest = ",highest,"mean = ",mean)
