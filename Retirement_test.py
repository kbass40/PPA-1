from Retirement import *
import pytest

def test_Retirement_age_raises_exception_on_non_int_args():
    with pytest.raises(TypeError):
        Retirement("age",45000,5000,50000)
        Retirement(12.2,45000,5000,50000)
        Retirement('5',45000,5000,50000)
        Retirement(None,45000,5000,50000)

def test_Retirement_salary_raises_exception_on_non_int_args():
    with pytest.raises(TypeError):
        Retirement(32,'salary',5000,50000)
        Retirement(32,45000.24,5000,50000)
        Retirement(32,'4',5000,50000)
        Retirement(32,None,5000,50000)

def test_Retirement_saved_raises_exception_on_non_float_args():
    with pytest.raises(TypeError):
        Retirement(32,45000,'annual salary',50000)
        Retirement(32,45000,5000,50000)
        Retirement(32,45000,'5',50000)
        Retirement(32,45000,None,50000)

def test_Retirement_goal_raises_exception_on_non_int_args():
    with pytest.raises(TypeError):
        Retirement(32,45000,5000.0,'goal')
        Retirement(32,45000,5000.0,50000.25)
        Retirement(32,45000,5000.0,'5')
        Retirement(32,45000,5000.0,None)