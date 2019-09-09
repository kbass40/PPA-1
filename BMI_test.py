from BMI import *
import pytest

def test_BMI_feet_raises_exception_on_non_int_args():
    with pytest.raises(TypeError):
        BMI("feet",11,15.2)
    
    with pytest.raises(TypeError):
        BMI(122.2,11,15.2)

    with pytest.raises(TypeError):
        BMI('5',1,15.2)

    with pytest.raises(TypeError):
        BMI(None,1,15.2)

def test_BMI_feet_raises_exception_on_bad_int_args():
    with pytest.raises(RuntimeError):
        BMI(-1,11,15.2)
    
    with pytest.raises(RuntimeError):
        BMI(50,11,15.2)

def test_BMI_inches_raises_exception_on_non_int_args():
    with pytest.raises(TypeError):
        BMI(5,"inches",15.2)
    
    with pytest.raises(TypeError):
        BMI(5,15.4,15.2)

    with pytest.raises(TypeError):
        BMI(5,'9',15.2)

    with pytest.raises(TypeError):
        BMI(5,None,15.2)

def test_BMI_inches_raises_exception_on_bad_int_args():
    with pytest.raises(RuntimeError):
        BMI(5,12,15.2)
    
    with pytest.raises(RuntimeError):
        BMI(5,-1,15.2)

def test_BMI_pounds_raises_exception_on_non_float_args():
    with pytest.raises(TypeError):
        BMI(5,9,'Pounds')
    
    with pytest.raises(TypeError):
        BMI(5,9,int(150))

    with pytest.raises(TypeError):
        BMI(5,9,'5')

    with pytest.raises(TypeError):
        BMI(5,9,None)

def test_BMI_pounds_raises_exception_on_bad_float_args():
    with pytest.raises(RuntimeError):
        BMI(5,10,-1.0)
    
    with pytest.raises(RuntimeError):
        BMI(5,0,.0)

def test_BMI_returns_string_argument():
    result = BMI(5,8,150.0)
    assert isinstance(result,str), 'Test Failed: BMI function failed to return a valid string result'

def test_calculate_BMI():
    result = calculate_BMI(5,3,125.0)
    assert round(result,1) == 22.7, 'Test Failed: Incorrect BMI calculated'

def test_classify_BMI1():
    result = classify_BMI(15)
    assert result == "Underweight"

def test_classify_BMI2():
    result = classify_BMI(18.5)
    assert result == "Normal weight"

def test_classify_BMI3():
    result = classify_BMI(29.9)
    assert result == "Overweight"

def test_classify_BMI4():
    result = classify_BMI(30)
    assert result == "Obese"