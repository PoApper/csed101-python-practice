def hanoi(n, src, dest, aux):
    """
    >>> hanoi(1, "A", "C", "B")
    Move disk 1 from A to C
    >>> hanoi(3, "A", "C", "B")
    Move disk 1 from A to C
    Move disk 2 from A to B
    Move disk 1 from C to B
    Move disk 3 from A to C
    Move disk 1 from B to A
    Move disk 2 from B to C
    Move disk 1 from A to C
    >>> hanoi(5, "A", "C", "B")
    Move disk 1 from A to C
    Move disk 2 from A to B
    Move disk 1 from C to B
    Move disk 3 from A to C
    Move disk 1 from B to A
    Move disk 2 from B to C
    Move disk 1 from A to C
    Move disk 4 from A to B
    Move disk 1 from C to B
    Move disk 2 from C to A
    Move disk 1 from B to A
    Move disk 3 from C to B
    Move disk 1 from A to C
    Move disk 2 from A to B
    Move disk 1 from C to B
    Move disk 5 from A to C
    Move disk 1 from B to A
    Move disk 2 from B to C
    Move disk 1 from A to C
    Move disk 3 from B to A
    Move disk 1 from C to B
    Move disk 2 from C to A
    Move disk 1 from B to A
    Move disk 4 from B to C
    Move disk 1 from A to C
    Move disk 2 from A to B
    Move disk 1 from C to B
    Move disk 3 from A to C
    Move disk 1 from B to A
    Move disk 2 from B to C
    Move disk 1 from A to C
    """
    if n==1:
        print("Move disk %d from %s to %s"%(n, src, dest))
    else:
        hanoi(n-1, src, aux, dest)
        print("Move disk %d from %s to %s"%(n, src, dest))
        hanoi(n-1, aux, dest, src)

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)