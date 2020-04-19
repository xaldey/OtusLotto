from random import randint, shuffle
import sys

def make_unique_numbers(count, minim, maxim):
    try:
        # Создаю пустое множество (для уникальных значений)
        num_row = set()
        # Генерю номера от min до max, пока не наполнится
        # (count элементов) множество
        if count <= 0:
            raise ValueError('Количество чисел может быть строго натуральным!')
            sys.exit()
        while len(num_row) < count:
            num = randint(minim, maxim)
            num_row.add(num)
        # Создаю список из полученного множества из count
        # уникальных значений
        num_row = list(num_row)
        # "Встряхиваю" список цифр
        shuffle(num_row)
        return num_row
    except TypeError:
        raise TypeError


# Создаю класс Карточки
class Card:
    _rows = 3
    _columns = 9
    _nums_in_each_rows = 5
    _data = None
    _empty_num = 0
    _checked_number = -1

    def __init__(self):
        card_numbers_count = self._rows * self._nums_in_each_rows
        digits_for_card = make_unique_numbers(card_numbers_count, 1, 90)

        # Forming empty list of data for card view
        self._data = []
        for item in range(0, self._rows):
            tmp = sorted(digits_for_card[self._nums_in_each_rows * item: self._nums_in_each_rows * (item + 1)])
            blank = self._columns - self._nums_in_each_rows
            for i in range(0, blank):
                index = randint(0, len(tmp))
                tmp.insert(index, self._empty_num)
            self._data += tmp

    def __str__(self):
        delimiter = '----------------------------'
        cursor = delimiter + '\n'
        for index, number in enumerate(self._data):
            if number == self._empty_num:
                cursor += '  '
            elif number == self._checked_number:
                cursor += ' -'
            elif number < 10:
                cursor += f' {str(number)}'
            else:
                cursor += str(number)

            if (index + 1) % self._columns == 0:
                cursor += '\n'
            else:
                cursor += ' '
        return cursor + delimiter

    def __contains__(self, item):
        return item in self._data

    def crossout_number(self, number):
        for index, item in enumerate(self._data):
            if item == number:
                self._data[index] = self._checked_number
                return
        raise ValueError(f'Номера {number} нет на карточке.')

    def closed(self) -> bool:
        return set(self._data) == {self._empty_num, self._checked_number}


# Формирую класс для Игры №1 (человек - компьютер) GameHuman_PC
class GameHumanVsPc:
    _usercard = None
    _compcard = None
    _num_of_barrels = 90
    _barrels = []
    _gameover = False

    def __init__(self):
        self._usercard = Card()
        self._compcard = Card()
        self._barrels = make_unique_numbers(self._num_of_barrels, 1, 90)

    def play_round(self) -> int:
        """
        :return:
         0 - game must go on
         1 - user wins
         2 - computer wins
        """

        # Достаю бочонки (убираю их из мешка и "попаю"
        barrel = self._barrels.pop()
        print(f'Новый бочонок: {barrel}  (осталось {len(self._barrels)})')
        print(f'-----  Карточка человека -----\n{self._usercard}')
        print(f'----- Карточка компьютера ----\n{self._compcard}')

        user_answer = input('Зачеркнуть цифру? y/n)').lower().strip()
        if (user_answer == 'y' and barrel not in self._usercard) or (user_answer != 'y' and barrel in self._usercard):
            return 2

        if barrel in self._usercard:
            self._usercard.crossout_number(barrel)
            if self._usercard.closed():
                return 1
        if barrel in self._compcard:
            self._compcard.crossout_number(barrel)
            if self._compcard.closed():
                return 2
        return 0


