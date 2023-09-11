# 1. ✔ Напишите функцию, которая принимает на вход строку — абсолютный путь до файла. Функция возвращает кортеж из трёх
# элементов: путь, имя файла, расширение файла.



import os

string = "C:/Users/user/PycharmProjects/pythonProject/GEEK/Dipping_python/Homeworks/HW_5/dz_1.py"

def fun(f_path: str) -> tuple:
    path, filename = os.path.split(f_path)
    name, extension = filename.split('.')
    return path, name, extension

print(f'Исходная строка: {string} \nКортеж из пути: {fun(string)}')

