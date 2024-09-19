from src.team_electricians import ElectricianDriver


def test_master(test_team_master):
    """Тест класса мастер"""
    assert str(test_team_master) == "Ivanov Ivan Ivanovich Возраст:40 Зарплата: 37500.0руб."


def test_electrician_driver(test_passenger_transport):
    electrician = ElectricianDriver("Petr", "Petrov", "Ivanovich", 40, 20000, [test_passenger_transport])
    assert str(electrician) == "Petrov Petr Ivanovich Возраст:40 Зарплата: 24000.0руб."
