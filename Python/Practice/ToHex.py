def ToHex(num):
    result = []
    while num > 0:
        base = num % 16
        if base < 10:
            result.append(str(base))
        else:
            ch = ord('a') + (base - 10)
            result.append(chr(ch))
        num /= 16

    return ''.join(result)[::-1]


if __name__ == '__main__':
    num = 1
    print '%s -> %s' % (num, ToHex(num))

    num = 100
    print '%s -> %s' % (num, ToHex(num))

    num = 190148
    print '%s -> %s' % (num, ToHex(num))

    num = 999
    print '%s -> %s' % (num, ToHex(num))

    num = 3735928559
    print '%s -> %s' % (num, ToHex(num))

