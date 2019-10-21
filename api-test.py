# This module tests the http api functionality of our program

import requests
import pytest
import werkzeug
from database import readBMI, readEmailVerifier, TestDBConnection
from BMI import postBMI, get_timestamp
from EmailVerifier import postEmailVerification

def test_fail_POST_BMI():
    # Should fail due to invalid inches
     with pytest.raises(werkzeug.exceptions.NotFound):
        ret = postBMI(5,12,60.54,True)

def test_POST_BMI():
    ret = postBMI(5,11,60.54,True)
    assert ret == 201

def test_GET_BMI():
    mockedDB = TestDBConnection()
    time_stamp = get_timestamp()
    confirmation = {1: {'Timestamp': time_stamp, 'Feet': '1', 'Inches': '2', 'Pounds': '3.33', 'Classification': 'TEST'}}
    
    mockedDB.insert_into_BMI(time_stamp, 1,2,3.33,'TEST')
    json = readBMI(mockedDB)

    assert json == confirmation

def test_GET_BMI_gets_all_entries():
    mockedDB = TestDBConnection()
    time_stamp1 = get_timestamp()
    time_stamp2 = get_timestamp()
    time_stamp3 = get_timestamp()
    confirmation = {1: {'Timestamp': time_stamp1, 'Feet': '1', 'Inches': '2', 'Pounds': '3.33', 'Classification': 'TEST'}}
    confirmation[2] = {'Timestamp': time_stamp2, 'Feet': '4', 'Inches': '5', 'Pounds': '66.67', 'Classification': 'TEST'}
    confirmation[3] = {'Timestamp': time_stamp3, 'Feet': '7', 'Inches': '8', 'Pounds': '999', 'Classification': 'TEST'}
    
    mockedDB.insert_into_BMI(time_stamp1, 1,2,3.33,'TEST')
    mockedDB.insert_into_BMI(time_stamp2, 4,5,66.67,'TEST')
    mockedDB.insert_into_BMI(time_stamp3, 7,8,999,'TEST')
    json = readBMI(mockedDB)

    assert json == confirmation
    
def test_fail_POST_EMAIL_VERIFICATION():
    # Should fail due to invalid inches
     with pytest.raises(werkzeug.exceptions.NotFound):
        ret = postEmailVerification(5,True)

def test_POST_EMAIL_VERIFICATION():
    ret = postEmailVerification("Test@test.com",True)
    assert ret == (201, 'Email is valid')

def test_invalid_POST_EMAIL_VERIFICATION():
    ret = postEmailVerification("Test@test,com",True)
    assert ret == (201, 'Email is not valid')
