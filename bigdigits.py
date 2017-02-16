#! /usr/bin/python3
#coding=utf-8


import sys


Zero = ["  ***  ",
        " *   * ",
        "*     *",
        "*     *",
        "*     *",
        " *   * ",
        "  ***  "]
One = [" * ", "** ", " * ", " * ", " * ", " * ", "***"]
Two = [" *** ", "*   *", "*  * ", "  *  ", " *   ", "*    ", "*****"]
Three = [" *** ", "*   *", "    *", "  ** ", "    *", "*   *", " *** "]
Four = ["   *  ", "  **  ", " * *  ", "*  *  ", "******", "   *  ",
        "   *  "]
Five = ["*****", "*    ", "*    ", " *** ", "    *", "*   *", " *** "]
Six = [" *** ", "*    ", "*    ", "**** ", "*   *", "*   *", " *** "]
Seven = ["*****", "    *", "   * ", "  *  ", " *   ", "*    ", "*    "]
Eight = [" *** ", "*   *", "*   *", " *** ", "*   *", "*   *", " *** "]
Nine = [" ****", "*   *", "*   *", " ****", "    *", "    *", "    *"]

BigDigits = [Zero,One,Two,Three,Four,Five,Six,Seven,Eight,Nine]

if len(sys.argv) < 2:
    print('Usage: ./bigdigits.py numbers_you_want_to_show_in_big_digit')
    sys.exit()

input_digits = sys.argv[1]
print('the input digit is: ',input_digits)
input_digits_count = len(input_digits)

print()
row = 0
while row < 7:

    line = ''
    count = 0
    while count < input_digits_count:
        digit = input_digits[count]
        try:
            number = int(digit)
            line = line + BigDigits[number][row] + ' '
        except ValueError as err:
           print('%s is not a digit!',digit)
        count += 1

    print(line)
    row += 1

