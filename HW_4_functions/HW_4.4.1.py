import module

#TODO: Задача №4
# Обменник. Скрипт запускается в консоли и работает постоянно. Остановится нажатием ctrl+c.
#     1. Скрипт сначала выводит "Выберите валюту из ['USD','EUR','CHF','GBP','CNY']"
#     2. Пользователь вводит один из 5 вариантов ['USD','EUR','CHF','GBP','CNY']
#     3. Потом Скрипт выводит "Введите сумму"
#     4. Пользователь вводит сумму int
#     5. Скрипт выводит:
#             "Вы ввели сумму int и валюту "Валюта" "
#             "конвертированная сумма в "Валюта" = int"
#     6. Скипт должен выдать сообщение
#                 "Введите положительное число." Если число меньше 0.
#                 "Вы ввели не число. Введите число." Если введены буквы.
#                 "Вы ввели пустое поле. Введите число." Если введено пустое значение.
#     7. После сообщеня об ошибке, скрипт должен автоматом вернуться к шагу 1.
#     8. Валюту пользователя определите сами.

rates = {"USD": 26.23,
         "EUR": 31.93,
         "CHF": 30.38,
         "GBR": 38.16,
         "CNY": 4.43}

try:
    while True:
        curr = input(f"Выберите валюту из ['USD','EUR','CHF','GBP','CNY']: ").upper()
        if curr in rates.keys():
            amount = input("Введите сумму: ")
            module.exchange_b(curr, amount, rates)
        else:
            print(f"Выберите валюту из списка")

except KeyboardInterrupt:
    print('\nПрограмма завершена')