from src.team_dispatcher import Dispatcher, SupervisorDispatcher


def test_supervisor_control(test_employee_data_1, test_metering_device):
    supervisor = SupervisorDispatcher(
        "Ivan", "Ivanov", "Ivanovich", 40, 20000, [test_employee_data_1], [test_metering_device]
    )
    assert supervisor.number_of_subordinates == 1
    assert supervisor.number_of_equipment == 1
    assert str(supervisor) == "Ivanov Ivan Ivanovich Возраст:40 Зарплата: 30000.0руб."


def test_inspector(test_employee_data_1, test_metering_device):
    dispatcher = Dispatcher("Ivan", "Ivanov", "Ivanovich", 40, 20000, [test_metering_device])
    assert dispatcher.number_of_equipment == 1
    assert str(dispatcher) == "Ivanov Ivan Ivanovich Возраст:40 Зарплата: 26000.0руб."
