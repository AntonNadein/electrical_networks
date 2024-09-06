from src.class_employee import Employee


class Team:
    """Базовый класс бригад"""

    work_being_performed: str
    leader: list
    function_leader: str
    personal: list
    max_person: int
    number_of_person: int

    def __init__(
        self, work_being_performed: str, function_leader: str, leader: Employee, personal: list, max_person: int
    ) -> None:
        self.work_being_performed = work_being_performed
        self.leader = leader if leader else []
        self.function_leader = function_leader
        self.personal = personal if personal else []
        self.max_person = max_person
        self.personal = self.len_max_person()

    def __str__(self):
        """Вывод информации для пользователя"""
        a = []
        for i in self.personal:
            a.append(str(i))
        return f"{self.work_being_performed}. {self.function_leader}: {self.leader} Подчиненные: {" ".join(a)}"

    def len_max_person(self):
        """Проверка отсутствия превышения персрнала"""
        if len(self.personal) <= self.max_person:
            return self.personal
        else:
            raise TypeError("Превышено количество человек в бригаде")

    def add_personal(self, personal: Employee):
        """Добавленияе нового персрнала"""
        if isinstance(personal, Employee) and len(self.personal) < self.max_person:
            return self.personal.append(personal)
        else:
            raise TypeError("Превышено количество человек в бригаде")


# if __name__ == "__main__":
#     electrician_1 = Employee("Petr", "Petrov", "Ivanovich", 20)
#     bri1 = Team("jgbc", "мастер", ['vfsnth'], [electrician_1], 1)
# electrician_2 = Employee("Petr", "Petrov", "Ivanovich", 20)
# bri1.add_personal(electrician_2)
# print(bri1)
