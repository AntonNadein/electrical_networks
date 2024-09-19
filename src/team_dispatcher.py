from src.class_employee import Specialist, Supervisor
from src.class_team import Team


class TeamOfDispatcher(Team):
    """Диспетчерский участок"""

    pass


class SupervisorDispatcher(Supervisor, Specialist):
    """Класс руководитель дисетчерской службы"""

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


class Dispatcher(Specialist):
    """Класс диспетчер"""

    job_coefficient = 1.3
