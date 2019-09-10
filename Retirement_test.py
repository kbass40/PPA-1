from Retirement import *
import pytest

def test_Retirement_age_raises_exception_on_non_int_args_for_str():
    with pytest.raises(TypeError):
        Retirement("age",45000,5.0,50000)

def test_Retirement_age_raises_exception_on_non_int_args_for_float():
    with pytest.raises(TypeError):
        Retirement(12.2,45000,5.0,50000)

def test_Retirement_age_raises_exception_on_non_int_args_for_None():
    with pytest.raises(TypeError):
        Retirement(None,45000,5.0,50000)

def test_Retirement_age_raises_exception_on_zero_int_args():
    with pytest.raises(RuntimeError):
        Retirement(0,45000,5.0,50000)

def test_Retirement_age_raises_exception_on_negative_int_args():
    with pytest.raises(RuntimeError):
        Retirement(-45,45000,5.0,50000)

def test_Retirement_age_raises_exception_on_too_young_int_args():
    with pytest.raises(RuntimeError):
        Retirement(13,45000,5.0,50000)

def test_Retirement_age_raises_exception_on_too_old_int_args():
    with pytest.raises(RuntimeError):
        Retirement(100,45000,5.0,50000)

def test_Retirement_salary_raises_exception_on_non_int_args_for_str():
    with pytest.raises(TypeError):
        Retirement(32,'salary',5.0,50000)

def test_Retirement_salary_raises_exception_on_non_int_args_for_float():
    with pytest.raises(TypeError):
        Retirement(32,45000.24,5.0,50000)

def test_Retirement_salary_raises_exception_on_non_int_args_for_None():
    with pytest.raises(TypeError):
        Retirement(32,None,5.0,50000)

def test_Retirement_salary_raises_exception_on_negative_int_args():
    with pytest.raises(RuntimeError):
        Retirement(32,-1000,5.0,50000)

def test_Retirement_salary_raises_exception_on_zero_int_args():
    with pytest.raises(RuntimeError):
        Retirement(32,0,5.0,50000)

def test_Retirement_saved_raises_exception_on_non_float_args_for_str():
    with pytest.raises(TypeError):
        Retirement(32,45000,'annual salary',50000)

def test_Retirement_saved_raises_exception_on_non_float_args_for_int():
    with pytest.raises(TypeError):
        Retirement(32,45000,5000,50000)

def test_Retirement_saved_raises_exception_on_non_float_args_for_None():
    with pytest.raises(TypeError):
        Retirement(32,45000,None,50000)

def test_Retirement_saved_raises_exception_on_negative_float_args():
    with pytest.raises(RuntimeError):
        Retirement(32,45000,-15.2,50000)

def test_Retirement_saved_raises_exception_on_over_100_perecent_float_args():
    with pytest.raises(RuntimeError):
        Retirement(32,45000,101.5,50000)

def test_Retirement_saved_raises_exception_on_equal_0_perecent_float_args():
    with pytest.raises(RuntimeError):
        Retirement(32,45000,0.0,50000)

def test_Retirement_goal_raises_exception_on_non_int_args_for_str():
    with pytest.raises(TypeError):
        Retirement(32,45000,5.0,'goal')

def test_Retirement_goal_raises_exception_on_non_int_args_for_float():
    with pytest.raises(TypeError):
        Retirement(32,45000,5.0,50000.25)

def test_Retirement_goal_raises_exception_on_non_int_args_for_None():
    with pytest.raises(TypeError):
        Retirement(32,45000,5.0,None)

def test_Retirement_goal_raises_exception_on_negative_int_args():
    with pytest.raises(RuntimeError):
        Retirement(32,45000,5.0,-5)

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
