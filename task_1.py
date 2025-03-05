def is_prime(n):
    if n <= 1:
        return False
    elif n == 2 or n == 3:
        return True
    elif n%3 == 0 or n%2 == 0:
        return False
    i = 5
    while i**2 <= n:
        if n%i == 0 or n%(i+2) == 0:
            return False
        i+=6
    return True
m = []
while True:
    try:
        a = int(input())
        b = int(input())
        break
    except ValueError as v:
        print('Вы ввели данные некоректно попробуйте заново')
        continue
for i in range(a, b+1):
    if is_prime(i):
        m.append(i)
print(m)