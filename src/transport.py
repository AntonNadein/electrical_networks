from abc import ABC, abstractmethod


class BaseTransport(ABC):
    """Абстрактный класс для транспорта"""

    @classmethod
    @abstractmethod
    def add_transport(cls, dicts):
        pass

    @abstractmethod
    def __add__(self, other):
        pass


class Transport:
    """Базовый класс для транспорта"""

    name: str
    purpose: str
    engine_power: int
    fuel_consumption: float

    def __init__(self, name: str, purpose: str, engine_power: int, fuel_consumption: float) -> None:
        self.name = name
        self.purpose = purpose
        self.engine_power = engine_power
        self.fuel_consumption = fuel_consumption

    @classmethod
    def add_transport(cls, dicts):
        """Добавление транспорта из словаря"""
        return cls(**dicts)

    @staticmethod
    def __check_isinstance_fuel_consumption(other):
        """Проверка принадлежности значения топлива"""
        if not isinstance(other, (int, Transport)):
            raise ArithmeticError("Правый операнд должен быть типом int")
        num_fuel = other
        if isinstance(other, Transport):
            return num_fuel.fuel_consumption
        return num_fuel

    def __add__(self, other):
        """Добавление расхода топлива"""
        num_fuel = self.__check_isinstance_fuel_consumption(other)
        return Transport(self.name, self.purpose, self.engine_power, self.fuel_consumption + num_fuel)

    def __radd__(self, other):
        """Добавление расхода топлива"""
        return self + other

    def __sub__(self, other):
        """Убавление расхода топлива"""
        num_fuel = self.__check_isinstance_fuel_consumption(other)
        return Transport(self.name, self.purpose, self.engine_power, self.fuel_consumption - num_fuel)

    def __rsub__(self, other):
        """Убавление расхода топлива"""
        num_fuel = self.__check_isinstance_fuel_consumption(other)
        return Transport(self.name, self.purpose, self.engine_power, num_fuel - self.fuel_consumption)

    @staticmethod
    def get_fuel_consumption(transport_list: list):
        """Подсчет расхода топлива из списка транспорта"""
        fuel = 0
        for i in transport_list:
            fuel += i.fuel_consumption
        return fuel


class PassengerTransport(Transport):
    """Класс транспорта для перевозки персонала"""

    passenger_transport = 0

    passenger_capacity: int

    def __init__(
        self, name: str, purpose: str, engine_power: int, fuel_consumption: float, passenger_capacity: int
    ) -> None:
        super().__init__(name, purpose, engine_power, fuel_consumption)
        if passenger_capacity < 0:
            raise ValueError("Количетво пассажиров не может быть отрицательным")
        self.passenger_capacity = passenger_capacity
        PassengerTransport.passenger_transport += 1


class FreightTransport(Transport):
    """Класс транспорта для грузоперевозок"""

    freight_transport = 0

    passenger_capacity: int

    def __init__(
        self,
        name: str,
        purpose: str,
        engine_power: int,
        fuel_consumption: float,
        empty_weight: float | int,
        cargo_weight: float | int,
    ) -> None:
        super().__init__(name, purpose, engine_power, fuel_consumption)
        if empty_weight < 0:
            raise ValueError("Порожняя масса не может быть отрицательной")
        self.empty_weight = empty_weight
        if cargo_weight < 0:
            raise ValueError("Порожняя масса не может быть отрицательной")
        self.cargo_weight = cargo_weight
        self.max_mass = self.empty_weight + self.cargo_weight
        self.remaining_weight = 0  # отсаток веса до заполнения
        FreightTransport.freight_transport += 1

    def __logic_check(self, check_weight):
        """Вспомогательная логика для контроля веса"""
        self.remaining_weight = self.cargo_weight - check_weight
        if self.remaining_weight < 0:
            self.remaining_weight = 0
            print("Допустимая масса груза превышена")

    def checking_weight(self, check_weight):
        """Функция контроля веса"""
        if type(check_weight) in (float, int):
            self.__logic_check(check_weight)
        elif type(check_weight) is list:
            remaining_weight = 0
            for i in check_weight:
                if type(i) in (float, int):
                    remaining_weight += i
            self.__logic_check(remaining_weight)


class SpecialTransport(Transport):
    """Класс спецтехники"""

    special_transport = 0

    passenger_capacity: int

    def __init__(
        self,
        name: str,
        purpose: str,
        engine_power: int,
        fuel_consumption: float,
        engine_hours: float | int,
        engine_hours_fuel_consumption: float | int,
    ) -> None:
        super().__init__(name, purpose, engine_power, fuel_consumption)
        if engine_hours < 0:
            raise ValueError("Моточасы не могут быть отрицательными")
        self.engine_hours = engine_hours
        self.__engine_hours_fuel_consumption = (
            engine_hours_fuel_consumption if engine_hours_fuel_consumption > 0 else 0
        )
        SpecialTransport.special_transport += 1

    def increase_engine_hours(self, add_engine_hours):
        """Функция для добавления моточасов"""
        if type(add_engine_hours) in (float, int):
            self.engine_hours += add_engine_hours
        else:
            print("Моточасы должны быть в числовом формате")

    @property
    def engine_hours_fuel_consumption(self):
        """Геттер для получения расхода топлива моточасов"""
        return self.__engine_hours_fuel_consumption

    @engine_hours_fuel_consumption.setter
    def engine_hours_fuel_consumption(self, new_value):
        """Сеттер для изменения расхода топлива моточасов"""
        if type(new_value) in (float, int):
            self.__engine_hours_fuel_consumption = new_value
        else:
            print("Моточасы должны быть в числовом формате")


# if __name__ == "__main__":
#     transp_1 = PassengerTransport("УАЗ", "Пассажироперевозки", 87, 16, 4)
#     transp_2 = PassengerTransport("Газ66", "Бригадный", 95, 28, 5)
#     transp_4 = PassengerTransport("Газ66", "Бригадный", 95, 25, 5)
#     qtransp_1 = Transport("УАЗ", "Пассажироперевозки", 87, 15)
#     qtransp_2 = Transport("Газ66", "Бригадный", 95, 20)
#     dict_transp_3 = {'name': "Газ66", 'purpose': "Бригадный", 'engine_power': 95, 'fuel_consumption': 25,
#                      'passenger_capacity': 6}
#     transp_3 = PassengerTransport.add_transport(dict_transp_3)
#     cargo_transp_1 = FreightTransport("УАЗ", "Грузоперевозки", 87, 16, 4, 4)
#     spec_transp_1 = SpecialTransport("Газ", "Автовышка", 87, 16, 4, 1)
#
#     # listok_1 = [transp_1, transp_2, transp_3, transp_4]
#     # print(Transport.get_fuel_consumption(listok_1))
#     # # cdds = 100 - transp_1
#     # print((100 - transp_1).fuel_consumption)
#     # # c3 = 100 + transp_1 + transp_2 + 100
#     # # print(c3.fuel_consumption)
#     # print(PassengerTransport.passenger_transport)
#     # print(SpecialTransport.special_transport)
#     # print(cargo_transp_1.сhecking_weight(3))
#     # print(cargo_transp_1.remaining_weight)
#     spec_transp_1.increase_engine_hours(3)
#     print(spec_transp_1.engine_hours)
#     print(spec_transp_1.engine_hours_fuel_consumption)
#     spec_transp_1.engine_hours_fuel_consumption = 5
#     print(spec_transp_1.engine_hours_fuel_consumption)
