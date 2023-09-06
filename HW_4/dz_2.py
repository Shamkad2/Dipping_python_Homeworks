# 2. Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь, где ключ — значение
# переданного аргумента, а значение — имя аргумента. Если ключ не хешируем, используйте его строковое представление.



def bargs_to_dict(**bargs):
    result = {}
    for key, value in bargs.items():
        try:
            result[value] = key
        except:
            result[str(value)] = key
    return result

print(bargs_to_dict(name='Шамиль', sername='Кадыров', weight=35.5,
                     months=['January', 'February', 'March'],
                     courses={'python': 'ver 3.11', 'c#': 'ver 2.5'}))
