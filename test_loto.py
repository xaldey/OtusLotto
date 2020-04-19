from game_stuff import make_unique_numbers
import pytest


class TestGame:
    def test_dummy(self):
        """Проверка запуска теста"""
        assert 1 == 1

    def test_unique_number_row(self):
        """Верный ли ряд уникальных чисел получаем?"""
        assert(sorted(make_unique_numbers(4, 2, 5))) == [2, 3, 4, 5]

    def test_single_number(self):
        """А если только одно число пришло?"""
        assert make_unique_numbers(1, 1, 1) == [1]


if __name__ == '__main__':
    TestGame
