count = 0
name = input('Введите имя: ')
while name != 'Александра':
    name = input('Введите имя: ')
while name != 'Левон':
    count += 1
    name = input('Введите имя: ')
print(f'число людей в очереди: {count - 1}')