from SplitTip import *
import pytest

def test_SplitTip_totalAmount_raises_exception_on_non_float_args_for_str():
    with pytest.raises(TypeError):
        SplitTip("total amount",5)

def test_SplitTip_totalAmount_raises_exception_on_non_float_args_for_int():
    with pytest.raises(TypeError):
        SplitTip(5,5)

def test_SplitTip_totalAmount_raises_exception_on_non_float_args_for_None():
    with pytest.raises(TypeError):
        SplitTip(None,5)

def test_SplitTip_numberOfGuest_raises_exception_on_non_int_args_for_str():
    with pytest.raises(TypeError):
        SplitTip(5.5,"total amount")

def test_SplitTip_numberOfGuest_raises_exception_on_non_int_args_for_float():
    with pytest.raises(TypeError):
        SplitTip(5.5,5.5)

def test_SplitTip_numberOfGuest_raises_exception_on_non_int_args_for_None():
    with pytest.raises(TypeError):
        SplitTip(5.5,None)

def test_SplitTip_totalAmount_raises_exception_on_negative_int_args():
    with pytest.raises(RuntimeError):
        SplitTip(-45.50,5)

def test_SplitTip_numberOfGuest_raises_exception_on_negative_int_args():
    with pytest.raises(RuntimeError):
        SplitTip(45.50,-5)

def test_SplitTip_numberOfGuest_raises_exception_on_zero_int_args():
    with pytest.raises(RuntimeError):
        SplitTip(45.50,0)

def test_calculate_total_with_tip():
    assert calculate_total_with_tip(10,.15) == 1150

def test_get_left_over_cents1():
    assert get_left_over_cents(1150,3) == 1  

def test_get_left_over_cents2():
    assert get_left_over_cents(1150,5) == 0

def test_get_distributed_values_without_left_over_cents():
    assert get_distributed_values_without_left_over_cents(1515, 3) == [5.05,5.05,5.05]

def test_get_distributed_values():
    assert get_distributed_values([5.05,5.05,5.05], 1) == [5.06,5.05,5.05]

def test_make_return_string():
    assert make_return_string([5.06,5.05,5.05]) == "Guest1-5.06, Guest2-5.05, Guest3-5.05"