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
    >>> fizzbuzz(20)
    [1, 2, 'fizz', 4, 'buzz', 'fizz', 7, 8, 'fizz', 'buzz', 11, 'fizz', 13, 14, 'fizzbuzz', 16, 17, 'fizz', 19, 'buzz']
    """

    def fizzbuzz_single(x):
        if x % 15 == 0:
            return "fizzbuzz"
        elif x % 3 == 0:
            return "fizz"
        elif x % 5 == 0:
            return "buzz"
        return x

    return [fizzbuzz_single(x) for x in range(1, n + 1)]


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
