# Numbers are generated and passed to a method. This method should keep a
# running median of the stream of numbers.

import random
import bisect

def StreamMedian(newval, record):
    bisect.insort_left(record, newval)
    if len(record) % 2 != 0:
        middle = len(record) / 2
        return record[middle], record
    else:
        m1 = len(record) / 2
        m2 = m1 - 1
        median = (record[m1] + record[m2]) / 2
        return median, record


if __name__ == '__main__':
    count = 0
    record = []
    while count < 10:
        new = random.randint(0, 100)
        median, record = StreamMedian(new, record)
        count += 1

    print 'Record = %s' % record
    print 'Median = %s' % median

