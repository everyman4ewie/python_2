# Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются
# элементы с индексами 0 и 1, 2 и 3 и т.д. При нечетном количестве элементов последний
# сохранить на своем месте. Для заполнения списка элементов необходимо использовать
# функцию input().
elem = input('Введите элементы списка через запятую: ')
my_elem = [i for i in elem.split(',')]  # описывал в 1 задании
print(my_elem)  # вывожу элементы, чтобы можно было сравнить их с итоговым списком
el = 0  # задаю счетчику значение 0, чтобы начинался отсчет с нулевого элемента
for i in range(int(len(my_elem) / 2)):  # делаю перебор по элементам списка, при этом перевожу в
    # в формат int иначе не получится добавлять к счетчику цифры, т.к. формат другой и беру длину спсписка
    my_elem[el], my_elem[el + 1] = my_elem[el + 1], my_elem[el]  # самый простой способ, как мне показалось
    # поменять местами элементы 1 и 2, 3 и 4, 5 и 6 и т.д., чтобы они просто менялись местами
    el += 2  # добавляю каждый раз при переборе списка 2 значения,
             # чтобы с 0 перескачил на 2 эл-т, со 2 на 4 и т.д., пока не закончится список
print(my_elem)
# мне кажется, что проверку здесь делать смысла нет, потому что словарь состоит из цифр и слов, особо негде ошибаться