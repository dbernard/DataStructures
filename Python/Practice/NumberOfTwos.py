# Find the number of twos between 0 and n (inclusive)

def NumberOfTwos(num):
    sum = 0
    for i in range(num + 1):
        # Only check if its even, to cut down checks
        check = list(str(i))
        sum += check.count('2')

    return sum

if __name__ == '__main__':
    num = 25
    print 'Number of twos: %s' % NumberOfTwos(num)

