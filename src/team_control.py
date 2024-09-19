from src.class_employee import Employee, Specialist, Supervisor
from src.class_team import Team


class TeamOfControl(Team):
    """Бригада участка транпорта"""

    pass


class SupervisorControl(Supervisor, Specialist):
    """Класс руководитель участка транпорта"""

    job_coefficient = 1.5

    def __init__(
        self,
        name: str,
        surname: str,
        patronymic: str,
        age: int,
        base_salary: int = None,
        subordinates: list = None,
        equipment_list: list = None,
    ) -> None:
        Supervisor.__init__(self, name, surname, patronymic, age, base_salary, subordinates)
        Specialist.__init__(self, name, surname, patronymic, age, base_salary, equipment_list)


class Inspector(Specialist):
    """Класс инспектор участка транпорта"""

    job_coefficient = 1.2


class ElectricianControl(Employee):
    """Класс электромонтер участка транпорта"""

    pass
