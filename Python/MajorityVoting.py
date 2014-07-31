#!/ust/bin/python
# This is an implementation of the majority voting algorithm. This algorithm
# returns a value if that value is in the "majority" (if it appears more than
# 50% of the time.
#
# This algorithm's time complexity is O(n) (linear) because each array element
# is accessed only once.

def get_majority(arr):
    counter = 0
    majority = None

    for item in arr:
        if not majority:
            majority = item
            counter += 1
        elif majority == item:
            counter += 1
        elif counter == 0:
            majority = None
        else:
            counter -= 1

        # Print the majority and counter to show traversal
        print '[%s, %s]' % (majority, counter)

    return majority


if __name__ == '__main__':
    # Set us up so 'a' will be our majority
    arr = ['a', 'e', 'a', 'a', 'f', 'a', 'g', 'e', 'a', 'a']
    print 'Majority is: %s\n' % get_majority(arr)

    # Show an example where majority changes throughout the algorithm. Majority
    # should be 1 in the end.
    arr = [1, 2, 4, 9, 1, 1, 3, 3, 3, 3, 1, 1, 1, 6, 1, 1, 1, 1]
    print 'Majority is: %s\n' % get_majority(arr)

