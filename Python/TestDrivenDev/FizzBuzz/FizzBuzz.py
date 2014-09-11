# Print values from 1 to 100 - for multiples of 3 print "Fizz", for multiples of
# 5 print "Buzz", for multiples of 3 AND 5 print "FizzBuzz".

def FizzBuzz(val):
    output = ''
    if val % 3 == 0:
        output += 'Fizz'
    if val % 5 == 0:
        output += 'Buzz'
    if not output:
        return str(val)

    return output

def main():
    for i in xrange(100):
        print FizzBuzz(i)

if __name__ == '__main__':
    main()

