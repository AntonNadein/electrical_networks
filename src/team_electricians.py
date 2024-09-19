from src.class_employee import Driver, Employee, Supervisor
from src.class_team import Team


class TeamOfElectricians(Team):
    """Бригада монтерского участка"""

    pass


class MasterElectric(Supervisor):
    """Класс Мастер"""

    job_coefficient = 1.5


class Electrician(Employee):
    """Класс Электромонтер"""

    pass


class ElectricianDriver(Driver):
    """Класс Электромонтер-водитель"""

    job_coefficient = 1.2
