# Implement Bubble Sort. This algorithm has a worst case time complexity of
# O(n^2) (quadratic performance).
import random

def bubblesort(arr):
    while True:
        swapped = False

        for i in range(1, len(arr)):
            if arr[i-1] > arr[i]:
                # Store values from the to-be-swapped positions
                first = arr[i-1]
                second = arr[i]
                # Swap the values
                arr[i] = first
                arr[i-1] = second
                print 'Swapping %s and %s: %s' % (arr[i-1], arr[i], arr)
                # Flag that we needed to swap this iteration
                swapped = True

        if not swapped:
            break

    return arr


if __name__ == '__main__':
    arr = [i for i in range(10)]
    random.shuffle(arr)

    print 'Starting Array: %s' % arr
    sorted = bubblesort(arr)
    print 'FINAL RESULT: %s' % sorted

