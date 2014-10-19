# Given multiple sorted lists, find the smallest range that includes at least
# one element from each list.

def GetRange(lists):
    mins = []
    for k in lists:
        mins.append(k[0])
    return (min(mins), max(mins))


def SmallestRange(lists, minrange=None):
    # If any of our range have been exhausted to a single element, we should be
    # done.
    if not all(len(x) > 0 for x in lists):
        return minrange

    if not minrange:
        minrange = GetRange(lists)
    else:
        new_range = GetRange(lists)
        if new_range[1] - new_range[0] < minrange[1] - minrange[0]:
            minrange = new_range

    # Remove the smallest value
    min = lists[0][0]
    for k in lists:
        if k[0] <= min:
            to_pop = k

    to_pop.pop(0)

    return SmallestRange(lists, minrange)

if __name__ == '__main__':
    a = [4, 10, 15, 24, 26]
    b = [0, 9, 12, 20]
    c = [5, 18, 22, 30]

    range = SmallestRange([a, b, c])
    print range

