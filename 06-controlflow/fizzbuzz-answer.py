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
    for x in range(1, n + 1):
        if x % 15 == 0:
            print("fizzbuzz")
        elif x % 3 == 0:
            print("fizz")
        elif x % 5 == 0:
            print("buzz")
        else:
            print(x)


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
