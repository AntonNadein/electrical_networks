from src.class_employee import Driver, Specialist, Supervisor
from src.class_team import Team


class TeamOfSupervisor(Team):
    """Бригада участка транпорта"""

    pass


class SupervisorManager(Supervisor, Specialist, Driver):
    """Класс руководитель района электрических сетей"""

    job_coefficient = 2.5

    def __init__(
        self,
        name: str,
        surname: str,
        patronymic: str,
        age: int,
        base_salary: int = None,
        subordinates: list = None,
        equipment_list: list = None,
        transport_list: list = None,
        category_driver_license: str = None,
    ) -> None:
        Supervisor.__init__(self, name, surname, patronymic, age, base_salary, subordinates)
        Specialist.__init__(self, name, surname, patronymic, age, base_salary, equipment_list)
        Driver.__init__(self, name, surname, patronymic, age, base_salary, transport_list, category_driver_license)


class Engineer(Supervisor, Specialist, Driver):
    """Класс инженер района электрических сетей"""

    job_coefficient = 2.1

    def __init__(
        self,
        name: str,
        surname: str,
        patronymic: str,
        age: int,
        base_salary: int = None,
        subordinates: list = None,
        equipment_list: list = None,
        transport_list: list = None,
        category_driver_license: str = None,
    ) -> None:
        Supervisor.__init__(self, name, surname, patronymic, age, base_salary, subordinates)
        Specialist.__init__(self, name, surname, patronymic, age, base_salary, equipment_list)
        Driver.__init__(self, name, surname, patronymic, age, base_salary, transport_list, category_driver_license)
