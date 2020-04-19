from game_stuff import make_unique_numbers, Card, choose_mode, gamemode
import pytest


class TestGame:
    @pytest.mark.parametrize(
        'args, expected_result',
        [
            pytest.param(
                (10, 1, 90), 10,
                id='count = 10',
            ),
            pytest.param(
                (100, 1, 500), 100,
                id='count = 100',
            ),
        ]
    )
    def test_len_unique_row(self, args, expected_result):
        """Проверка длины уникального списка
        при условии разных параметров
        """
        res = make_unique_numbers(*args)
        assert len(res) == expected_result

    def test_dummy(self):
        """Проверка запуска теста"""
        assert 1 == 1

    def test_unique_number_row(self):
        """Верный ли ряд уникальных чисел получаем?"""
        assert (sorted(make_unique_numbers(4, 2, 5))) == [2, 3, 4, 5]

    def test_single_number(self):
        """А если только одно число пришло?"""
        assert make_unique_numbers(1, 1, 1) == [1]


if __name__ == '__main__':
    TestGame
