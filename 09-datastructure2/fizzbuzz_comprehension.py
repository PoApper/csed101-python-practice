def fizzbuzz(n):
    """
    Given an integer `n`, create a list of numbers and strings whose length is n
    where i'th element is:
    - "fizzbuzz" if (i + 1) is divisible by 3 and 5.
    - "fizz" if (i + 1) is divisible by 3.
    - "buzz" if (i + 1) is divisible by 5.
    - i + 1 if otherwise. (as number)

    Use list comprehensions instead of explicit loops.

    >>> fizzbuzz(0)
    []
    >>> fizzbuzz(3)
    [1, 2, 'fizz']
    >>> fizzbuzz(10)
    [1, 2, 'fizz', 4, 'buzz', 'fizz', 7, 8, 'fizz', 'buzz']
    """


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
