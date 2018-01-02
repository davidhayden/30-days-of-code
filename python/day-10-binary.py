def max_consecutive_ones(n):
    """
    >>> max_consecutive_ones(5)
    1
    >>> max_consecutive_ones(13)
    2
    """
    binary_str = str(bin(n)[2:])

    current, max = 0, 0
    for i in binary_str:
        if i == '1':
            current += 1
            continue

        if current > max:
            max = current

        current = 0

    return max


if __name__ == '__main__':
    print(max_consecutive_ones(13))
