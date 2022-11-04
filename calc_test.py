from calculator import *

# Testing add_in_string method
def test_add_in_string():


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
    ts_10 = "5^7^39384"
    assert calc(ts_1) == ["1", "2"]
    assert calc(ts_2) == ["0", "0"]
    assert calc(ts_3) == ["100", "100", "1001"]
    assert calc(ts_4) == ["3", "3", "1"]
    assert calc(ts_5) == ["0", "4", "0", "180", "1"]
    assert calc(ts_6) == ["8", "2", "4", "4"]
    assert calc(ts_7) == ['-1', '2', '-3', '-1000', '0', '3']
    assert calc(ts_8) == ['3', '3', '3', '3', '3', '3', '-3', '-3', '-3']
    assert calc(ts_9) == ['1', '2', '3']
    assert calc(ts_10) == ['5', '7', '39384']



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
    assert(3+4-1.) == "Invalid: Can only have integers"
    assert(.) == "Invalid: Can only have integers"
    assert(+3+4^2) == "Invalid: Can only have number or \"-\" at beginning of expression"
    assert(5*3+) == "Invalid: Cannot end expression with an operator"
    assert(4&5-2) == "Invalid: Contains invalid character: \"" + eq[i] + "\""
    assert(3*4+++2) == "Invalid: can't have more than three operators in a row"
    assert(5+9-2+*)) == "Invalid: can't have more than three operators in a row"
    assert(8+9**2) == "Invalid: can't have duplicate \"*\" operators in a row"
    assert(3+++) == "Invalid: can't have more than three \"" + eq[i] + "\" operators in a row"
    assert(5---) == "Invalid: can't have more than three \"" + eq[i] + "\" operators in a row"
    # Testing valid inputs
    assert(4+3*4-1) == "!4+3*4-1"
    assert(21/3) == "!21/3"
    assert(2^3) == "!2^3"
    assert(9++) == "!9++"
    assert(3--) == "!3--"


# Testing sep method
def test_sep():
    assert(10/2) == "5"
    assert(4*2-3+5) == "10"
    assert((2+3)-1) == "4"
    assert(3^2) == "9"
    assert(3+(4^2)) = "19"
    assert(3/0) == "Invalid: Division by zero"
    