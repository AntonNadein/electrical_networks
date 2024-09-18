import pytest

from src.class_employee import Employee
from src.class_team import Team
from src.class_team_electricians import MasterElectric
from src.transport import FreightTransport, PassengerTransport, SpecialTransport


@pytest.fixture
def test_employee_data_1():
    return Employee("Ivan", "Ivanov", "Ivanovich", 40, 40000)


@pytest.fixture
def test_employee_data_2():
    return Employee("Petr", "Ivanov", "Petrovich", 42)


@pytest.fixture
def test_team_master():
    return MasterElectric("Ivan", "Ivanov", "Ivanovich", 40, 25000, 5)


@pytest.fixture
def test_team_data(test_employee_data_1, test_employee_data_2, test_team_master):
    return Team("Рабочая бригада", "Мастрер", test_team_master, [test_employee_data_1, test_employee_data_2], 2)


@pytest.fixture
def test_passenger_transport():
    transport_1 = PassengerTransport("УАЗ", "Пассажироперевозки", 87, 16, 4)
    transport_2 = PassengerTransport("Газ66", "Бригадный", 95, 28, 6)
    transport_3 = PassengerTransport("Газ66", "Бригадный", 95, 25, 5)
    return transport_1, transport_2, transport_3


@pytest.fixture
def test_dict_passenger_transport():
    return {
        "name": "Газ66",
        "purpose": "Бригадный",
        "engine_power": 95,
        "fuel_consumption": 25,
        "passenger_capacity": 6,
    }


@pytest.fixture
def test_freight_transport():
    return FreightTransport("Газ", "Грузоперевозки", 87, 16, 4, 4)


@pytest.fixture
def test_special_transport():
    return SpecialTransport("Газ", "Автовышка", 87, 16, 4, 1)
