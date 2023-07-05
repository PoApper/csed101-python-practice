def rpn(expr):
    """
    Evaluate the expression given in `expr`, which is written in reverse
    Polish notation. `expr` is a list constisting of integers and strings. The
    integer elements of `expr` are operands, and string elements of `expr` are
    operators. The operators are one of ["+", "-", "*", "/"], and "/"
    corresponds to integer division. In other words, you should use `//`
    operator of Python to implement it. You don't have to care about malformed
    expressions, such as expressions that lack an operator, division by zero,
    etc.

    Reverse Polish notation (RPN for short) is a notation of writing
    mathematical expressions. Unlike infix notation that we normally use, in
    RPN, operators follow their operands. For example, "3 + 4" is written as
    "3 4 +" in RPN.

    >>> rpn([3, 4, "+"])
    7
    >>> rpn([2, 1, "-"])
    1
    >>> rpn([5, 6, "*"])
    30
    >>> rpn([4, 2, "/"])
    2
    >>> rpn([1, 2, "+", 3, 4, "+", "*"])
    21
    >>> rpn([3, 4, "*", 5, 6, "*", "+"])
    42
    >>> rpn([6, 2, "+", 5, 1, "-", "/"])
    2

    Hint: Since operators come after operands, you can immediately calculate
    operands that come before an operator. From this fact, we can derive an
    algorithm based on stack:

    Create a stack that holds intermediate values.
    Iterate over the expression list. Consider two possibilities:
        - If the current element is a number, push it to the stack.
        - If the current element is an operator, pop two elements from the
          stack, and calculate according to the operator. Note that stack is
          last-in-first-out, so the number that popped later is the first
          operand.
    """
    stack = []
    OPERATORS = ["+", "-", "*", "/"]
    for term in expr:
        if term not in OPERATORS:
            stack.append(term)
            continue
        y = stack.pop()
        x = stack.pop()
        if term == "+":
            stack.append(x + y)
        elif term == "-":
            stack.append(x - y)
        elif term == "*":
            stack.append(x * y)
        elif term == "/":
            stack.append(x // y)
    return stack[0]


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
