# 3. ✔ Создайте функцию генератор чисел Фибоначчи (см. Википедию).



a = int(input('Введите число:  '))


def fib(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


print(list(fib(a)))