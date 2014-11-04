# Implement an Least Recently Used cache that tracks the three most recently
# used values.
#
# This is linear time - O(n)
from collections import deque
import random

def LruCache(stream):
    cache = deque()
    for val in stream:
        if val in cache:
            cache.remove(val)
            cache.appendleft(val)
        else:
            if len(cache) < 3:
                cache.appendleft(val)
            else:
                cache.pop()
                cache.appendleft(val)
        print '(Value is %s) Cache: %s' % (val, cache)


if __name__ == '__main__':
    stream = []
    for i in xrange(10000):
        stream.append(random.randint(0, 10))

    LruCache(stream)

