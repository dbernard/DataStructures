# Give you an array which has n integers,it has both positive and negative
# integers.Now you need sort this array in a special way.After that,the negative
# integers should in the front,and the positive integers should in the back. Also
# the relative position should not be changed.
#
# eg. -1 1 3 -2 2 ans: -1 -2 1 3 2.
#
# o(n)time complexity and o(1) space complexity is perfect.

def SignSort(arr):
    result = []
    neg = []
    pos = []
    for i in arr:
        if i <= 0:
            neg.append(i)
        elif i > 0:
            pos.append(i)

    result = neg + pos

    return result

if __name__ == '__main__':
    arr = [-1, 1, 3, -2, 2, -4, 6, -2, 4]

    print 'Initial array:\n%s\n' % arr
    print SignSort(arr)

