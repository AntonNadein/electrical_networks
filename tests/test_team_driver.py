from src.team_driver import DriverProfessional, Mechanic


def test_mechanic(test_employee_data_1, test_passenger_transport):
    supervisor = Mechanic(
        "Ivan", "Ivanov", "Ivanovich", 40, 20000, [test_employee_data_1], list(test_passenger_transport)
    )
    assert supervisor.number_of_subordinates == 1
    assert supervisor.number_of_transport == 3
    assert str(supervisor) == "Ivanov Ivan Ivanovich Возраст:40 Зарплата: 30000.0руб."


def test_driver_professional(test_employee_data_1, test_passenger_transport):
    driver = DriverProfessional("Ivan", "Ivanov", "Ivanovich", 40, 20000, list(test_passenger_transport))
    assert driver.number_of_transport == 3
    assert str(driver) == "Ivanov Ivan Ivanovich Возраст:40 Зарплата: 22000.0руб."
