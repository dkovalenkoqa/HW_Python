#TODO: Обменник. Создать скрипт который будет запускаться из консоли 1 раз из консоли, выдавать результат и зарываться.
#     1. На вход обменнику вводишь количество денег int.
#     2. На выходе в консоль выводится отввет в таком виде:
#                 "Ты ввёл int (Валюта)"
#                 "конвертированная сумма в USD = int"
#     3. Валюту пользователя определите сами.


money = int(input('Введите сумму денег: '))
usd_uah_rate = 26.23
usd = round(money / usd_uah_rate, 2)
print(f'Ты ввёл {money}{"₴"}, конвертированная сумма в USD = {usd}$')
