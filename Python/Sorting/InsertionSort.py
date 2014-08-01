# Implementation of an Insertion Sort. This algorithms has a time complexity of
# O(n^2) (quadratic)
import random

def insertion_sort(arr):
    for i in range(1, len(arr)):
        ptr = arr[i]
        j = i

        while (j > 0) and (ptr < arr[j-1]):
            arr[j] = arr[j-1]
            j -= 1

        arr[j] = ptr
        print arr

    return arr


if __name__ == '__main__':
    arr = [i for i in range(10)]
    random.shuffle(arr)

    print 'Starting Array: %s' % arr
    arr = insertion_sort(arr)
    print 'FINAL RESULT: %s' % arr

