import pytest

from src.class_employee import Employee


def test_employee(test_employee_data_1, test_employee_data_2):
    """Тест добавления сотрудника"""
    assert test_employee_data_1.name == "Ivan"
    assert test_employee_data_1.surname == "Ivanov"
    assert test_employee_data_1.patronymic == "Ivanovich"
    assert test_employee_data_1.age == 40
    assert test_employee_data_1.base_salary == 40000
    assert Employee.total_employee == 2


def test_add_employee():
    """Тест добавления сотрудника через классметод"""
    dict_1 = {"name": "Ivan", "surname": "Sidorov", "patronymic": "Petrovich", "age": 23, "base_salary": 25000}
    emp = Employee.add_employee(dict_1)
    assert emp.name == "Ivan"
    assert emp.surname == "Sidorov"
    assert emp.patronymic == "Petrovich"
    assert emp.age == 23
    assert emp.base_salary == 25000


def test_repr_employee():
    """Тест вывода информации для сотрудника"""
    emp_2 = Employee("Petr", "Ivanov", "Petrovich", 42)
    assert repr(emp_2) == "Employee(Petr, Ivanov, Petrovich, 42, 20000)"


def test_srt_employee():
    """Тест вывода информации для сотрудника"""
    emp_2 = Employee("Petr", "Ivanov", "Petrovich", 42)
    assert str(emp_2) == "Ivanov Petr Petrovich Возраст:42 Зарплата: 20000руб."


def test_srt_supervisor_norm(test_srt_supervisor):
    """Тест вывода информации для руководителя"""
    assert test_srt_supervisor.name == "Petr"
    assert test_srt_supervisor.surname == "Jdanov"
    assert test_srt_supervisor.patronymic == "Petrovich"
    assert test_srt_supervisor.age == 42
    assert test_srt_supervisor.base_salary == 50000
    assert test_srt_supervisor.subordinates[0].name == "Petr"
    assert test_srt_supervisor.number_of_subordinates == 1


def test_srt_supervisor_add_employee(test_srt_supervisor, test_employee_data_1):
    """Тест добавления работника"""
    test_srt_supervisor.add_subordinates(test_employee_data_1)
    assert test_srt_supervisor.subordinates[1].name == "Ivan"
    assert test_srt_supervisor.number_of_subordinates == 2


def test_srt_supervisor_add_employees(test_srt_supervisor, test_employee_data_1, test_employee_data_2):
    """Тест добавления списка работников"""
    employee_3 = Employee("Denis", "Ivanov", "Sidorov", 55, 25000)
    test_srt_supervisor.add_subordinates(
        [test_employee_data_1, test_employee_data_1, test_employee_data_2, "test", employee_3]
    )
    assert test_srt_supervisor.number_of_subordinates == 3


def test_srt_supervisor_add_employee_error(test_srt_supervisor):
    """Тест добавления работника с ошибкой"""
    with pytest.raises(TypeError, match="Не подходящий элемент для добавления"):
        test_srt_supervisor.add_subordinates("test_employee_data_1")


def test_specialist_norm(test_specialist):
    """Тест вывода информации для специалиста"""
    assert test_specialist.name == "Petr"
    assert test_specialist.surname == "Vasin"
    assert test_specialist.patronymic == "Petrovich"
    assert test_specialist.age == 42
    assert test_specialist.base_salary == 50000
    assert test_specialist.equipment_list[0].name == "ТМ-400"
    assert test_specialist.number_of_equipment == 1


def test_specialist_add_equipment(test_specialist, test_metering_device):
    """Тест добавления оборудования"""
    test_specialist.add_equipment(test_metering_device)
    assert test_specialist.equipment_list[1].name == "Прибор учета"
    assert test_specialist.number_of_equipment == 2


def test_specialist_add_equipments(test_specialist, test_metering_device, test_oil_switch, test_oil_filled_equipment):
    """Тест добавления списка оборудования"""
    test_specialist.add_equipment(
        [test_oil_switch, test_metering_device, test_oil_switch, "test", test_oil_filled_equipment]
    )
    assert test_specialist.number_of_equipment == 4


def test_specialist_add_equipment_error(test_specialist):
    """Тест добавления оборудования с ошибкой"""
    with pytest.raises(TypeError, match="Не подходящий элемент для добавления"):
        test_specialist.add_equipment("test_1")


def test_driver_norm(test_driver):
    """Тест вывода информации для водителя"""
    assert test_driver.name == "Vasily"
    assert test_driver.surname == "Vasin"
    assert test_driver.patronymic == "Petrovich"
    assert test_driver.age == 42
    assert test_driver.base_salary == 45000
    assert test_driver.transport_list[0].name == "Газ"
    assert test_driver.number_of_transport == 1


def test_driver_add_equipment(test_driver, test_special_transport):
    """Тест добавления транспорта"""
    test_driver.add_transport(test_special_transport)
    assert test_driver.transport_list[1].purpose == "Автовышка"
    assert test_driver.number_of_transport == 2


def test_driver_add_equipments(test_driver, test_passenger_transport):
    """Тест добавления списка транспорта"""
    test_driver.add_transport(list(test_passenger_transport))
    assert test_driver.number_of_transport == 4


def test_driver_add_equipment_error(test_driver):
    """Тест добавления оборудования с ошибкой"""
    with pytest.raises(TypeError, match="Не подходящий элемент для добавления"):
        test_driver.add_transport("test_1")
