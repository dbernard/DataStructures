# Find and return the second largest value in an array in O(n) time.

def SecondLargest(arr):
    # Case where we have an array too short to fulfill the requrements
    if len(arr) <= 1:
        return None

    top_two = []
    # O(n) time by not sorting, iterating over array once
    # Ignores duplicates in result
    for val in arr:
        # If we haven't fully populated two_two AND the current value isn't
        # already in our top_two
        if len(top_two) < 2 and not val in top_two:
            top_two.append(val)
        else:
            top_min = min(top_two)
            if val > top_min and val != max(top_two):
                replace = top_two.index(top_min)
                top_two[replace] = val

    if len(top_two) < 2:
        return None

    return min(top_two)


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 4]
    result = SecondLargest(arr)

    print 'Second largest is %s.' % result

