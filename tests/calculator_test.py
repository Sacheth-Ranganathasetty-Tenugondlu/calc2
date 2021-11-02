"""Testing the Calculator"""
from calculator.main import Calculator

def test_calculator_result():
    """testing calculator result is 0"""
    calc = Calculator()
    assert calc.result == 0

def test_calculator_add():
    """Testing the Add function of the calculator"""
    #Arrange by instantiating the calc class
    calc = Calculator()
    #Act by calling the method to be tested
    calc.add_number(4)
    #Assert that the results are correct
    assert calc.result == 4

def test_calculator_get_result():
    """Testing the Get result method of the calculator"""
    calc = Calculator()
    assert calc.get_result() == 0

def test_calculator_subtract():
    """Testing the subtract method of the calculator"""
    calc = Calculator()
    calc.subtract_number(1)
    assert calc.get_result() == -1
def test_calculator_multiply():
    """ tests multiplication of two numbers"""
    calc = Calculator()
    result  = calc.multiply_numbers(1,2)
    assert result == 2
def test_calculator_division():
    """ Testing division of two numbers"""
    # Arrange
    value_a = 1
    value_b = 1
    # Act
    result = Calculator.divide_numbers(value_a, value_b)
    # Assert
    assert result == 1

def test_calculator_division_exception():
    """ Testing division exception for division by zero"""
    # Arrange
    value_a = 1
    value_b = 0
    # Act
    with pytest.raises(ZeroDivisionError):
        Calculator.divide_numbers(value_a, value_b)
