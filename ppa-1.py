''' 
PPA-1 

Code Authored By:
Daniel Tymecki and Kyle Bassignani

'''

import re

# import pytest

from BMI import *
from EmailVerifier import *
from Retirement import *
from SplitTip import *
from database import *
import pytest


def print_heading(s):
    print('*'*25,s,'*'*25)

def print_border():
    print('='*66)

def prompt_user(phrase="", format=None): # format in this instance is a regex of what to expect
    wrong = True
    while wrong:
        print(phrase)
        temp = str(input("> "))
        p = re.compile(format)
        if p.match(temp):
            return temp
        else:
            print('Sorry, your input was not correct. Please try again matching this regex pattern: ',p,'.\n')

def promt_for_BMI():
    feet = prompt_user("Please enter your height in feet", '^[0-8]$')
    inches = prompt_user("Please enter your height in inches", '^[0-9]+$')
    pounds = prompt_user("Please enter your weight in pounds", '\d*\.\d+|\d+')
    try:
        return DoBMI(int(feet), int(inches), float(pounds))
    except RuntimeError as e:
        print(e)
        return ''

def prompt_for_retirement_age():
    age = prompt_user("Please enter your age", '^[0-9]+$')
    salary = prompt_user("Please enter your salary as a number", '^[0-9]+$')
    saved = prompt_user("Please enter the percantage of your salary that you save", '\d*\.\d+|\d+')
    goal = prompt_user("Please enter how much money you need to retire as a number", '^[0-9]+$')
    try:
        return Retirement(int(age), int(salary), float(saved), int(goal))
    except RuntimeError as e:
        print(e)
        return ''

def prompt_for_split_tip():
    totalAmount = prompt_user("Please enter the total amount of the meal", '\d*\.\d+|\d+')
    numberOfGuests = prompt_user("Please enter the total number of guests", '^[0-9]+$')
    try:
        return SplitTip(round(float(totalAmount), 2), int(numberOfGuests))
    except RuntimeError as e:
        print(e)
        return ''

def prompt_for_email_verifier():
    email = prompt_user("Please enter the email you'd like to check",'.*')
    return Verify(str(email))

def get_database_data(name):
    db = DBConnection()

    curr = db.conn.cursor(buffered=True)

    data = []
    query = "SELECT * FROM "+ name+ ";"
    curr.execute(query)

    for d in curr:
        data.append(d)
        
    return data

def print_database_data(data):
    for d in data:
        print(d)


# This function simply displays the menu for the prompt
def print_menu(first):
    if first:
        print_heading("WELCOME TO PP1")
    print_border()
    print("Please select the option you'd like :")
    print('1. BMI Function')
    print('2. Retirement Age')
    print('3. Email Verifier')
    print('4. Split the Tip')
    print('5. Exit')
    print_border()
    choice = prompt_user("Please select the number of the function you'd like",'^[1-5]$')
    if choice == "1":
        print(promt_for_BMI())
        print("For Table: "+ "BMI")
        data = get_database_data("BMI")
        print_database_data(data)
        return True
    if choice == "2":
        print(prompt_for_retirement_age())
        return True
    if choice == "3":
        print(prompt_for_email_verifier())
        print("For Table: "+ "EmailVerifier")
        data = get_database_data("EmailVerifier")
        print_database_data(data)
        return True
    if choice == "4":
        print(prompt_for_split_tip())
        return True
    if choice == "5":
        return False

loop = print_menu(True)

while loop:
    loop = print_menu(False)
