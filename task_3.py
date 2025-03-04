low = 0
high = 1000
mid = high // 2
while low + 1 != high:
    guess = input(f'твоё число больше {mid} ')
    if guess != 'да' and guess != 'нет':
        print('Некоректно введены данные. Отвечайте только "да" или "нет"')
        continue
    if guess == 'да':
        low = mid
        mid = mid + (high - low) // 2
    else:
        high = mid
        mid = mid - (high - low) // 2
    print(low, high)
print(f'Вы загадали число {high}')
