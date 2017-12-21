n = int(input().strip())

if (n % 2 == 1) or (n >= 6 and n <= 20):
    print('Not Weird')
else:
    print('Weird')
