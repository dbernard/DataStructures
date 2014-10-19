# Find all pairs of integers within an array that sum to a specified value

def SumToValue(arr, value):
    hash = {}
    pairs = []
    for num in arr:
        if value - num in hash:
            pairs.append([num, value - num])
        if num not in hash:
            hash[num] = True

    return pairs

if __name__ == '__main__':
    arr = [1, 3, 7, 5, 2, 4, 6]

    pairs = SumToValue(arr, 8)

    print 'Pairs: %s' % pairs


