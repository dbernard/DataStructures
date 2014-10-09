# Problem: Given tuples in the form (a, 1, 5) where first element is ID, send
# and 3rd are integers, and 2nd is always < 3rd - break them up into two
# 2-element tuples (i.e. (a, 1) & (a, 5)) and sort them.

def SplitTuples(arr):
    first, second = [], []
    for element in arr:
        first.append((element[0], element[1]))
        second.append((element[0], element[2]))

    # 'first' is already sorted. Sort second for easier merging.
    second = sorted(second, key=lambda s:s[1])

    return first, second

def SortTuples(arr):
    sorted = []
    first, second = SplitTuples(arr)

    while len(first) != 0:
        if first[0][1] <= second[0][1]:
            sorted.append(first.pop(0))
        else:
            sorted.append(second.pop(0))

    # There will ALWAYS be at least one element left in the 'second' array
    sorted.extend(second)

    return sorted

if __name__ == '__main__':
    arr = [('a', 1, 5),
           ('b', 2, 4),
           ('c', 7, 8)]

    sorted = SortTuples(arr)

    print sorted

