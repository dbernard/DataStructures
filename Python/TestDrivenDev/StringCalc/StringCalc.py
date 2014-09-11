# TDD: String Calculator that can take 0, 1 or 2 numbers and return their sum.
import re

def stringcalc(s):
    ints = re.split(',|\n', s)

    if len(ints) == 1:
        if not ints[0]:
            return 0

        return int(ints[0])

    sum = 0
    for i in ints:
        sum += int(i)

    return sum

