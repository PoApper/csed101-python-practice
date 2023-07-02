def newton_method(x, iteration_count):
    """
    In numerical analysis, Newton's method is an algorithm for calculating
    roots of polynomial equation. In this problem, you will implement it to
    calculate square root of given number, `x`.

    Suppose that you are using Newton's method in order to find a root of a
    polynomial equation, "f(t) = 0". First we set x as some starting value,
    and set t as "t - f(t) / f'(t)" continuously. In this case, we are solving
    the equation "t^2 - x = 0" with respect to t, so t should be set as
    "t / 2 + x / (2t)" in each iteration of the loop. Use `x` as starting value
    and run the loop `iteration_count` times.

    >>> print(f"{newton_method(2, 1000):.3f}")
    1.414
    >>> print(f"{newton_method(3, 1000):.3f}")
    1.732
    >>> print(f"{newton_method(5, 1000):.3f}")
    2.236
    """
    t = x
    for _ in range(iteration_count):
        t = t / 2 + x / (2 * t)
    return t


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
