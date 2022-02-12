def exchange (amount, rate):
    if amount:
        if amount.isdigit():
            print(f'Ты ввёл {amount} {"₴"}')
            for key, value in rate.items():
                print(f'Конвертированная сумма в {key} = {round(int(amount) / value)}')
        elif amount.lstrip('-').isnumeric():
            print('Введите положительное число.')
        else:
            print('Вы ввели не число. Введите число.')
    else:
        print('Вы ввели пустое поле. Введите число.')

def exchange_b (curr, amount, rates):
    if amount:
        if amount.isdigit():
            print(f'Вы ввели сумму {amount}{"₴"} и валюту {curr}')
            for key, value in rates.items():
                if key == curr:
                    print(f'Конвертированная сумма в {key} = {round(int(amount) / value, 2)}')
                    break
        elif amount.lstrip('-').isnumeric():
            print('Введите положительное число.')
        else:
            print('Вы ввели не число. Введите число.')
    else:
        print('Вы ввели пустое поле. Введите число.')