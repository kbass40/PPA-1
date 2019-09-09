''' 
PPA-1 

Code Authored By:
Daniel Tymecki and Kyle Bassignani

'''

import re
import logging
import pytest
from BMI import *

def print_heading(s):
    print('*'*25,s,'*'*25)

def print_border():
    print('='*66)

def prompt_user(phrase="", format=None): #format in this instance is a regex of what to expect
    wrong = True
    while wrong:
        print(phrase)
        temp = str(input("> "))
        p = re.compile(format)
        if p.match(temp):
            return temp
        else:
            print('Sorry, your input was not correct. Please try again matching this regex pattern: ',p,'.\n')
        

# This function simply displays the menu for the prompt
def print_menu():
    print_heading("WELCOME TO PP1")
    print_border()
    print("Please select the option you'd like :")
    print('1. Function One')
    print('2. Function Two')
    print('3. Function Three')
    print('4. Function Four')
    print('5. Exit')
    print_border()
    choice = prompt_user("Please select the number of the function you'd like",'[1-5]')
    print(choice)


print_menu()