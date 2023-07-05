def transpose(mat):
    """
    Calculate a transpose of the given 2D list, `mat`.
    Given a 2D list M consisting of R 1D lists whose sizes are C, a transpose
    of M is a 2D list T, consisting of C 1D lists whose sizes are R. T should
    satisfy M[i][j] = T[j][i], where 0 <= i < R and 0 <= j < C.
    You can assume that all lists in `mat` have same sizes.

    >>> transpose([[1, 2, 3], [4, 5, 6]])
    [[1, 4], [2, 5], [3, 6]]
    >>> transpose([[1, 2], [3, 4]])
    [[1, 3], [2, 4]]
    >>> transpose([[1, 2, 3, 4]])
    [[1], [2], [3], [4]]
    """


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
