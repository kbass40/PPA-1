from EmailVerifier import *
import pytest

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