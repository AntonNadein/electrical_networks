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
    dict_1 = {'name': "Ivan", 'surname': "Sidorov", 'patronymic': "Petrovich", 'age': 23, 'base_salary': 25000}
    emp = Employee.add_employee(dict_1)
    assert emp.name == "Ivan"
    assert emp.surname == "Sidorov"
    assert emp.patronymic == "Petrovich"
    assert emp.age == 23
    assert emp.base_salary == 25000


def test_new_job_coefficient(test_employee_data_1):
    """Тест изменения коэффициента зарплаты"""
    Employee.new_job_coefficient(1.2)
    assert test_employee_data_1.salary() == 48000


def test_repr_employee():
    """Тест вывода информации для разработчика"""
    emp_2 = Employee("Petr", "Ivanov", "Petrovich", 42)
    assert repr(emp_2) == "Employee(Petr, Ivanov, Petrovich, 42, 20000)"


def test_srt_employee():
    """Тест вывода информации для пользователя"""
    emp_2 = Employee("Petr", "Ivanov", "Petrovich", 42)
    assert str(emp_2).replace('\n', " ") == 'Ivanov Petr Petrovich Возраст:42 Зарплата: 24000.0руб.'
