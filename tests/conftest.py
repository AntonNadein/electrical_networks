import pytest

from src.class_employee import Driver, Employee, Specialist, Supervisor
from src.class_team import Team
from src.equipment import ElectricalEquipment, MeteringDevice, OilFilledEquipment, Switch, Transformer
from src.team_electricians import MasterElectric
from src.transport import FreightTransport, PassengerTransport, SpecialTransport


@pytest.fixture
def test_employee_data_1():
    return Employee("Ivan", "Ivanov", "Ivanovich", 40, 40000)


@pytest.fixture
def test_employee_data_2():
    return Employee("Petr", "Ivanov", "Petrovich", 42)


@pytest.fixture
def test_srt_supervisor(test_employee_data_2):
    return Supervisor("Petr", "Jdanov", "Petrovich", 42, 50000, [test_employee_data_2])


@pytest.fixture
def test_team_master(test_employee_data_1):
    return MasterElectric("Ivan", "Ivanov", "Ivanovich", 40, 25000, [test_employee_data_1])


@pytest.fixture
def test_team_data(test_employee_data_1, test_employee_data_2, test_team_master):
    return Team("Рабочая бригада", "Мастрер", test_team_master, [test_employee_data_1, test_employee_data_2], 2)


@pytest.fixture
def test_passenger_transport():
    PassengerTransport.passenger_transport = 0
    transport_1 = PassengerTransport("УАЗ", "Пассажироперевозки", 87, 16, 4)
    transport_2 = PassengerTransport("Газ66", "Бригадный", 95, 28, 6)
    transport_3 = PassengerTransport("Газ66", "Бригадный", 95, 25, 5)
    return transport_1, transport_2, transport_3


@pytest.fixture
def test_dict_passenger_transport():
    return {
        "name": "Газ66",
        "purpose": "Бригадный",
        "engine_power": 95,
        "fuel_consumption": 25,
        "passenger_capacity": 6,
    }


@pytest.fixture
def test_freight_transport():
    FreightTransport.freight_transport = 0
    return FreightTransport("Газ", "Грузоперевозки", 87, 16, 4, 4)


@pytest.fixture
def test_special_transport():
    SpecialTransport.special_transport = 0
    return SpecialTransport("Газ", "Автовышка", 87, 16, 4, 1)


@pytest.fixture
def test_electrical_equipment():
    return ElectricalEquipment("электропибор", "электропотребления", 0.23)


@pytest.fixture
def test_oil_filled_equipment():
    return OilFilledEquipment("маслонаполненное оборудование", "гашение дуги в масле", 220, 24)


@pytest.fixture
def test_transformer():
    return Transformer("ТМ-400", "трасформации", 10, 0.7, 0.4, 400)


@pytest.fixture
def test_oil_switch():
    return Switch("МВ-110", "отключение сети", 110, 4, 124000, "дистанционное")


@pytest.fixture
def test_metering_device():
    return MeteringDevice("Прибор учета", "подсчет киловатт", 0.4, 3)


@pytest.fixture
def test_specialist(test_transformer):
    return Specialist("Petr", "Vasin", "Petrovich", 42, 50000, [test_transformer])


@pytest.fixture
def test_driver(test_freight_transport):
    return Driver("Vasily", "Vasin", "Petrovich", 42, 45000, [test_freight_transport])
