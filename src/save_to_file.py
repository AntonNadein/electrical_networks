import os
import shelve
from abc import ABC, abstractmethod


class SaveToFile(ABC):
    """Абстрактный класс для срхранения вакансий в файл."""

    @abstractmethod
    def save_to_file(self, key, value):
        pass


class SaveToFileDB(SaveToFile):
    """Kласс для срхранения экземпляров в файл с помощью shelve
     и десериализации экземпляров из файла."""

    def __init__(self, file_name: str = None) -> None:
        self._file_name = file_name if file_name else "data_base"
        self.__path_to_file = os.path.join(os.path.dirname(__file__), "..", "data", self._file_name)

    def save_to_file(self, key: str, value: object) -> None:
        """
        Добавление в файл экземпляров класса
        :param key: Уникальный ключ для сохранения данных
        :param value: Экземпляр класса
        """
        with shelve.open(self.__path_to_file) as db:
            db[key] = value

    def open_file(self, key: str) -> object:
        """Десериализация одного экземпляра класса по ключу"""
        with shelve.open(self.__path_to_file) as db:
            for d in db:
                if key in d:
                    return db[d]

    def open_file_list(self, key: str) -> list[dict]:
        """Десериализация экземпляра класса по ключу"""
        list_class = []
        with shelve.open(self.__path_to_file) as db:
            for d in db:
                if key in d:
                    list_class.append(db[d])
            return list_class

    def delete_item(self, key: str) -> None:
        """Удаление данных из файла по ключу"""
        with shelve.open(self.__path_to_file) as db:
            for d in db:
                if key in d:
                    del db[key]

    def load_base(self):
        """Функция загрузки базы данных и пвывода количества данных"""
        num = 1
        with shelve.open(self.__path_to_file) as db:
            for d in db:
                num += 1
            return num


if __name__ == '__main__':
    # for i in range(5):
    #     emp = "emp_" + str(i)
    #     print(emp)
    #     dict_3 = {'name': "Ivan" + str(i), 'surname': "Sidorov", 'patronymic': "Petrovich", 'age': 23, 'base_salary': 25000}
    #     emp_3 = Employee.add_employee(dict_3)
    #     bd = SaveToFileDB()
    #     bd.save_to_file(emp, dict_3)
    # bd.open_file("emp")
    # bd.delete_item("emp_1")

    bd = SaveToFileDB()
    a = bd.open_file_list("supervisor_40")
    b = bd.open_file('engineer_41')
    print(a[0])
    print(b)
