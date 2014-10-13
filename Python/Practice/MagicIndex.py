# Design an algorithm to find the index where A[i] == i in a sorted array of
# distinct integers.

def MagicIndex(arr, start, end):
    # If we have not or can not find a magic index, return None
    if end < start or start < 0 or end >= len(arr):
        return None

    # Get the middle index of the array (binary search)
    mid = (start + end) / 2

    # If value at mid is equal to mid (index), return it.
    if arr[mid] == mid:
        return mid

    # Compare mid index to the value at the index. If value at index is greater
    # than index, check lower half, if value at index is less than index, check
    # greater half.
    elif arr[mid] > mid:
        return MagicIndex(arr, start, mid - 1)

    elif arr[mid] < mid:
        return MagicIndex(arr, mid + 1, end)

