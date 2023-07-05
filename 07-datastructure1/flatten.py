def flatten(mat):
    """
    Flatten `mat`, a 2D list into an 1D list.
    Given a 2D list M consisting of R 1D lists whose sizes are C, a flattened
    list of M is a list which has R*C elements, whose elements are [M[0][0],
    M[0][1], ..., M[0][C-1], M[1][0], ..., M[1][C-1], ..., M[R-1][0], ...,
    R[R-1][C-1]].

    >>> flatten([[1, 2], [3, 4]])
    [1, 2, 3, 4]
    >>> flatten([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    [1, 2, 3, 4, 5, 6, 7, 8, 9]
    """


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
