import pytest

from src.transport import FreightTransport, PassengerTransport, SpecialTransport


def test_passenger_transport_norm(test_passenger_transport):
    """Тест класса пассажирского транспорта нормальная работа"""
    assert test_passenger_transport[0].name == "УАЗ"
    assert test_passenger_transport[0].purpose == "Пассажироперевозки"
    assert test_passenger_transport[0].engine_power == 87
    assert test_passenger_transport[0].fuel_consumption == 16
    assert test_passenger_transport[0].passenger_capacity == 4
    assert PassengerTransport.passenger_transport == 3


def test_add_passenger_transport(test_dict_passenger_transport):
    """Тест класса пассажирского транспорта бовавление через словарь"""
    transport_4 = PassengerTransport.add_transport(test_dict_passenger_transport)
    assert transport_4.name == "Газ66"
    assert transport_4.passenger_capacity == 6
    assert PassengerTransport.passenger_transport == 4


def test_passenger_transport_error():
    """Тест класса пассажирского транспорта
    ошибка инициализации"""
    with pytest.raises(ValueError):
        PassengerTransport("УАЗ", "Пассажироперевозки", 87, 16, -54)


def test_get_fuel_consumption(test_passenger_transport):
    """Тест базового класса сумма расхода топлива"""
    result = PassengerTransport.get_fuel_consumption(test_passenger_transport)
    assert result == 69


def test_passenger_transport_add(test_passenger_transport):
    """Тест базового класса сложение расхода топлива"""
    var = test_passenger_transport[0] + 1
    assert var.fuel_consumption == 17
    var = 1 + test_passenger_transport[0]
    assert var.fuel_consumption == 17
    var = test_passenger_transport[0] + test_passenger_transport[1]
    assert var.fuel_consumption == 44


def test_passenger_transport_sub(test_passenger_transport):
    """Тест базового класса вычитание расхода топлива"""
    var = test_passenger_transport[0] - 1
    assert var.fuel_consumption == 15
    var = 20 - test_passenger_transport[0]
    assert var.fuel_consumption == 4
    var = test_passenger_transport[1] - test_passenger_transport[0]
    assert var.fuel_consumption == 12


def test_passenger_transport_check_isinstance(test_passenger_transport):
    """Тест базового класса ошибка int"""
    with pytest.raises(ArithmeticError):
        print(test_passenger_transport[0] + "1")


def test_freight_transport_norm(test_freight_transport):
    """Класс транспорта для грузоперевозок"""
    assert test_freight_transport.name == "Газ"
    assert test_freight_transport.purpose == "Грузоперевозки"
    assert test_freight_transport.engine_power == 87
    assert test_freight_transport.fuel_consumption == 16
    assert test_freight_transport.empty_weight == 4
    assert test_freight_transport.cargo_weight == 4
    assert test_freight_transport.max_mass == 8
    assert test_freight_transport.remaining_weight == 0
    assert FreightTransport.freight_transport == 1


def test_freight_transport_empty_weight_error():
    """Тест класса транспорта для грузоперевозок
    ошибка инициализации"""
    with pytest.raises(ValueError):
        FreightTransport("УАЗ", "Пассажироперевозки", 87, 16, -54, 5)


def test_freight_transport_cargo_weight_error():
    """Тест класса транспорта для грузоперевозок
    ошибка инициализации"""
    with pytest.raises(ValueError):
        FreightTransport("УАЗ", "Пассажироперевозки", 87, 16, 4, -5)


def test_freight_transport_checking_weight(test_freight_transport, capsys):
    """Тест класса транспорта для грузоперевозок контроль веса"""
    test_freight_transport.checking_weight(3)
    assert test_freight_transport.remaining_weight == 1
    test_freight_transport.checking_weight([1, "2", 3])
    assert test_freight_transport.remaining_weight == 0
    test_freight_transport.checking_weight(5)
    message = capsys.readouterr()
    assert message.out.strip() == "Допустимая масса груза превышена"
    assert test_freight_transport.remaining_weight == 0


def test_special_transport_norm(test_special_transport):
    """Класс спецтехники"""
    assert test_special_transport.name == "Газ"
    assert test_special_transport.purpose == "Автовышка"
    assert test_special_transport.engine_power == 87
    assert test_special_transport.fuel_consumption == 16
    assert test_special_transport.engine_hours == 4
    assert test_special_transport.engine_hours_fuel_consumption == 1
    assert SpecialTransport.special_transport == 1


def test_special_transport_get_set(test_special_transport, capsys):
    """Класс спецтехники тест геттера и сеттера"""
    test_special_transport.engine_hours_fuel_consumption = 1.2
    assert test_special_transport.engine_hours_fuel_consumption == 1.2
    test_special_transport.engine_hours_fuel_consumption = "1.3"
    message = capsys.readouterr()
    assert message.out.strip() == "Моточасы должны быть в числовом формате"
    assert test_special_transport.engine_hours_fuel_consumption == 1.2


def test_special_transport_increase_engine_hours(test_special_transport, capsys):
    """Класс спецтехники тест геттера и сеттера"""
    test_special_transport.increase_engine_hours(1.1)
    assert test_special_transport.engine_hours == 5.1
    test_special_transport.increase_engine_hours("1.3")
    message = capsys.readouterr()
    assert message.out.strip() == "Моточасы должны быть в числовом формате"
    assert test_special_transport.engine_hours == 5.1


def test_special_transport_error():
    """Тест класса транспорта для грузоперевозок
    ошибка инициализации"""
    with pytest.raises(ValueError):
        SpecialTransport("Газ", "Автовышка", 107, 26, -54, 5)
