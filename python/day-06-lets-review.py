def print_characters(word):
    """
    Returns even and odd characters in word.

    >>> print_characters('Hacker')
    'Hce akr'
    >>> print_characters('Rank')
    'Rn ak'
    >>> print_characters('David')
    'Dvd ai'
    >>> print_characters('')
    ''
    >>> print_characters('a')
    'a'
    >>> print_characters('ab')
    'a b'
    >>> print_characters('abc')
    'ac b'
    """
    even, odd = '', ''
    for i in range(len(word)):
        if i % 2 == 0:
            even += word[i]
        else:
            odd += word[i]

    return ('{} {}'.format(even, odd)).strip()


if __name__ == '__main__':
    n = int(input().strip())
    for line in range(n):
        print(print_characters(input().strip()))
