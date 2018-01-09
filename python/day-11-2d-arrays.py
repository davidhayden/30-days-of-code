def find_max_hourglass(matrix):
    """
    >>> find_max_hourglass([\
            [1, 1, 1, 0, 0, 0],\
            [0, 1, 0, 0, 0, 0],\
            [1, 1, 1, 0, 0, 0],\
            [0, 0, 2, 4, 4, 0],\
            [0, 0, 0, 2, 0, 0],\
            [0, 0, 1, 2, 4, 0]\
        ])
    19
    """
    max_hourglass = None
    for j in range(1, 5):
        for k in range(1, 5):
            total = sum(matrix[j-1][k-1:k+2]) + \
                matrix[j][k] + sum(matrix[j+1][k-1:k+2])
            if max_hourglass is None or max_hourglass < total:
                max_hourglass = total

    return max_hourglass


if __name__ == '__main__':
    values = []
    for i in range(6):
        values.append(list(map(int, input().strip().split(' '))))

    print(find_max_hourglass(values))
