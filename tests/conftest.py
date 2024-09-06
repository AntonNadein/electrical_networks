import pytest

from src.class_employee import Employee


@pytest.fixture
def test_employee_data_1():
    return Employee("Ivan", "Ivanov", "Ivanovich", 40, 40000)


@pytest.fixture
def test_employee_data_2():
    return Employee("Petr", "Ivanov", "Petrovich", 42)