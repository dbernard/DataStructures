from FizzBuzz import FizzBuzz

from nose.tools import *

def test_normal():
    eq_('1', FizzBuzz(1))
    eq_('2', FizzBuzz(2))
    eq_('4', FizzBuzz(4))
    eq_('7', FizzBuzz(7))

def test_multipleOfThree():
    eq_('Fizz', FizzBuzz(3))

def test_multipleOfFive():
    eq_('Buzz', FizzBuzz(5))

def test_multipleOfFiveAndThree():
    eq_('FizzBuzz', FizzBuzz(15))


