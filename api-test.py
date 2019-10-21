# This module tests the http api functionality of our program

import requests
import pytest
import werkzeug
from database import readBMI, readEmailVerifier
from BMI import postBMI
from EmailVerifier import postEmailVerification

def test_fail_POST_BMI():
    # Should fail due to invalid inches
     with pytest.raises(werkzeug.exceptions.NotFound):
        ret = postBMI(5,12,60.54,True)

def test_POST_BMI():
    ret = postBMI(5,11,60.54,True)
    assert ret == 201
