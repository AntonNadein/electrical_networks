from abc import ABC, abstractmethod


class BaseEmployee(ABC):

    @classmethod
    @abstractmethod
    def add_employee(cls, dicts):
        pass

    @abstractmethod
    def salary(self):
        pass
