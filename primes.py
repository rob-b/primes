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


def main():
    print("hi")


if __name__ == "__main__":
    main()
