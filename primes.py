# coding=utf-8
import sys
import os.path
import itertools


def is_prime(n):
    if n in [2, 3]:
        return True
    if n % 2 == 0:
        return False
    if n % 3 == 0:
        return False

    poss = 5
    offset = 2
    while n >= poss * poss:
        if n % poss == 0:
            return False
        poss += offset
        offset = 6 - offset
    return True


def draw_matrix(m):
    for row in m:
        yield ' | '.join([unicode(x) if x != 1 else ' ' for x in row])


def matrix(xs):
    """
    |   | 2  | 3  | 5  |
    | 2 | 4  | 6  | 10 |
    | 3 | 6  | 9  | 15 |
    | 5 | 10 | 15 | 25
    """
    xs.insert(0, 1)
    return [[(row * col) for col in xs] for row in xs]


def primes_for(n):
    seen = 1
    candidates = itertools.count(start=1, step=2)
    results = [2]
    while n > seen:
        x = candidates.next()
        if x == 1:
            continue
        if is_prime(x):
            results.append(x)
            seen += 1
    return results


def usage(progname):
    return u'Usage: {} n'.format(os.path.basename(progname))


def main():
    if len(sys.argv) != 2:
        sys.exit(usage(sys.argv[0]))
    n = sys.argv[1]
    primes = primes_for(int(n))

    for row in draw_matrix(matrix(primes)):
        print(row)


if __name__ == "__main__":
    main()
