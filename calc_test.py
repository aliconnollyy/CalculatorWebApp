from calculator import *

# Testing calc method
def test_calc():
    ts_1 = "1+2"
    ts_2 = "0*0"
    ts_3 = "100-100-1001"
    ts_4 = "3*3-1"
    ts_5 = "0+4*0*180+1"
    ts_6 = "8*2-4*4"
    ts_7 = "-1-2*-3+-1000*0+3"
    ts_8 = "3*3*3*3*3*3*-3*-3*-3"
    ts_9 = "1/2/3"
    ts_10 = "5^7^3"
    assert calc(ts_1) == '3'
    assert calc(ts_2) == '0'
    assert calc(ts_3) == '-1001'
    assert calc(ts_4) == '8'
    assert calc(ts_5) == '1'
    assert calc(ts_6) == '0'
    assert calc(ts_7) == '8'
    assert calc(ts_8) == '-19683'
    assert calc(ts_9) == '0.167'
    assert calc(ts_10) == '476837158203125'
    
    assert calc('10/2') == '5.000'
    assert calc('4*2-3+5') == '10'
    assert calc('2+3-1') == '4'
    assert calc('3^2') == '9'
    assert calc('3+4^2') == '19'
    assert calc('9/3-8^2+5') == '-56.000'
    assert calc('3/0') == "Invalid: Division by zero"
    assert calc('20*2/0') == "Invalid: Division by zero"



# Testing sub_calc
def test_sub_calc():
    assert sub_calc(4, 6, "*") == 24
    assert sub_calc(102, 3, "/") == 34
    assert sub_calc(4, 0, "/") == None
    assert sub_calc(4, 6, "-") == -2
    assert sub_calc(4, 6, "+") == 10
    assert sub_calc(4, 6, "^") == 4096



# Testing validate method
def test_validate():
    # Testing invalid inputs
    assert(validate('3+4-1.')) == "Invalid: Cannot end expression with an operator"
    assert(validate('.')) == "Invalid: Cannot end expression with an operator"
    assert(validate('4..5')) == "Invalid: invalid position for decimal point (.)"
    assert(validate('+3+4^2')) == "Invalid: Can only have number or \"-\" at beginning of expression"
    assert(validate('5*3+')) == "Invalid: Cannot end expression with an operator"
    assert(validate('4&5-2')) == "Invalid: Contains invalid character: \"&\""
    assert(validate('3*4+++2')) == "Invalid: can't have more than three operators in a row"
    assert(validate('5+9-2+*)')) == "Invalid: Cannot end expression with an operator"
    assert(validate('8+9**2')) == "Invalid: can't have duplicate \"*\" operators in a row"
    assert(validate('3+++3')) == "Invalid: can't have more than three operators in a row"
    assert(validate('5---98')) == "Invalid: can't have more than three operators in a row"
    # Testing valid inputs
    assert(validate('4+3*4-1')) == "!4+3*4-1"
    assert(validate('21/3')) == "!21/3"
    assert(validate('2^3')) == "!2^3"
    assert(validate('9++8')) == "!9++8"
    assert(validate('3--1')) == "!3--1"
