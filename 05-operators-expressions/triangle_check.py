def triangle_check(a, b, c):
    """
    Given three lengths `a`, `b`, `c`, return True if a triangle can be formed
    using those lengths. Otherwise, return False.

    >>> triangle_check(1, 1, 1)
    True
    >>> triangle_check(1, 2, 1)
    False
    >>> triangle_check(1, 2, 3)
    False
    >>> triangle_check(2, 2, 3)
    True
    """


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
