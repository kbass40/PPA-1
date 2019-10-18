from EmailVerifier import *
from database import TestDBConnection
import pytest
import datetime

def test_EmailVerifier_email_raises_exception_on_non_str_args():
    with pytest.raises(TypeError):
        EmailVerifier(45)
        EmailVerifier(25.2)
        EmailVerifier(None)

def test_EmailVerifier_returns_str_argument():
    assert isinstance(EmailVerifier('daniel@ufl.edu'),str), 'Test Failed: Function does not return a string'

def test_EmailVerifier_fails_with_consecutive_periods():
    assert 'Email is not valid' == EmailVerifier('..@g.com'), 'Test Failed: Email should not be valid'

def test_EmailVerifier_fails_with_starting_number():
    assert 'Email is not valid' == EmailVerifier('1dog@g.com'), 'Test Failed: Email should not be valid'

def test_EmailVerifier_fails_with_ending_period():
    assert 'Email is not valid' == EmailVerifier('greencat.@g.com'), 'Test Failed: Email should not be valid'

def test_EmailVerifier_fails_with_starting_period():
    assert 'Email is not valid' == EmailVerifier('.gncat@g.com'), 'Test Failed: Email should not be valid'

def test_EmailVerifier_works_with_period_interally():
    assert 'Email is valid' == EmailVerifier('gncat.dog.rat@g.com'), 'Test Failed: Email should be valid'

def test_EmailVerifier_works_with_starting_symbols():
    assert 'Email is valid' == EmailVerifier('$wgMoney@g.com'), 'Test Failed: Email should be valid'

def test_EmailVerifier_works_different_domains():
    assert 'Email is valid' == EmailVerifier('Forrest**!@ufl.udu'), 'Test Failed: Email should be valid'

def test_EmailVerifier_fails_with_invalid_symbols():
    assert 'Email is not valid' == EmailVerifier('Forrest()!@ufl.uwu'), 'Test Failed: Email should not be valid'

def test_EmailVerifier_fails_with_invalid_symbols_in_domain():
    assert 'Email is not valid' == EmailVerifier('ForrestGUMP@uf!l.uwu'), 'Test Failed: Email should not be valid'

def test_EmailVerifier_works_with_basic_email():
    assert 'Email is valid' == EmailVerifier('greenphantom@ufl.edu'), 'Test Failed: Email should be valid'

def test_EmailVerifier_works_with_short_email():
    assert 'Email is valid' == EmailVerifier('tt@ufl.co'), 'Test Failed: Email should be valid'

def test_EmailVerifier_works_with_long_email():
    assert 'Email is valid' == EmailVerifier('PopeyesBestChickenSandwichInTown!123456789@enterprise.comp'), 'Test Failed: Email should be valid'

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