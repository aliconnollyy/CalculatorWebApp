from calculator import *

def test_calculator():
    assert sub_calc(4, 6, "*") == 24
    assert sub_calc(102, 3, "/") == 34
    assert sub_calc(4, 0, "/") == None
    assert sub_calc(4, 6, "-") == -2
    assert sub_calc(4, 6, "+") == 10
    assert sub_calc(4, 6, "^") == 4096
    
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