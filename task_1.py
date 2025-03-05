def is_prime(number):
    if number <= 1:
        return False
    elif number == 2 or number == 3:
        return True
    elif number % 3 == 0 or number % 2 == 0:
        return False
    i = 5
    while i ** 2 <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True

low = -1
high = -1
array_prime_numbers = []
while True:
    try:
        low = int(input())
        high = int(input())
        break
    except ValueError as ve:
        print('Вы ввели данные некоректно попробуйте заново')
        continue
for numeric in range(low, high + 1):
    if is_prime(numeric):
        array_prime_numbers.append(numeric)
print(array_prime_numbers)
