def paren_matching(expression):
    """
    Nowadays, most code editors and IDEs[note 1] highlight the matching sets of
    parentheses if the cursor is on one of the parenthesis' position. For
    example, consider this expression:

        x = (a + b) / 2

    If the cursor is on the opening parenthesis before `a`, the closing
    parenthesis after `b` will be highlighted. Also, if the cursor is on the
    closing parenthesis, the opening parenthesis will be highlighted.

    When given an expression in `expression`, for all parentheses pairs,
    determine `(left parenthesis position, right parenthesis position)` and
    return a list of those tuples. The list should be lexicographically ordered
    -- that is, the tuples should be ordered by starting parenthesis
    position.[note 2] You can assume that for all parenthesis, there exists a
    parenthesis that matches.

    >>> paren_matching("x = (a + b) / 2")
    [(4, 10)]
    >>> paren_matching("(a + b) ** 2 == (a ** 2 + b ** 2)") # freshman's dream
    [(0, 6), (16, 32)]

    [note 1]
        In other words, if you are using an editor which does not support basic
        editing functionality like this, you really should consider using an
        editor that is more suitable. (looking at you, notepad coders)

    [note 2]
        In this challenge, you don't have to consider a case of two or more
        tuples having the same left parenthesis position as a parenthesis
        matches with only one parenthesis.
    """
    pos_stack = []
    res = []
    for i in range(len(expression)):
        if expression[i] == "(":
            pos_stack.append(i)
        elif expression[i] == ")":
            res.append((pos_stack.pop(), i))
    # Instead of using `range(len(...))`, `enumerate` can be used.
    # Actually, iterating over lists and strings using `range(len(...))` is
    # generally considered as a bad practice. The `range(len(...))` loop cannot
    # be used for iterating over types that are not subscriptable, such as
    # sets.
    # for i, ch in enumerate(expression):
    #     if ch == "(":
    #         pos_stack.append(i)
    #     elif ch == ")":
    #         res.append((pos_stack.pop(), i))
    return res


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
