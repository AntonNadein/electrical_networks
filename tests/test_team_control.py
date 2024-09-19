from src.team_control import Inspector, SupervisorControl


def test_supervisor_control(test_employee_data_1, test_metering_device):
    supervisor = SupervisorControl(
        "Ivan", "Ivanov", "Ivanovich", 40, 20000, [test_employee_data_1], [test_metering_device]
    )
    assert supervisor.number_of_subordinates == 1
    assert supervisor.number_of_equipment == 1


def test_inspector(test_employee_data_1, test_metering_device):
    inspector = Inspector("Ivan", "Ivanov", "Ivanovich", 40, 20000, [test_metering_device])
    assert inspector.number_of_equipment == 1
