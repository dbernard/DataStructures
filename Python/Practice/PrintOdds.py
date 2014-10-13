# Print all odd numbers from 1 to 99

def PrintOdds():
    # This allows us to only touch the values we need, and never need to check
    # whether or not they are odd
    for i in xrange(1, 100, 2):
        # Start at 1, go to 99, step by 2 (odds)
        print i


if __name__ == '__main__':
    PrintOdds()

