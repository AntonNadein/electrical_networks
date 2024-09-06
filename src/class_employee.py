from src.base_employee import BaseEmployee


class Employee(BaseEmployee):
    """Базовый класс работника"""

    total_employee = 0
    job_coefficient = 1

    name: str
    surname: str
    patronymic: str
    age: int
    base_salary: int

    def __init__(self, name: str, surname: str, patronymic: str, age: int, base_salary: int = None) -> None:
        self.name = name
        self.surname = surname
        self.patronymic = patronymic
        self.age = age
        self.base_salary = base_salary if base_salary else 20000
        Employee.total_employee += 1

    @classmethod
    def add_employee(cls, dicts):
        """Добавление нового работника из словаря"""
        return cls(**dicts)

    def salary(self):
        """Рассчет зарплаты работника (зарплата * зарплатный коэффициент)"""
        return self.base_salary * self.job_coefficient

    def __repr__(self):
        """Вывод информации для разработчика"""
        return (f"{self.__class__.__name__}({self.name}, {self.surname}, {self.patronymic},"
                f" {self.age}, {self.base_salary})")

    def __str__(self):
        """Вывод информации для пользователя"""
        return f"{self.surname} {self.name} {self.patronymic} Возраст:{self.age} Зарплата: {self.salary()}руб."


# if __name__=="__main__":
#     emp_1 = Employee("Ivan", "Ivanov", "Ivanovich", 40, 40000)
#     emp_2 = Employee("Petr", "Ivanov", "Petrovich", 42)
#     print(emp_1.base_salary)
#     print(repr(emp_1))
#     print(str(emp_1))
#     print(Employee.total_employee)
#
#     dict_3 = {'name': "Ivan", 'surname': "Sidorov", 'patronymic': "Petrovich", 'age': 23, 'base_salary': 25000}
#     emp_3 = Employee.add_employee(dict_3)
#     print(repr(emp_3))
#     print(str(emp_3))
#     print(Employee.total_employee)
