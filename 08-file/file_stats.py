def file_stats(filename):
    """
    Read a file from `filename` and calculate its statistics.
    This function returns a dictionary containing these keys and values:

    - line_count:
        number of lines in the file.
    - char_count:
        number of characters in the file.
    - average_char_per_line:
        average number of characters per line.

    >>> import tempfile
    >>> with tempfile.NamedTemporaryFile("w+", delete=False) as f:
    ...     f.writelines(["Wow\\n", "file IO\\n", "is\\n", "so easy!"])
    ...     filename = f.name
    >>> res = file_stats(filename)
    >>> res["line_count"]
    4
    >>> res["char_count"]
    23
    >>> print(f"{res['average_char_per_line']:.1f}")
    5.8
    >>> import os
    >>> os.remove(filename)
    """


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
