from database import DBConnection as db
from database import TestDBConnection
import pytest
from pytest_mock import mocker
import datetime

def test_mock_database(mocker):
    mocker.patch.object(db, 'get_connection')
    db.get_connection()
    db.get_connection.assert_called_once()

# faking the database
def test_email_database1():
    fakedb = TestDBConnection()
    fakedb.insert_into_Email_Verifier("fake date", "test@test.com", "TRUE")
    insert = fakedb.get_email()
    assert insert[0] == ("fake date", "test@test.com", "TRUE")

def test_email_database2():
    fakedb = TestDBConnection()
    fakedb.insert_into_Email_Verifier("fake date", "test@test.com", "TRUE")
    fakedb.insert_into_Email_Verifier(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), "test@test.com", "TRUE")
    insert = fakedb.get_email()
    assert len(insert) == 2

# faking the database
def test_bmi_databse1():
    fakedb = TestDBConnection()
    fakedb.insert_into_BMI("fake date", "5", "5", "150", "Overweight")
    insert = fakedb.get_bmi()
    assert insert[0] == ("fake date", "5", "5", "150", "Overweight")

def test_bmi_database2():
    fakedb = TestDBConnection()
    fakedb.insert_into_BMI("fake date", "5", "5", "150", "Overweight")
    fakedb.insert_into_BMI(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), "6", "5", "180", "Normal weight")
    insert = fakedb.get_bmi()
    assert len(insert) == 2

def print_db():
    data = db('user','password')
    data.print_db()