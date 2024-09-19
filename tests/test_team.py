import pytest

from src.class_team import Team
from src.team_electricians import Electrician


def test_team(test_team_data):
    """Тест базового класса бригад"""
    assert str(test_team_data) == (
        "Рабочая бригада. Мастрер: Ivanov Ivan Ivanovich Возраст:40 Зарплата: 37500.0руб. "
        "Подчиненные: Ivanov Ivan Ivanovich Возраст:40 Зарплата: 40000руб. "
        "Ivanov Petr Petrovich Возраст:42 Зарплата: 20000руб."
    )


def test_team_add_personal_error(test_team_data):
    """Тест базового класса на превышение лимита персонала"""
    with pytest.raises(TypeError):
        electrician_3 = Electrician("Petr", "Petrov", "Ivanovich", 40, 21000)
        test_team_data.add_personal(electrician_3)


def test_len_max_person_error(test_team_data):
    """Тест функции добавления на превышение лимита персонала"""
    with pytest.raises(TypeError):
        Team("jgbc", "мастер", "vfsnth", ["test", "test1"], 1)


def test_team_add_personal():
    """Тест функции добавления персонала"""
    electrician_1 = Electrician("Petr", "Petrov", "Ivanovich", 40, 25000)
    team = Team("jgbc", "мастер", "vfsnth", [electrician_1], 3)
    electrician_2 = Electrician("Test", "Petrov", "Ivanovich", 40, 20000)
    team.add_personal(electrician_2)
    assert str(team.personal[-1]) == "Petrov Test Ivanovich Возраст:40 Зарплата: 20000руб."
