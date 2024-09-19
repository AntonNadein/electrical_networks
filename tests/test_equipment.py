import pytest

from src.equipment import Transformer


def test_electrical_equipment_norm(test_electrical_equipment):
    """Тест нормальной работы класса электрооборудование"""
    assert test_electrical_equipment.name == "электропибор"
    assert test_electrical_equipment.assignment == "электропотребления"
    assert test_electrical_equipment.voltage_kilovolt == 0.23


def test_oil_filled_equipment_norm(test_oil_filled_equipment):
    """Тест нормальной работы класса маслонаполненное оборудование"""
    assert test_oil_filled_equipment.name == "маслонаполненное оборудование"
    assert test_oil_filled_equipment.assignment == "гашение дуги в масле"
    assert test_oil_filled_equipment.voltage_kilovolt == 220
    assert test_oil_filled_equipment.weight_oil == 24


def test_transformer_norm(test_transformer):
    """Тест нормальной работы класса трансформатор"""
    assert test_transformer.name == "ТМ-400"
    assert test_transformer.assignment == "трасформации"
    assert test_transformer.voltage_kilovolt == 10
    assert test_transformer.weight_oil == 0.7
    assert test_transformer.voltage_transformations == 0.4
    assert test_transformer.power_kVA == 400


def test_oil_switch_norm(test_oil_switch):
    """Тест нормальной работы класса выключатель"""
    assert test_oil_switch.name == "МВ-110"
    assert test_oil_switch.assignment == "отключение сети"
    assert test_oil_switch.voltage_kilovolt == 110
    assert test_oil_switch.weight_oil == 4
    assert test_oil_switch.voltage_switch == 124000
    assert test_oil_switch.control == "дистанционное"


def test_metering_device_norm(test_metering_device):
    """Тест нормальной работы класса прибор учета"""
    assert test_metering_device.name == "Прибор учета"
    assert test_metering_device.assignment == "подсчет киловатт"
    assert test_metering_device.voltage_kilovolt == 0.4
    assert test_metering_device.phases == 3
    assert str(test_metering_device) == "Прибор учета - 0.4кВ Предназначение: подсчет киловатт"


def test_electrical_equipment_error():
    """Тест ошибки ввода отрицательного значения"""
    with pytest.raises(ValueError, match="Значение не может быть отрицательным"):
        return Transformer("ТМ-400", "трасформации", 10, 0.7, 0.4, -400)
