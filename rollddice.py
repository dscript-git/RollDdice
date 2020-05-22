#!/usr/bin/env python3

import random
import os

#colors
yellow = '\033[93m'
green = '\033[92m'
good = '\033[92m[+]\033[0m'

#variables
min = 1
max = 6
roll_dice = True
#Let's begin
print (green,"Thank you for checking my code...")
print ("===> Roll-d-Dice v1.0 => dscript-git <===")
print (yellow,"Pls wait... ")
os.system('sleep 3')

def roll_d_dice():
    while roll_dice:

        print (green,"Rolling dice... What would it be...")
        print (yellow,"Here it is ... ")
        dice =  random.randint(min,max)
        os.system('sleep 2')
        print (good,"DICE: ",green,dice)
        ask = input("Roll the Dice Again? y/n: "'\033[93m')
        if ask == 'y' or ask == 'Y':
            os.system('clear')
            roll_d_dice()
        elif ask == 'n' or ask == 'N':
            os.system('clear')
            exit()
        else:
            os.system('clear')
            exit()


roll_d_dice()
