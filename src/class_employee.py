from abc import ABC, abstractmethod

from src.equipment import ElectricalEquipment
from src.transport import Transport


class BaseEmployee(ABC):

    @classmethod
    @abstractmethod
    def add_employee(cls, dicts):
        pass

    @abstractmethod
    def salary(self):
        pass


class Employee(BaseEmployee):
    """Базовый класс работника"""

    id_employee = 0
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
        self.age = self._check_age_value(age)
        self.base_salary = base_salary if base_salary else 20000
        Employee.id_employee += 1

    @classmethod
    def add_employee(cls, dicts):
        """Добавление нового работника из словаря"""
        cls(**dicts)
        return cls(**dicts)

    def salary(self):
        """Рассчет зарплаты работника (зарплата * зарплатный коэффициент)"""
        return self.base_salary * self.job_coefficient

    def _check_age_value(self, value: float | int) -> float | int:
        """Функция проверки отрицательного значения"""
        if value < 0:
            raise ValueError("Возраст не может быть отрицательным")
        elif value > 150:
            raise ValueError("К сожалению люди столько не живут")
        else:
            return value

    def __repr__(self):
        """Вывод информации для разработчика"""
        return (
            f"{self.__class__.__name__}({self.name}, {self.surname}, {self.patronymic},"
            f" {self.age}, {self.base_salary})"
        )

    def __str__(self):
        """Вывод информации для пользователя"""
        return f"{self.surname} {self.name} {self.patronymic} Возраст:{self.age} Зарплата: {self.salary()}руб."


class Supervisor(Employee):
    """Класс руководителя"""

    subordinates: list

    def __init__(
        self, name: str, surname: str, patronymic: str, age: int, base_salary: int = None, subordinates: list = None
    ) -> None:
        super().__init__(name, surname, patronymic, age, base_salary)
        self.subordinates = subordinates if subordinates else []
        self.number_of_subordinates = self._get_len_subordinates()

    def add_subordinates(self, worker: list | Employee):
        """Добавление работников в список"""
        if isinstance(worker, Employee):
            self.subordinates.append(worker)
            self.number_of_subordinates = self._get_len_subordinates()
        elif type(worker) is list:
            for i in worker:
                if isinstance(i, Employee):
                    self.subordinates.append(i)
            self.subordinates = list(set(self.subordinates))
            self.number_of_subordinates = self._get_len_subordinates()
        else:
            raise TypeError("Не подходящий элемент для добавления")

    def _get_len_subordinates(self):
        """Подсчет количества работников"""
        return len(self.subordinates)


class Specialist(Employee):
    """Класс специалист"""

    equipment_list: list

    def __init__(
        self, name: str, surname: str, patronymic: str, age: int, base_salary: int = None, equipment_list: list = None
    ) -> None:
        super().__init__(name, surname, patronymic, age, base_salary)
        self.equipment_list = equipment_list if equipment_list else []
        self.number_of_equipment = self._get_len_equipment()

    def add_equipment(self, worker: list | ElectricalEquipment):
        """Добавление оборудования в список"""
        if isinstance(worker, ElectricalEquipment):
            self.equipment_list.append(worker)
            self.number_of_equipment = self._get_len_equipment()
        elif type(worker) is list:
            for i in worker:
                if isinstance(i, ElectricalEquipment):
                    self.equipment_list.append(i)
            self.equipment_list = list(set(self.equipment_list))
            self.number_of_equipment = self._get_len_equipment()
        else:
            raise TypeError("Не подходящий элемент для добавления")

    def _get_len_equipment(self):
        """Подсчет количества оборудования"""
        return len(self.equipment_list)


class Driver(Employee):
    """Класс водитель"""

    transport_list: list
    category_driver_license: str

    def __init__(
        self,
        name: str,
        surname: str,
        patronymic: str,
        age: int,
        base_salary: int = None,
        transport_list: list = None,
        category_driver_license: str = None,
    ) -> None:
        super().__init__(name, surname, patronymic, age, base_salary)
        self.transport_list = transport_list if transport_list else []
        self.category_driver_license = category_driver_license
        self.number_of_transport = self._get_len_transport()

    def add_transport(self, worker: list | Transport):
        """Добавление оборудования в список"""
        if isinstance(worker, Transport):
            self.transport_list.append(worker)
            self.number_of_transport = self._get_len_transport()
        elif type(worker) is list:
            for i in worker:
                if isinstance(i, Transport):
                    self.transport_list.append(i)
            self.transport_list = list(set(self.transport_list))
            self.number_of_transport = self._get_len_transport()
        else:
            raise TypeError("Не подходящий элемент для добавления")

    def _get_len_transport(self):
        """Подсчет количества транспорта"""
        return len(self.transport_list)


# if __name__ == "__main__":
#     emp_1 = Employee("Ivan", "Ivanov", "Ivanovich", 40, 40000)
#     emp_2 = Employee("Petr", "Ivanov", "Petrovich", 42)
#     print(emp_1.base_salary)
#     print(repr(emp_1))
#     print(str(emp_1))
#     print(Employee.total_employee)
#
    # dict_3 = {'name': "Ivan", 'surname': "Sidorov", 'patronymic': "Petrovich", 'age': 23, 'base_salary': 25000}
    # emp_3 = Employee.add_employee(dict_3)
    # print(emp_3.name)
    # print(repr(emp_3))
    # print(str(emp_3))
#     print(Employee.total_employee)
#     supervisor = Supervisor("Anry", "Gabi", "Ivanovich", 40, 40000, [emp_1])
#     print(supervisor.subordinates)
#     print(supervisor.number_of_subordinates)
#     supervisor.add_subordinates(emp_2)
#     print(supervisor.number_of_subordinates)
#     supervisor.add_subordinates([emp_1, emp_2, emp_3, "sadf"])
#     print(supervisor.subordinates)
#     print(supervisor.number_of_subordinates)
