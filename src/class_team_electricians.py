from src.class_employee import Employee
from src.class_team import Team


class TeamOfElectricians(Team):
    """Бригада монтерского участка"""

    pass


class MasterElectric(Employee):
    """Класс рабочего 'Мастер'"""

    job_coefficient = 1.5

    number_of_subordinates: int

    def __init__(self, name, surname, patronymic, age, base_salary, number_of_subordinates):
        super().__init__(name, surname, patronymic, age, base_salary)
        self.number_of_subordinates = number_of_subordinates


class Electrician(Employee):
    """Класс рабочего 'Электромонтер'"""

    pass


# if __name__=="__main__":
#     master_1 = MasterElectric("Ivan", "Ivanov", "Ivanovich", 40, 25000, 5)
#     electrician_1 = Electrician("Petr", "Petrov", "Ivanovich", 20)
#     electrician_2 = Electrician("Petr", "Petrov", "Ivanovich", 30)
#     electrician_3 = Electrician("Petr", "Petrov", "Ivanovich", 40, 21000)
#     bri1 = Team("Бригада для ремонта линий","Мастер", master_1, [electrician_1, electrician_2], 3)
#     bri1.add_personal(electrician_3)
#     print(bri1)
