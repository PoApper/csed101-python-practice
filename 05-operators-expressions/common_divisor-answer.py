def common_divisor_check(a, b, d):
    """
    Return True if `d` is a common divisor of `a` and `b` and False otherwise.

    >>> common_divisor_check(4, 6, 2)
    True
    >>> common_divisor_check(7, 5, 2)
    False
    """
    return a % d == 0 and b % d == 0


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
