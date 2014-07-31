#!/usr/bin/python
# This is an implementation of the "wiggle problem" - given an array, arrange it
# such that alternate elements are large and small.

def wiggle(arr):
    if len(arr) % 2 == 0:
        index = len(arr) / 2
    else:
        index = (len(arr) + 1) / 2

    arr.sort() # Sort the array for splitting

    sm = arr[:index] # first n entries of sorted array
    lg = arr[index:] # last (up to) n entries of sorted array

    wiggled = []
    while sm:
        wiggled.append(sm.pop(0))
        wiggled.append(lg.pop(0))

    return wiggled


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    new_arr = wiggle(arr)
    print new_arr
