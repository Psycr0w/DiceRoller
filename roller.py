import random
import argparse
import re

parser = argparse.ArgumentParser()

parser.add_argument("dice", type=str)
args = parser.parse_args()

def roll(num):
    return random.randrange(1,num)

a = re.findall(pattern="^\d+", string=args.dice)
b = re.findall(pattern="\D", string=args.dice)
c = re.findall(pattern="\d+$", string=args.dice)

list = []
for x in range(int(a[0])):
    list.append(roll(int(c[0])))

if b[0] == 'd':
    seperator = ","
    print((str(list)))

if b[0] == 's':
    sum = 0
    for i in list:
        sum = sum + int(i)
    print(sum)