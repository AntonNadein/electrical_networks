from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import Qt

from src.program_shell import SoftwareShell


class ProgramManagement(SoftwareShell):
    def __init__(self):
        super(SoftwareShell).__init__()
        self.page_number = 0
        self.list_box = []
        self.data = {}
        self.list_combo_box_employee = ["", "", "", "", ""]
        self.list_combo_box_transport = ["", "", "", "", ""]
        self.list_combo_box_equipment = ["", "", "", "", ""]
        self.data = {}
        self.original_values_combo_box = {}
        self.original_combo_box = {}

    def save_data(self):
        if self.page_number == 1:
            self.save_data_manager()
        elif self.page_number == 2:
            self.save_data_engineer()
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

    def save_data_manager(self):
        """Сохранение данных начальника при нажатии на кнопку 'создать'"""
        print(self.list_combo_box_equipment)
        while "" in self.list_combo_box_employee:
            index_none = self.list_combo_box_employee.index("")
            self.list_combo_box_employee.pop(index_none)
        while "" in self.list_combo_box_equipment:
            index_none = self.list_combo_box_equipment.index("")
            self.list_combo_box_equipment.pop(index_none)
        self.data = {
            'name': self.text_manager_ln.toPlainText(),
            'surname': self.text_manager_fn.toPlainText(),
            'patronymic': self.text_manager_pn.toPlainText(),
            'age': self.text_manager_age.toPlainText(),
            'base_salary': self.text_manager_salary.toPlainText(),
            'category_driver_license': self.list_box,
            'subordinates': self.list_combo_box_employee,  # подчиненные
            'equipment_list': self.list_combo_box_equipment  # оборудование
        }
        print(self.data)
        self.clear_manager()

    def save_data_engineer(self):
        """Сохранение данных начальника при нажатии на кнопку 'создать'"""
        print(self.list_combo_box_equipment)
        while "" in self.list_combo_box_employee:
            index_none = self.list_combo_box_employee.index("")
            self.list_combo_box_employee.pop(index_none)
        while "" in self.list_combo_box_equipment:
            index_none = self.list_combo_box_equipment.index("")
            self.list_combo_box_equipment.pop(index_none)
        self.data = {
            'name': self.text_engineer_ln.toPlainText(),
            'surname': self.text_engineer_fn.toPlainText(),
            'patronymic': self.text_engineer_pn.toPlainText(),
            'age': self.text_engineer_age.toPlainText(),
            'base_salary': self.text_engineer_salary.toPlainText(),
            'category_driver_license': self.list_box,
            'subordinates': self.list_combo_box_employee,  # подчиненные
            'equipment_list': self.list_combo_box_equipment  # оборудование
        }
        print(self.data)
        self.clear_engineer()

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

    def check_box_manager(self):
        """Фунция получения и передачи сигнала чек.бокса для класса начальник"""
        self.checkBox_driver_a_3.stateChanged.connect(self.__show_state_a)
        self.checkBox_driver_b_3.stateChanged.connect(self.__show_state_b)
        self.checkBox_driver_c_3.stateChanged.connect(self.__show_state_c)
        self.checkBox_driver_d_3.stateChanged.connect(self.__show_state_d)
        self.checkBox_driver_e_3.stateChanged.connect(self.__show_state_e)

    def check_box_engineer(self):
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

    def list_combo_box_manager_add(self): # вставка items из файла или БД
        """Функция управления и вывода данных комбо бокса"""
        self.original_values_combo_box['combo_box_manager_employee'] = ["", "One", "Two", "Three"]
        self.original_values_combo_box['combo_box_manager_equipment'] = ["", "One", "Two", "Three"]

        self.comboBox_manager_1.addItems(self.original_values_combo_box['combo_box_manager_employee'])
        self.comboBox_manager_2.addItems(self.original_values_combo_box['combo_box_manager_employee'])
        self.comboBox_manager_3.addItems(self.original_values_combo_box['combo_box_manager_employee'])
        self.comboBox_manager_4.addItems(self.original_values_combo_box['combo_box_manager_employee'])
        self.comboBox_manager_5.addItems(self.original_values_combo_box['combo_box_manager_employee'])
        self.comboBox_manager_6.addItems(self.original_values_combo_box['combo_box_manager_equipment'])
        self.comboBox_manager_7.addItems(self.original_values_combo_box['combo_box_manager_equipment'])
        self.comboBox_manager_8.addItems(self.original_values_combo_box['combo_box_manager_equipment'])
        self.comboBox_manager_9.addItems(self.original_values_combo_box['combo_box_manager_equipment'])
        self.comboBox_manager_10.addItems(self.original_values_combo_box['combo_box_manager_equipment'])

        self.original_combo_box['original_combo_box_employee'] = self.comboBox_manager_1.currentText()
        self.original_combo_box['combo_box_manager_equipment'] = self.comboBox_manager_6.currentText()

        self.comboBox_manager_1.currentTextChanged.connect(self.__text_changed1)
        self.comboBox_manager_2.currentTextChanged.connect(self.__text_changed2)
        self.comboBox_manager_3.currentTextChanged.connect(self.__text_changed3)
        self.comboBox_manager_4.currentTextChanged.connect(self.__text_changed4)
        self.comboBox_manager_5.currentTextChanged.connect(self.__text_changed5)
        self.comboBox_manager_6.currentTextChanged.connect(self.__text_changed6)
        self.comboBox_manager_7.currentTextChanged.connect(self.__text_changed7)
        self.comboBox_manager_8.currentTextChanged.connect(self.__text_changed8)
        self.comboBox_manager_9.currentTextChanged.connect(self.__text_changed9)
        self.comboBox_manager_10.currentTextChanged.connect(self.__text_changed10)

    def list_combo_box_engineer_add(self): # вставка items из файла или БД
        """Функция управления и вывода данных комбо бокса"""
        self.original_values_combo_box['combo_box_manager_employee'] = ["", "One", "Two", "Three"]
        self.original_values_combo_box['combo_box_manager_equipment'] = ["", "One", "Two", "Three"]

        self.comboBox_engineer_1.addItems(self.original_values_combo_box['combo_box_manager_employee'])
        self.comboBox_engineer_2.addItems(self.original_values_combo_box['combo_box_manager_employee'])
        self.comboBox_engineer_3.addItems(self.original_values_combo_box['combo_box_manager_employee'])
        self.comboBox_engineer_4.addItems(self.original_values_combo_box['combo_box_manager_employee'])
        self.comboBox_engineer_5.addItems(self.original_values_combo_box['combo_box_manager_employee'])
        self.comboBox_engineer_6.addItems(self.original_values_combo_box['combo_box_manager_equipment'])
        self.comboBox_engineer_7.addItems(self.original_values_combo_box['combo_box_manager_equipment'])
        self.comboBox_engineer_8.addItems(self.original_values_combo_box['combo_box_manager_equipment'])
        self.comboBox_engineer_9.addItems(self.original_values_combo_box['combo_box_manager_equipment'])
        self.comboBox_engineer_10.addItems(self.original_values_combo_box['combo_box_manager_equipment'])

        self.original_combo_box['original_combo_box_employee'] = self.comboBox_engineer_1.currentText()
        self.original_combo_box['combo_box_manager_equipment'] = self.comboBox_engineer_6.currentText()

        self.comboBox_engineer_1.currentTextChanged.connect(self.__text_changed1)
        self.comboBox_engineer_2.currentTextChanged.connect(self.__text_changed2)
        self.comboBox_engineer_3.currentTextChanged.connect(self.__text_changed3)
        self.comboBox_engineer_4.currentTextChanged.connect(self.__text_changed4)
        self.comboBox_engineer_5.currentTextChanged.connect(self.__text_changed5)
        self.comboBox_engineer_6.currentTextChanged.connect(self.__text_changed6)
        self.comboBox_engineer_7.currentTextChanged.connect(self.__text_changed7)
        self.comboBox_engineer_8.currentTextChanged.connect(self.__text_changed8)
        self.comboBox_engineer_9.currentTextChanged.connect(self.__text_changed9)
        self.comboBox_engineer_10.currentTextChanged.connect(self.__text_changed10)

    def __text_changed1(self, s):
        print(s)
        self.list_combo_box_employee[0] = s
        print(self.list_combo_box_employee)

    def __text_changed2(self, s):
        print(s)
        self.list_combo_box_employee[1] = s
        print(self.list_combo_box_employee)

    def __text_changed3(self, s):
        print(s)
        self.list_combo_box_employee[2] = s
        print(self.list_combo_box_employee)

    def __text_changed4(self, s):
        print(s)
        self.list_combo_box_employee[3] = s
        print(self.list_combo_box_employee)

    def __text_changed5(self, s):
        print(s)
        self.list_combo_box_employee[4] = s
        print(self.list_combo_box_employee)

    def __text_changed6(self, s):
        print(s)
        self.list_combo_box_equipment[0] = s
        print(self.list_combo_box_equipment)

    def __text_changed7(self, s):
        print(s)
        self.list_combo_box_equipment[1] = s
        print(self.list_combo_box_equipment)

    def __text_changed8(self, s):
        print(s)
        self.list_combo_box_equipment[2] = s
        print(self.list_combo_box_equipment)

    def __text_changed9(self, s):
        print(s)
        self.list_combo_box_equipment[3] = s
        print(self.list_combo_box_equipment)

    def __text_changed10(self, s):
        print(s)
        self.list_combo_box_equipment[4] = s
        print(self.list_combo_box_equipment)

