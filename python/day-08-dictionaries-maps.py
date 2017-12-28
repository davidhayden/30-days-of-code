n = int(input().strip())
phone_book = {}

for i in range(n):
    name, phone_number = input().split(' ')
    phone_book[name] = phone_number

while True:
    query = input()
    if query in phone_book:
        print('{0}={1}'.format(query, phone_book[query]))
    else:
        print('Not found')
