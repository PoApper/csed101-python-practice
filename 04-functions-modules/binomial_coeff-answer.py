def binomial_coefficient(n, k):
    """
    Calculate binomial coefficient nCk, using recursion.
    Hint:
    nCk = (n - 1)C(k - 1) + (n - 1)Ck
    nC0 = 1

    >>> binomial_coefficient(1, 0)
    1
    >>> binomial_coefficient(4, 2)
    6
    >>> binomial_coefficient(4, 3)
    4
    """
    if k == 0:
        return 1
    elif n <= 0 or k < 0:
        return 0
    return binomial_coefficient(n - 1, k - 1) + binomial_coefficient(n - 1, k)


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
