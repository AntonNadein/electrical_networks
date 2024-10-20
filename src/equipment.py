from abc import ABC, abstractmethod


class BaseEquipment(ABC):
    """Абстрактный класс для транспорта"""

    @classmethod
    @abstractmethod
    def add_equipment(cls, dicts):
        pass

    @abstractmethod
    def _check_negative_value(self, value):
        pass


class ElectricalEquipment(BaseEquipment):
    """Базовый класс электрооборудования"""

    name: str
    assignment: str  # назначение
    voltage_kilovolt: float | int

    def __init__(self, name: str, assignment: str, voltage_kilovolt: float | int) -> None:
        self.name = name
        self.assignment = assignment
        self.voltage_kilovolt = self._check_negative_value(voltage_kilovolt)

    @classmethod
    def add_equipment(cls, dicts):
        """Добавление оборудования из словаря"""
        return cls(**dicts)

    def _check_negative_value(self, value: float | int) -> float | int:
        """Функция проверки отрицательного значения"""
        if value < 0:
            raise ValueError("Значение не может быть отрицательным")
        else:
            return value

    def __repr__(self):
        """Вывод информации для разработчика"""
        return (
            f"{self.__class__.__name__}({self.name}, {self.assignment}, {self.voltage_kilovolt},"
        )

    def __str__(self):
        """Вывод информации для пользователя"""
        return f"{self.name} - {self.voltage_kilovolt}кВ Предназначение: {self.assignment}"


class OilFilledEquipment(ElectricalEquipment):
    """Класс маслонаполненного электрооборудования"""

    weight_oil: float

    def __init__(self, name: str, assignment: str, voltage_kilovolt: float | int, weight_oil: float) -> None:
        super().__init__(name, assignment, voltage_kilovolt)
        self.weight_oil = self._check_negative_value(weight_oil)


class Transformer(OilFilledEquipment):
    """Класс маслонаполненного электрооборудования: трансформатор"""

    voltage_transformation: str
    power_kVA: int

    def __init__(
        self,
        name: str,
        assignment: str,
        voltage_kilovolt: float | int,
        weight_oil: float | int,
        voltage_transformations: float | int,
        power_kva: int,
    ) -> None:
        super().__init__(name, assignment, voltage_kilovolt, weight_oil)
        self.voltage_transformations = self._check_negative_value(voltage_transformations)
        self.power_kva = self._check_negative_value(power_kva)


class Switch(OilFilledEquipment):
    """Класс маслонаполненного электрооборудования: выключатель"""

    voltage_switch: int
    control: str  # тип управления

    def __init__(
        self,
        name: str,
        assignment: str,
        voltage_kilovolt: float | int,
        weight_oil: float | int,
        voltage_switch: int,
        control: str,
    ) -> None:
        super().__init__(name, assignment, voltage_kilovolt, weight_oil)
        self.voltage_switch = self._check_negative_value(voltage_switch)
        self.control = control


class MeteringDevice(ElectricalEquipment):
    """Измерительное электрооборудование"""

    phases: int  # фазность

    def __init__(self, name: str, assignment: str, voltage_kilovolt: float | int, phases: int) -> None:
        super().__init__(name, assignment, voltage_kilovolt)
        self.phases = self._check_negative_value(phases)


if __name__ == "__main__":
    asdfad = ElectricalEquipment("nngbg", "sfdsdf", 20)
    asdfad1 = Transformer("nngbg", "sfdsdf", 50, 5000, 50, 160)
    print(asdfad.voltage_kilovolt)
    d = {'name': 'testq', 'assignment':'test1', 'voltage_kilovolt': 50, 'weight_oil': 110, 'voltage_transformations': '50', 'power_kva': 160}
    ob1 = Transformer.add_equipment(d)
    print(ob1.voltage_transformations)