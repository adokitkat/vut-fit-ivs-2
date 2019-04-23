from mathematica import Math

def init_test():
    assert str(Math(5)) == "5"
    assert str(Math(0.1326)) == "0.1326"
    assert str(Math(0.9999999999)) == "0.9999999999"
    assert str(Math(-0.42)) == "-0.42"

def simple_op_test():
    assert str(Math(236) + Math(98)) == "334"
    assert str(Math(0.2238) + Math(1.99999)) == "2.22379"
    assert str(Math(236) - Math(98)) == "138"
    assert str(Math(0.2238) - Math(1.99999)) == "-1.77619"
    assert str(Math(236) * Math(98)) == "23128"
    assert str(Math(0.2238) * Math(1.99999)) == "0.447597762"
    assert str(Math(236) / Math(98)) == "2.408163265306122"

def factorial_test():
    assert str(Math(12).factorial()) == "479001600"
    assert str(Math(-10).factorial()) == "Math Error"
    assert str(Math(1).factorial()) == "1"
    assert str(Math(0).factorial()) == "1"

def root_test():
    assert str(Math(16).root()) == "4"
    assert str(Math(512).root(9)) == "2"
    assert str(Math(27).root(-3)) == "0.333333333333333"

def power_test():
    assert str(Math(6) ** Math(10)) == "60466176"
    assert str(Math(-3) ** Math(9)) == "-19683"
    assert str(Math(0) ** Math(80085)) == "0"
    assert str(Math(1.26) ** Math(3)) == "2.000376"

def log_test():
    assert str(Math(2).ln()) == "0.69314718"
    assert str(Math(2).log(10)) == "0.30102999"
    assert str(Math(0.5).log(0.5)) == "1"

if __name__ == '__main__':
    init_test()
    simple_op_test()
    factorial_test()
    root_test()
    power_test()
    log_test()