# Формирую класс для Игры №2 (комп-комп) GamePC_PC
class GamePcToPc:
    _compcard1 = None
    _compcard2 = None
    _num_of_barrels = 90
    _barrels = []
    _gameover = False

    def __init__(self):
        self._compcard1 = Card()
        self._compcard2 = Card()
        self._barrels = make_unique_numbers(self._num_of_barrels, 1, 90)

    def play_round(self) -> int:
        """
        :return:
         0 - game must go on
         1 - user wins
         2 - computer wins
        """

        # Достаю бочонки (убираю их из мешка и "попаю"
        barrel = self._barrels.pop()
        print(f'Новый бочонок: {barrel}  (осталось {len(self._barrels)})')
        print(f'-- Карточка компьютера #1 --\n{self._compcard1}')
        print(f'-- Карточка компьютера #2 --\n{self._compcard2}')

        # Убираю вопрос игроку-человеку
        # user_answer = input('Зачеркнуть цифру? y/n)').lower().strip()
        # if (user_answer == 'y' and barrel not in self._usercard) or (user_answer != 'y' and barrel in self._usercard):
        #     return 2

        if barrel in self._compcard1:
            self._compcard1.crossout_number(barrel)
            # Добавил задержку для визуального контроля игры комп-комп
            # time.sleep(2)
            if self._compcard1.closed():
                return 1
        if barrel in self._compcard2:
            self._compcard2.crossout_number(barrel)
            # Добавил задержку для визуального контроля игры комп-комп
            # time.sleep(2)
            if self._compcard2.closed():
                return 2
        return 0


# Формирую класс для Игры №3 (человек - человек) GameHuman_Human
class GameHumanVsHuman:
    _usercard1 = None
    _usercard2 = None
    _num_of_barrels = 90
    _barrels = []
    _gameover = False

    def __init__(self):
        self._usercard1 = Card()
        self._usercard2 = Card()
        self._barrels = make_unique_numbers(self._num_of_barrels, 1, 90)

    def play_round(self) -> int:
        """
        :return:
         0 - game must go on
         1 - user1 wins
         2 - user2 wins

        """

        # Достаю бочонки (убираю их из мешка и "попаю"
        barrel = self._barrels.pop()
        print(f'Новый бочонок: {barrel}  (осталось {len(self._barrels)})')
        print(f'- Карточка первого игрока -\n{self._usercard1}')
        print(f'- Карточка второго игрока -\n{self._usercard2}')

        user_answer1 = input('Вопрос к Игорьку №1 - Зачеркнуть цифру? y/n)').lower().strip()
        if (user_answer1 == 'y' and barrel not in self._usercard1) or (user_answer1 != 'y' and barrel in self._usercard1):
            return 2

        if barrel in self._usercard1:
            self._usercard1.crossout_number(barrel)
            if self._usercard1.closed():
                return 1

        user_answer2 = input('Вопрос к Игорьку №2 - Зачеркнуть цифру? y/n)').lower().strip()
        if (user_answer2 == 'y' and barrel not in self._usercard2) or (
                user_answer2 != 'y' and barrel in self._usercard2):
            return 1

        if barrel in self._usercard2:
            self._usercard2.crossout_number(barrel)
            if self._usercard2.closed():
                return 2
        return 0


def gamemode(mode):
    if mode == 0:
        game = GameHumanVsPc()
        while True:
            score = game.play_round()
            if score == 1:
                print('Вы выиграли!')
                break
            elif score == 2:
                print('Вы проиграли!')
                break
    elif mode == 2:
        game = GameHumanVsHuman()
        while True:
            score = game.play_round()
            if score == 1:
                print('Выиграл Игорек №1!')
                break
            elif score == 2:
                print('Выиграл Игорек №2!')
                break
    else:
        game = GamePcToPc()
        while True:
            score = game.play_round()
            if score == 1:
                print('Выиграл первый компьютер!')
                break
            elif score == 2:
                print('Выиграл второй компьютер!')
                break


if __name__ == '__main__':
    print('Выберите режим игры: человек-компьютер (0) / человек-человек (2) / компьютер-компьютер (любая другая цифра)')
    mode = int(input('Сделайте выбор режима: '))
    gamemode(mode)
