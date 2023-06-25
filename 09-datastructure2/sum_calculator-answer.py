def sum_args(*args, **kwargs):
    """
    Calculate the sum of the numbers given as arguments. If there are string in
    the arguments, look it up from `kwargs` and use the value corresponding to the
    name provided as string.

    >>> sum_args(1, 2, 3)
    6
    >>> sum_args(1, 2, "a", "b", a=1, b=3)
    7
    >>> sum_args("x", "y", x=1, y=2)
    3
    """
    res = 0
    for arg in args:
        if type(arg) == str:
            res += kwargs[arg]
        else:
            res += arg
    return res


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
