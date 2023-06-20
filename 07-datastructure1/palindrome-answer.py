import copy


def palindrome_check(ls):
    """
    Check if `ls` is a palindrome or not. Return `True` if ls is same when reversed,
    otherwise return `False`.

    >>> palindrome_check([0, 1, 2])
    False
    >>> palindrome_check([0, 1, 0])
    True
    >>> palindrome_check([1, 2, 3, 2, 1])
    True
    """
    reversed_list = copy.copy(ls)
    reversed_list.reverse()
    return ls == reversed_list
    # Instead of using `reverse`, you can also write for loop:
    # for i in range(len(ls)):
    #     if ls[i] != ls[len(ls) - i - 1]:
    #         return False
    # return True


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
