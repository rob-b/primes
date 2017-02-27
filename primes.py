# coding=utf-8
import itertools

def is_prime(n):
    is_ = True
    for i in xrange(2, n):
        if n % i == 0:
            is_ = False
            break
    return is_


def primes_for(n):
    seen = 0
    candidates = itertools.count(2)
    results = []
    while n > seen:
        x = candidates.next()
        if is_prime(x):
            results.append(x)
            seen += 1
    return results


def main():
    print("hi")


if __name__ == "__main__":
    main()
