# 2. Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.


def print_hex(b_input):

    print(f'Вы ввели {b_input}\n')
    dict_hex = {10: 'A',
                11: 'B',
                12: 'C',
                13: 'D',
                14: 'E',
                15: 'F'}
    b = b_input
    list_b = []
    while (b // 16) > 0:
        ostatok = b % 16
        if ostatok > 9:
            list_b.insert(0, dict_hex[ostatok])
        else:
            list_b.insert(0, str(ostatok))
        b = b // 16
    list_b.insert(0,str(b))
    print(f'Число {b_input} в шестнадцатеричной системе => {("".join(list_b))}')
    print(f'Проверка введенного: {b_input} в шестнадцатеричной системе => {hex(b_input)}')



b = -1
while b < 0 or b > 1000000:
    try:
        b = int(input('Введите b от 1 до 1000000 => '))
    except:
        print('Введите число')
print_hex(b)