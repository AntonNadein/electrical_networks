from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import Qt

from src.program_shell import SoftwareShell


class ProgramManagement(SoftwareShell):
    def __init__(self):
        super(SoftwareShell).__init__()
        self.page_number = 0
        self.list_box= []
        self.data = {}

    def save_data(self):
        if self.page_number == 1:
            self.save_data_manadger()
        elif self.page_number == 2:
            self.save_data_engenear()
        elif self.page_number == 3:
            self.save_data_master()
        elif self.page_number == 4:
            self.save_data_supervisor_control()
        elif self.page_number == 5:
            self.save_data_mechanic()
        elif self.page_number == 6:
            self.save_data_supervisor_control()
        elif self.page_number == 7:
            self.save_data_electrician()
        elif self.page_number == 8:
            self.save_data_driver()
        elif self.page_number == 9:
            self.save_data_inspector()
        elif self.page_number == 10:
            self.save_data_electrician_control()
        elif self.page_number == 11:
            self.save_data_dispetcher()
        elif self.page_number == 12:
            self.save_data_transformer()
        elif self.page_number == 13:
            self.save_data_switch()
        elif self.page_number == 14:
            self.save_data_metering_device()
        elif self.page_number == 15:
            self.save_data_passenger_transport()
        elif self.page_number == 16:
            self.save_data_freight_transport()
        elif self.page_number == 17:
            self.save_data_special_transport()

    def click_item_button(self):
        """Фунция выбора спин бокса и передачи сигнала нажатия на кнопки"""
        # Действие выбора спин бокса (сделать одельной функцией на каждый виджет)
        self.spinBox_ptr_1.textChanged.connect((lambda num: setattr(self, 'pt', num)))
        self.doubleSpinBox_ptr_2.textChanged.connect(lambda num: setattr(self, 'pt_1', num))
        self.spinBox_ptr_3.textChanged.connect((lambda num: setattr(self, 'pt_2', num)))

    def save_data_manadger(self):
        pass

    def save_data_engenear(self):
        pass

    def save_data_master(self):
        pass

    def save_data_supervisor_control(self):
        pass

    def save_data_mechanic(self):
        pass

    def save_data_supervisor_dispatcher(self):
        pass

    def save_data_electrician(self):
        pass

    def save_data_driver(self):
        pass

    def save_data_inspector(self):
        pass

    def save_data_electrician_control(self):
        pass

    def save_data_dispetcher(self):
        pass

    def save_data_transformer(self):
        pass

    def save_data_switch(self):
        pass

    def save_data_metering_device(self):
        pass

    def save_data_passenger_transport(self):
        """Сохранение данных при нажатии на кнопку 'создать'"""
        data = {
            'name': self.text_transport_name.toPlainText(),
            'purpose': self.text_transport_purpose.toPlainText(),
            'engine_power': self.pt,
            'fuel_consumption': self.pt_1,
            'passenger_capacity': self.pt_2
        }
        print(data)  # Здесь можно добавить сохранение данных в файл или базу данных

    def save_data_freight_transport(self):
        pass

    def save_data_special_transport(self):
        pass


    def check_box_driver(self):
        """Фунция получения и передачи сигнала чек.бокса для класса водитель"""
        self.checkBox_driver_a.stateChanged.connect(self.__show_state_a)
        self.checkBox_driver_b.stateChanged.connect(self.__show_state_b)
        self.checkBox_driver_c.stateChanged.connect(self.__show_state_c)
        self.checkBox_driver_d.stateChanged.connect(self.__show_state_d)
        self.checkBox_driver_e.stateChanged.connect(self.__show_state_e)

    def check_box_mechanic(self):
        """Фунция получения и передачи сигнала чек.бокса для класса механик"""
        self.checkBox_driver_a_2.stateChanged.connect(self.__show_state_a)
        self.checkBox_driver_b_2.stateChanged.connect(self.__show_state_b)
        self.checkBox_driver_c_2.stateChanged.connect(self.__show_state_c)
        self.checkBox_driver_d_2.stateChanged.connect(self.__show_state_d)
        self.checkBox_driver_e_2.stateChanged.connect(self.__show_state_e)

    def check_box_manadger(self):
        """Фунция получения и передачи сигнала чек.бокса для класса начальник"""
        self.checkBox_driver_a_3.stateChanged.connect(self.__show_state_a)
        self.checkBox_driver_b_3.stateChanged.connect(self.__show_state_b)
        self.checkBox_driver_c_3.stateChanged.connect(self.__show_state_c)
        self.checkBox_driver_d_3.stateChanged.connect(self.__show_state_d)
        self.checkBox_driver_e_3.stateChanged.connect(self.__show_state_e)

    def check_box_engenear(self):
        """Фунция получения и передачи сигнала чек.бокса для класса инженер"""
        self.checkBox_driver_a_4.stateChanged.connect(self.__show_state_a)
        self.checkBox_driver_b_4.stateChanged.connect(self.__show_state_b)
        self.checkBox_driver_c_4.stateChanged.connect(self.__show_state_c)
        self.checkBox_driver_d_4.stateChanged.connect(self.__show_state_d)
        self.checkBox_driver_e_4.stateChanged.connect(self.__show_state_e)



    def __show_state_a(self, s):
        print(s == Qt.CheckState.Checked.value)
        if s == Qt.CheckState.Checked.value:
            self.list_box.append("A")
            print(self.list_box)
        else:
            b = self.list_box.index("A")
            print(b)
            self.list_box.pop(b)
            print(self.list_box)

    def __show_state_b(self, s):
        if s == Qt.CheckState.Checked.value:
            self.list_box.append("B")
            print(self.list_box)
        else:
            b = self.list_box.index("B")
            print(b)
            self.list_box.pop(b)
            print(self.list_box)

    def __show_state_c(self, s):
        if s == Qt.CheckState.Checked.value:
            self.list_box.append("C")
            print(self.list_box)
        else:
            b = self.list_box.index("C")
            print(b)
            self.list_box.pop(b)
            print(self.list_box)

    def __show_state_d(self, s):
        if s == Qt.CheckState.Checked.value:
            self.list_box.append("D")
            print(self.list_box)
        else:
            b = self.list_box.index("D")
            print(b)
            self.list_box.pop(b)
            print(self.list_box)

    def __show_state_e(self, s):
        if s == Qt.CheckState.Checked.value:
            self.list_box.append("E")
            print(self.list_box)
        else:
            b = self.list_box.index("E")
            print(b)
            self.list_box.pop(b)
            print(self.list_box)

