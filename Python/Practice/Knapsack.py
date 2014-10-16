# Implementation of the NP-complete "Knapsack" problem:
# Given items with various weights and values, find the maximum benefit (value)
# you can attain by placing items in a bag limited by a given capacity.

def knapsack(values, weights, capacity):
    m = [[0] * (capacity + 1) for i in xrange(len(weights) + 1)]

    for i in xrange(1, len(weights) + 1):
        for j in xrange(capacity + 1):
            if weights[i-1] <= j:
                m[i][j] = max(m[i-1][j],
                              m[i-1][j-weights[i-1]] + values[i-1])
            else:
                m[i][j] = m[i-1][j]

    result = []
    w = capacity
    for j in xrange(len(weights), 0, -1):
        added = m[j][w] != m[j-1][w]

        if added:
            result.append(('val = %s' % values[j-1], 'wt = %s' % weights[j-1]))
            w -= weights[j-1]

    return result


if __name__ == '__main__':
    values = [5, 3, 4, 8]
    weights = [3, 2, 1, 6]
    capacity =  5

    result = knapsack(values, weights, capacity)

    print 'values = %s' % values
    print 'weights = %s' % weights
    print 'capacity = %s' % capacity
    print 'result = %s' % result

