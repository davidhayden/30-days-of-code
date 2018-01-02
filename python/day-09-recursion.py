def factorial(n):
    """
    >>> factorial(0)
    1
    >>> factorial(1)
    1
    >>> factorial(2)
    2
    >>> factorial(5)
    120
    """
    if n < 2:
        return 1;

    return n * factorial(n - 1)


if __name__ == "__main__":
    n = int(input().strip())
    result = factorial(n)
    print(result)
