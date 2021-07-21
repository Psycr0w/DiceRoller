import random
import argparse
import re

help ="""
Simple dice program to evaluate mutli-sided dice, fudge dice and exploding dice.\n

Usage:

python roller.py

dicenumber = number of rolled dice.
mode = d, f, ! or s.
'd' will output the diceresults.
's' will output the sum of the dicerolls.
'!' will output exploding dice.
'f' is used for fudge dice. Since fudge dice are always the same, the input is <dicenumber>f.
number of sides = number of sides of the dice.

example:

roller.exe 2s10 - will print the sum of two tensided dice.
roller.exe 3d6  - will print the output of 3 sixsided dice.
roller.exe 20!6 - will print the output of 20 6 sided exploding dice.
roller.exe 6f   - will print the output and sum of 6 fudge dice.
"""

parser = argparse.ArgumentParser(description=help, formatter_class=argparse.RawDescriptionHelpFormatter)


parser.add_argument("dice", type=str)
args = parser.parse_args()

#TODO helpfile
# -h, h, /h, --help


a = re.findall(pattern="^\d+", string=args.dice)
b = re.findall(pattern="\D", string=args.dice)
c = re.findall(pattern="\d+$", string=args.dice)

def roll(num):
    return random.randrange(1,num + 1)

def recrand(x,a=0):
    while a%x<1:a+=random.randint(1,x)
    return a

list = []

string = "".join(b)


if string != 'f':
    if string != '!':
        for x in range(int(a[0])):
            list.append(roll(int(c[0])))

    else:
        for x in range(int(a[0])):
            list.append(recrand(int(c[0])))
        print((str(list)))

    if string == 'd':
        seperator = ","
        print((str(list)))

    elif string == 's!':
        sum = 0
        for i in list:
            if int(i) == int(c[0]):
                sum = sum + int(i) + roll(int(c[0]))
            else:
                sum = sum + int(i)
        print(sum)

    elif string == 's!':
        sum = 0
        print("yay")
        for i in list:
            if i == c:
                sum = sum + int(i) + recrand(int(c))
            else:
                sum = sum + int(i)
        print(sum)

    elif string == 's':
        sum = 0
        for i in list:
            sum = sum + int(i)
        print(sum)


else:
    for x in range(int(a[0])):
        list.append(roll(3))
    translation = {1: "+", 2: " ", 3: "-"}
    summe = 0
    for x in list:
        if x == 1:
            summe += 1
        elif x == 3:
            summe -= 1
        else:
            pass
    for i,x in enumerate(list):
        list[i] = translation[x]
    print(list)
    print(summe)