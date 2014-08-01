# Implementation of a Selection Sort. This algorithm has a time complexity of
# O(n^2).
import random

def selection_sort(arr):
    for i in range(len(arr)):
        min = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min]:
                # change the index of the min to the new min
                min = j

        if min != i:
            # Record the values-to-be-changed
            old_min = arr[i]
            new_min = arr[min]
            # Swap them
            arr[i] = new_min
            arr[min] = old_min

            print 'Swapping %s and %s: %s' % (old_min, new_min, arr)

    return arr

if __name__ == '__main__':
    arr = [i for i in range(10)]
    random.shuffle(arr)

    print 'Starting Array: %s' % arr
    sorted = selection_sort(arr)
    print 'FINAL RESULT: %s' % sorted

