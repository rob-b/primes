import pytest

first_3 = [2, 3, 5]
first_39 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59,
            61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131,
            137, 139, 149, 151, 157, 163, 167, ]


@pytest.mark.parametrize(("x", "expected"), [
    (3, first_3),
    (39, first_39),
])
def test_primes_for(x, expected):
    from primes import primes_for
    assert list(primes_for(x)) == expected


def test_matrix():
    from primes import matrix
    assert matrix(first_3) == [[1, 2, 3, 5],
                               [2, 4, 6, 10],
                               [3, 6, 9, 15],
                               [5, 10, 15, 25]]
