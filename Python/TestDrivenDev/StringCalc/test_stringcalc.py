from StringCalc import stringcalc, NegativesNotAllowed

from nose.tools import *

def test_empty():
    eq_(0, stringcalc(''))

def test_oneValue():
    eq_(1, stringcalc('1'))
    eq_(2, stringcalc('2'))
    eq_(10, stringcalc('10'))

def test_twoValues():
    eq_(1, stringcalc('0,1'))
    eq_(3, stringcalc('1,2'))
    eq_(2, stringcalc('1,1'))
    eq_(100, stringcalc('50,50'))

def test_newLine():
    eq_(1, stringcalc('0\n1'))
    eq_(6, stringcalc('1\n2,3'))

def test_customDelimeter():
    eq_(3, stringcalc('//;\n1;2'))

def test_NegsNotAllowedError():
    try:
        stringcalc('-1')
        raise AssertionError
    except NegativesNotAllowed, nne:
        eq_(str(nne), 'Negatives not allowed: -1')

def test_ignoreNumsOverOneThousand():
    eq_(1001, stringcalc('1,1000'))
    eq_(1, stringcalc('1,1001'))
    eq_(0, stringcalc('1001'))

