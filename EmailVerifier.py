# This module runs EmailVerifier 
import re

from database import *
from flask import abort
import datetime 

'''
Email Verifier - Input a string, determine if it is a valid email address (i.e., some_string ‘@’ domain)
according to these stated requirements with required caveats. some_string1 can consist of text,
optionally separated by periods. No periods can start or end some_string1. Two periods together is
invalid and the address must start with a non-numeric character. some_string1 can contain the following
printable characters: !$%*+-=?^_{|}~ but not: "(),:;<>@[\]` (this function provides a good opportunity
to use regular expressions).
'''

def Verify(email, db=None):
    if db == None:
        db = DBConnection()

    ret = EmailVerifier(email)

    out = ""

    if ret == "Email is valid":
        out = "TRUE"
    else:
        out = "FALSE"

    # Log function use in database
    insert_into_database(db, email, out)

    return ret

def EmailVerifier(email):
    # First, verify that the data inputted is of the correct type
    if not isinstance(email,str):
        raise TypeError('Argument email must be passed as a string')

    # Next we test if the data makes sense given the domain
    match = re.match('^[A-Z_a-z!$%*+\-=?^_{|}~ ][A-Z_a-z0-9!$%*+\-=?^_{|}~]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email)
    
    ret = ""

    if match == None: 
        ret = 'Email is not valid' 
    else: 
        ret = 'Email is valid'

    return ret

def postEmailVerification(email, debug=False):
    if debug:
        db = TestDBConnection()
    else:
        db = DBConnection()
    try:
        ret = Verify(email, db)
        return 201, ret
    except:
        abort(404, "Parameters were not correct")

def insert_into_database(db, inpt, output):
    db.insert_into_Email_Verifier(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),inpt, output)
