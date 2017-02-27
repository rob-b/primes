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
    is_ = True
    for i in xrange(5, n):
        if n % i == 0:
            is_ = False
            break
    return is_


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
    print(primes_for(int(n)))


if __name__ == "__main__":
    main()
