def reversed_array(array):
    """
    Returns a space separated version
    of the array in reverse.

    >>> reversed_array([1, 2, 3, 4])
    '4 3 2 1'
    """
    return ' '.join(str(i) for i in reversed(array))


if __name__ == '__main__':
    n, array = input(), input().split()
    print(reversed_array(array))
