# Implementation of a merge sort algorithm
# Time complexity for this algorithm is O(nlogn) (linearithmic)
import random

def mergesort(arr):
    # Array of single item is considered sorted
    if len(arr) <= 1:
        return arr

    left, right = [], []
    mid = len(arr) / 2
    for i in range(mid):
        left.append(arr[i])

    for i in range(mid, len(arr)):
        right.append(arr[i])

    left = mergesort(left)
    right = mergesort(right)

    # Merge the now-sorted left and right lists
    return merge(left, right)


def merge(arr1, arr2):
    result = []
    print '(left) %s' % arr1
    print '(right) %s' % arr2
    while len(arr1) > 0 or len(arr2) > 0:
        if len(arr1) > 0 and len(arr2) > 0:
            # Compare first elements in arrays
            if arr1[0] <= arr2[0]:
                result.append(arr1.pop(0))
            else:
                result.append(arr2.pop(0))
        # One array is empty, just add the remaining elements to result
        elif len(arr1) > 0:
            result.append(arr1.pop(0))
        elif len(arr2) > 0:
            result.append(arr2.pop(0))

    print '(merged) %s' % result
    print '---------------------'
    return result


if __name__ == '__main__':
    arr = [i for i in range(10)]
    random.shuffle(arr)

    print 'Starting Array: %s' % arr
    final = mergesort(arr)
    print 'FINAL RESULT: %s' % final

