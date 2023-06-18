def binomial_coefficient(n, k):
    """
    Calcaulate binomial coefficient nCk, using recursion.
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
    pass


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
