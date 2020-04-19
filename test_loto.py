from game_stuff import make_unique_numbers
import pytest
from random import randint, shuffle


class TestGame:

    def test_unique_number_row(self):
        '''Верный ли ряд уникальных чисел получаем?'''
        assert(sorted(make_unique_numbers(4, 2, 5))) == [2, 3, 4, 5]


if __name__ == '__main__':
    TestGame
