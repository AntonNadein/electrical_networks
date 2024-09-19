from src.team_supervisor import Engineer, SupervisorManager


def test_supervisor_manager(test_employee_data_1, test_passenger_transport, test_transformer):
    supervisor = SupervisorManager(
        "Ivan",
        "Ivanov",
        "Ivanovich",
        40,
        20000,
        [test_employee_data_1],
        [test_transformer],
        list(test_passenger_transport),
        "B",
    )
    assert supervisor.number_of_subordinates == 1
    assert supervisor.number_of_equipment == 1
    assert supervisor.number_of_transport == 3
    assert str(supervisor) == "Ivanov Ivan Ivanovich Возраст:40 Зарплата: 50000.0руб."


def test_engineer(test_employee_data_1, test_passenger_transport, test_transformer):
    engineer = Engineer(
        "Ivan",
        "Ivanov",
        "Ivanovich",
        40,
        20000,
        [test_employee_data_1],
        [test_transformer],
        list(test_passenger_transport),
        "B",
    )
    assert engineer.number_of_subordinates == 1
    assert engineer.number_of_equipment == 1
    assert engineer.number_of_transport == 3
    assert str(engineer) == "Ivanov Ivan Ivanovich Возраст:40 Зарплата: 42000.0руб."
