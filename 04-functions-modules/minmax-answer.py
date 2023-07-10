import random


def myMin(iterable):
    """
    >>> myMin([7, 6, 5])
    5
    >>> myMin([3, 2, 5, 7, 8, 90, 5])
    2
    >>> sample = [i for i in range(100)]; \
        random.shuffle(sample); \
        myMin(sample)
    0
    """
    min_value = iterable[0]
    for val in iterable:
        if min_value > val:
            min_value = val
    return min_value


def myMax(iterable):
    """
    >>> myMax([7, 6, 5])
    7
    >>> myMax([3, 2, 5, 7, 8, 90, 5])
    90
    >>> sample = [i for i in range(100)]; \
        random.shuffle(sample); \
        myMax(sample)
    99
    """
    max_value = iterable[0]
    for val in iterable:
        if max_value < val:
            max_value = val
    return max_value


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
