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
    return min(iterable)

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
    return max(iterable)    

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)