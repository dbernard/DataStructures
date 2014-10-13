# Compute the Nth fibonacci number. Allow for multiple requests.

def nth_fib(ns):
    # Catch empty input
    if not ns:
        return []

    # Record the fib numbers as we calculate them so we won't always need to
    # recalculate.
    fibs = []
    for i in range(max(ns)):
        # Calc and store each fib number up to the max value in 'ns'
        # fib numbers are the sum of the previous two values
        if len(fibs) < 2:
            fibs.append(i)
        else:
            fibs.append(fibs[i-2] + fibs[i-1])

    # Acually get the fib numbers
    results = []
    for n in ns:
        results.append(fibs[n-1])

    return results

