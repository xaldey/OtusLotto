from random import random, uniform, randrange, randint


def make_unique_numbers(count, minim, maxim):
    # Создаю пустое множество (для уникальных значений)
    num_row = set()
    # Генерю номера от min до max, пока не наполнится
    # (count элементов) множество
    while len(num_row) < count:
        num = randint(minim, maxim)
        num_row.add(num)
    # Создаю список из полученного множества из count
    # уникальных значений
    num_row = list(num_row)
    # Сортирую полученный список
    num_row.sort()
    print(num_row)
    return num_row


print('-' * 40)
make_unique_numbers(15,1,90)
print('-' * 40)


#
# class Card():
#     pass
#
# class Player():
#     pass
#
# class Bag():
#     pass
#

# Класс Бочонок
class Barrel:
    __num = None

    def __init__(self):
        self.__num = randint(1, 90)

    @property
    def num(self):
        return self.__num

    def __str__(self):
        return str(self.__num)

#
# if __name__ == '__main__':
#     main
#
#
