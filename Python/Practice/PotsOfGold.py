# Pots of gold game: Player A and B take turns choosing a pot of gold from
# either end of a line. The goal is to maximize the number of gold coins (for
# player A) by the end of the game, assuming player B will also play optimally.

def max_pot(pots, start, end):
    if start > end:
        return 0

    a = pots[start] + min(max_pot(pots, start+2, end),
                          max_pot(pots, start+1, end-1))

    b = pots[end] + min(max_pot(pots, start+1, end-1),
                        max_pot(pots, start, end-2))

    return max(a, b)

if __name__ == '__main__':
    pots = [1, 2, 5, 3, 7, 3, 7, 2, 4, 9, 2, 4, 5]
    result = max_pot(pots, 0, len(pots)-1)
    print result

