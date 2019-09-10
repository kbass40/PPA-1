from Retirement import *
import pytest

def test_Retirement_age_raises_exception_on_non_int_args():
    with pytest.raises(TypeError):
        Retirement("age",45000,5.0,50000)
        Retirement(12.2,45000,5.0,50000)
        Retirement('5',45000,5.0,50000)
        Retirement(None,45000,5.0,50000)

def test_Retirement_age_raises_exception_on_bad_int_args():
    with pytest.raises(RuntimeError):
        Retirement(0,45000,5.0,50000)
        Retirement(-45,45000,5.0,50000)
        Retirement(13,45000,5.0,50000)
        Retirement(100,45000,5.0,50000)

def test_Retirement_salary_raises_exception_on_non_int_args():
    with pytest.raises(TypeError):
        Retirement(32,'salary',5.0,50000)
        Retirement(32,45000.24,5.0,50000)
        Retirement(32,'4',5.0,50000)
        Retirement(32,None,5.0,50000)

def test_Retirement_salary_raises_exception_on_bad_int_args():
    with pytest.raises(RuntimeError):
        Retirement(32,-1000,5.0,50000)
        Retirement(32,0,5.0,50000)

def test_Retirement_saved_raises_exception_on_non_float_args():
    with pytest.raises(TypeError):
        Retirement(32,45000,'annual salary',50000)
        Retirement(32,45000,5000,50000)
        Retirement(32,45000,'5',50000)
        Retirement(32,45000,None,50000)

def test_Retirement_saved_raises_exception_on_bad_float_args():
    with pytest.raises(RuntimeError):
        Retirement(32,45000,-15.2,50000)
        Retirement(32,45000,101.5,50000)

def test_Retirement_goal_raises_exception_on_non_int_args():
    with pytest.raises(TypeError):
        Retirement(32,45000,5.0,'goal')
        Retirement(32,45000,5.0,50000.25)
        Retirement(32,45000,5.0,'5')
        Retirement(32,45000,5.0,None)

def test_Retirement_goal_raises_exception_on_bad_int_args():
    with pytest.raises(RuntimeError):
        Retirement(32,45000,5.0,-5)
        Retirement(32,45000,5000.0,'goal')
        Retirement(32,45000,5000.0,50000.25)
        Retirement(32,45000,5000.0,'5')
        Retirement(32,45000,5000.0,None)

def test_Retirement_returns_string_argument():
    assert isinstance(Retirement(32,45000,5.0,500000),str),'Test Failed: Function must return a string'
        
def test_total_saved_per_year():
        assert total_saved_per_year(100, 20) == 27

def test_years_until_retirement1():
        years = years_until_retirement(10000, 100000)
        assert years == 10

def test_years_until_retirement2():
        years = years_until_retirement(125000, 5555000)
        assert years == 45

def test_age_of_retirement1():
        age = age_of_retirement(50,15)
        assert age == 65

def test_age_of_retirement2():
        age = age_of_retirement(50,60)
        assert age == -1