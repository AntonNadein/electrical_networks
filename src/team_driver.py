from src.class_employee import Driver, Supervisor
from src.class_team import Team


class TeamOfDriver(Team):
    """Участок водителей"""

    pass


class Mechanic(Supervisor, Driver):
    """Механик"""

    job_coefficient = 1.5

    def __init__(
        self,
        name: str,
        surname: str,
        patronymic: str,
        age: int,
        base_salary: int = None,
        subordinates: list = None,
        transport_list: list = None,
        category_driver_license: str = None,
    ):
        Supervisor.__init__(self, name, surname, patronymic, age, base_salary, subordinates)
        Driver.__init__(self, name, surname, patronymic, age, base_salary, transport_list, category_driver_license)


class DriverProfessional(Driver):
    """Класс водитель"""

    job_coefficient = 1.1
