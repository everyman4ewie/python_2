# Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор
# натуральных чисел. У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент
# с тем же значением должен разместиться после них.


# Можно сделать так. Описание строчек в других видах этого же кода (ниже)
# 1 вариант
def numbers():
    while True:
        try:
            number = list(map(int, input('Введите числа через запятую: ').split(',')))  # перевожу то что введет пользователь сразу из текста в цифры и сразу в список
            print(sorted(number, reverse=True))
            counter = int(input('Введите сколько раз хотите добавлять цифры в список: '))
            q = 0
            while q < counter:
                num = input('Введите число, которое хотите добавить в список: ')
                number.append(int(num))
                number = sorted(number, reverse=True)
                print(f'Вы получили список: {number}')
                q += 1
        except ValueError:
            print("Вы ввели не числа. Попробуйте еще раз!")
        else:
            break
numbers()


# Не могу понять: почему, когда работаю в программе все ок, но когда нажимаю q вылетает ошибка
# Пришлось добавить две отдельных проверки ошибок, потому что если сделать одну, то выход из бесконечного
# цикла с помощью q он воспринимает как ошибку в виде "ввели не число".
# 2 вариант
# def numbers():
#     while True:
#         try:
#             number = list(map(int, input('Введите числа через запятую: ').split(',')))  # перевожу то что введет пользователь сразу из текста в цифры и сразу в список
#             print(sorted(number, reverse=True))
#             try:
#                 while True:
#                     q = 0
#                     num = input('Введите число, которое хотите добавить в список (чтобы выйти из программы нажмите q): ')
#                     if num == q:
#                         print(f'Вы закончили. Ваш список: {number}')
#                         break
#                     else:
#                         number.append(int(num))  # Добавляю число в список
#                         number = sorted(number, reverse=True)  # Сортирую список по убыванию
#                         print(f'Вы получили список: {number}')
#             except ValueError:
#                 if num == q:
#                     print(f'Вы закончили. Ваш список: {number}')
#                     break
#         except ValueError:
#             print("Вы ввели не числа. Попробуйте еще раз!")
#         else:
#             number.append(int(num))
#             number = sorted(number, reverse=True)
#             print(f'Вы получили список: {number}')
#             break
# numbers()


# Это первоначальная программа. Тут изи
# Основная программа
# number = list(map(int, input('Введите числа через запятую: ').split(',')))  # перевожу то что введет пользователь сразу из текста в цифры и сразу в список
# print(sorted(number, reverse=True))
#
# while True:
#     q = 0
#     num = input('Введите число, которое хотите добавить в список (чтобы выйти из программы нажмите q): ')
#     if num == q:
#         print(f'Вы закончили. Ваш список: {number}')
#         break
#     else:
#         number.append(int(num))
#         number = sorted(number, reverse=True)
#         print(f'Вы получили список: {number}')