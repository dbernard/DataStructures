# Implementation of a quicksort algorithm. This algorithm has a worst cast time
# complexity of O(n^2) (quadratic)
import random


def quicksort(arr, start, end):
    if start < end:
        # create a 'pivot'
        pivot = partition(arr, start, end)
        # sort the left and right halves of the pivot recursively
        quicksort(arr, start, pivot-1)
        quicksort(arr, pivot+1, end)

    return arr


def partition(arr, start, end):
    pivot = random.randint(start, end)
    pivot_val = arr[pivot]
    # Move the pivot all the way to the end (out of the way)
    swap(arr, pivot, end)

    # Store an index (starting at 'start' bound) and increment it every time we
    # swap a value lower than the pivot. Swap the pivot to the stored index at
    # the end.
    stored_index = start
    for i in range(start, end):
        if arr[i] < pivot_val:
            swap(arr, i, stored_index)
            stored_index += 1

    swap(arr, stored_index, end)

    # Return the stored index, as it will be the location of the pivot
    return stored_index


def swap(arr, to_swap, target):
    # Swap values at to_swap and target in the array 'arr'
    print '%s --> Swapping %s with %s' % (arr, arr[to_swap], arr[target])
    tmp = arr[to_swap]
    arr[to_swap] = arr[target]
    arr[target] = tmp

    return arr


if __name__ == '__main__':
    arr = [i for i in range(10)]
    random.shuffle(arr)

    print 'Starting Array: %s' % arr
    sorted = quicksort(arr, 0, len(arr)-1)
    print 'FINAL RESULT: %s' % sorted

