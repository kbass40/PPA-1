from BMI import *
import pytest

def test_BMI_feet_input():
    x = 1
    y = 1
    z = 1
    res = BMI(x,y,z)
    assert res == y, "Test Failed"

def test_BMI2():
    x = 1
    y = 1
    z = 1
    res = BMI(x,y,z)
    assert res == z, "Test Failed"
