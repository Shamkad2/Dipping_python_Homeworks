# 2. ✔ Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины: имена str,
# ставка int, премия str с указанием процентов вида «10.25%». В результате получаем словарь с именем в качестве
# ключа и суммой премии в качестве значения. Сумма рассчитывается как ставка умноженная на процент премии



names = ['Poly', 'Sebastian', "Kristian"]
salaries = [15000, 20000, 25000]
awards = ['10.0%', '7.25%', '5%']
print(f'исходные данные:\n{names}\n{salaries}\n{awards}')
print('Решение:')

print({name: salary * float(award[:-1]) / 100 for name, salary, award in zip(names, salaries, awards)})

