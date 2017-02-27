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
    msg = u'Usage: {} n (where n is number of prime numbers)'
    return msg.format(os.path.basename(progname))


def main():
    if len(sys.argv) != 2:
        sys.exit(usage(sys.argv[0]))

    try:
        n = int(sys.argv[1])
    except (ValueError, TypeError):
        sys.exit(usage(sys.argv[0]))

    primes = primes_for(n)
    multiplied = matrix(primes)
    for row in draw_matrix(multiplied):
        print(row)


if __name__ == "__main__":
    main()
