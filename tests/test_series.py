from math_series.series import fibonacci
from math_series.series import lucas
from math_series.series import sum_series

#test fibonacci series 
def test_fibonacci_zero():
    actual = fibonacci(0) 
    assert  actual == 0


def test_fibonacci_one():
    actual = fibonacci(1) 
    assert  actual == 1


def test_fibonacci_Two():
    actual = fibonacci(2) 
    assert  actual == 1

def test_fibonacci_Three():
    actual = fibonacci(3) 
    assert  actual == 2

def test_fibonacci_four():
    actual = fibonacci(4) 
    assert  actual == 3

def test_fibonacci_five():
    actual = fibonacci(5) 
    assert  actual == 5

def test_fibonacci_six():
    actual = fibonacci(6) 
    assert  actual == 8

def test_fibonacci_sevan():
    actual = fibonacci(7) 
    assert  actual == 13

def test_fibonacci_eight():
    actual = fibonacci(8) 
    assert  actual == 21

#test lucas series 
def test_lucas_one():
    actual = lucas(1) 
    assert  actual == 2

def test_lucas_Two():
    actual = lucas(2) 
    assert  actual == 1

def test_lucas_Three():
    actual = lucas(3) 
    assert  actual == 3

def test_lucas_four():
    actual = lucas(4) 
    assert  actual == 4

def test_lucas_five():
    actual = lucas(5) 
    assert  actual == 7

def test_lucas_six():
    actual = lucas(6) 
    assert  actual == 11

def test_lucas_sevan():
    actual = lucas(7) 
    assert  actual == 18

def test_lucas_eight():
    actual = lucas(8) 
    assert  actual == 29



#test sum series 

def test_sum_series():
    actual = sum_series(8,0,1) #should call fibonacci
    assert  actual == 21

def test_sum_series():
    actual = sum_series(8,2,1) #should call lucas
    assert  actual == 29


def test_sum_series():
    actual = sum_series(8,4,5) #should call new series
    assert  actual == 97
# 4,5,9,14,23,37,60, 97