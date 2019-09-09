from Retirement import *
import pytest

def test_Retirement_age_raises_exception_on_non_int_args():
    with pytest.raises(TypeError):
        Retirement("age",45000,5000,5000)