def fizzbuzz(n):
    """
    Print numbers from 1 to `n`.
    For multiples of 3, print "fizz" instead of the number.
    For multiples of 5, print "buzz" instead of the number.
    For multiples of both 3 and 5, print "fizzbuzz" instead of the number.

    >>> fizzbuzz(3)
    1
    2
    fizz
    >>> fizzbuzz(15)
    1
    2
    fizz
    4
    buzz
    fizz
    7
    8
    fizz
    buzz
    11
    fizz
    13
    14
    fizzbuzz
    """


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
