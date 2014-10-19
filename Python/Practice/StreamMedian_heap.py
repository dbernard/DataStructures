# Numbers are generated and passed to a method. This method should keep a
# running median of the stream of numbers. Use a heap for this implementation.

import random
import heapq

def StreamMedian(newval, record):
    record.append(newval)
    if len(record) == 1:
        return record[0], record

    # If we have an even number of values
    if len(record) % 2 == 0:
        small = heapq.nsmallest(len(record) / 2, record)
        large = heapq.nlargest(len(record) / 2, record)
        return float(small[-1] + large[-1]) / 2, record

    # If we have an odd number of values
    else:
        small = heapq.nsmallest(len(record) / 2 + 1, record)
        return small[-1], record


if __name__ == '__main__':
    count = 0
    record = []
    limit = random.randint(10, 100)
    while count < limit:
        new = random.randint(0, 1000)
        median, record = StreamMedian(new, record)
        count += 1

    record.sort()
    print 'Size = %s' % limit
    print 'Record = %s' % record
    print 'Median = %s' % median

