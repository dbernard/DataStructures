# TDD: String Calculator that can take 0, 1 or 2 numbers and return their sum.
import re


class NegativesNotAllowed(Exception):
    pass


def stringcalc(s):
    delim = ',|\n'

    # Custom delimiter - split the new delim argument off of the string, use it
    # to break up the rest of the string.
    if s.startswith('//'):
        s = s.strip('//')
        custom = s.split('\n')
        delim = custom[0]
        s = custom[1]

    ints = re.split(delim, s)

    if len(ints) == 1:
        if not ints[0] or int(ints[0]) > 1000:
            return 0
        if int(ints[0]) < 0:
            raise NegativesNotAllowed('Negatives not allowed: %s' %
                                        ', '.join(ints))

        return int(ints[0])

    sum = 0
    negatives = []
    for i in ints:
        # Numbers greater than 1000 should be ignored.
        if int(i) <= 1000:
            sum += int(i)
        if int(i) < 0:
            negatives.append(i)

    if negatives:
        raise NegativesNotAllowed('Negatives not allowed: %s' %
                                        ', '.join(negatives))

    return sum

