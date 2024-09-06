import pytest

from src.class_employee import Employee
from src.class_team import Team
from src.class_team_electricians import MasterElectric


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
