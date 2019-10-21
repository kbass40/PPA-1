# This module tests the http api functionality of our program

import requests
import pytest
import werkzeug
from database import readBMI, readEmailVerifier, TestDBConnection
from BMI import postBMI, get_timestamp
from EmailVerifier import postEmailVerification
from pytest_mock import mocker
import flask_app

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

def test_GET_EMAIL():
    mockedDB = TestDBConnection()
    time_stamp = get_timestamp()
    confirmation = {1: {'Timestamp': time_stamp, "Input Email" : 'danil_kyle@rocketmail.com', "Valid" : 'TRUE',}}
    
    mockedDB.insert_into_Email_Verifier(time_stamp, 'danil_kyle@rocketmail.com', 'TRUE')
    json = readEmailVerifier(mockedDB)

    assert json == confirmation

def test_GET_EMAIL_gets_all_entries():
    mockedDB = TestDBConnection()
    time_stamp1 = get_timestamp()
    time_stamp2 = get_timestamp()
    time_stamp3 = get_timestamp()
    email1 = 'this'
    email2 = 'is'
    email3 = 'atest@ufl.edu'
    confirmation = {1: {'Timestamp': time_stamp1, "Input Email" : email1, "Valid" : 'FALSE',}}
    confirmation[2] = {'Timestamp': time_stamp2, "Input Email" : email2, "Valid" : 'FALSE',}
    confirmation[3] = {'Timestamp': time_stamp3, "Input Email" : email3, "Valid" : 'TRUE',}
    
    mockedDB.insert_into_Email_Verifier(time_stamp1, email1, 'FALSE')
    mockedDB.insert_into_Email_Verifier(time_stamp2, email2, 'FALSE')
    mockedDB.insert_into_Email_Verifier(time_stamp3, email3, 'TRUE')
    json = readEmailVerifier(mockedDB)

    assert json == confirmation

def test_mock_get_bmi(mocker):
    mocker.patch.object(flask_app, 'get_bmi')
    flask_app.get_bmi()
    flask_app.get_bmi.assert_called_once()

def test_mock_get_email(mocker):
    mocker.patch.object(flask_app, 'get_email')
    flask_app.get_email()
    flask_app.get_email.assert_called_once()
