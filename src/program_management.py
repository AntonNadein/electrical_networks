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
            self.save_data_supervisor_dispatcher()
        elif self.page_number == 7:
            self.save_data_electrician()
        elif self.page_number == 8:
            self.save_data_driver()
        elif self.page_number == 9:
            self.save_data_inspector()
        elif self.page_number == 10:
            self.save_data_electrician_control()
        elif self.page_number == 11:
            self.save_data_dispatcher()
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
        """Сохранение данных инжкнера при нажатии на кнопку 'создать'"""
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
        """Сохранение данных мастера при нажатии на кнопку 'создать'"""
        while "" in self.list_combo_box_employee:
            index_none = self.list_combo_box_employee.index("")
            self.list_combo_box_employee.pop(index_none)
        while "" in self.list_combo_box_equipment:
            index_none = self.list_combo_box_equipment.index("")
            self.list_combo_box_equipment.pop(index_none)
        self.data = {
            'name': self.text_master_ln.toPlainText(),
            'surname': self.text_master_fn.toPlainText(),
            'patronymic': self.text_master_pn.toPlainText(),
            'age': self.text_master_age.toPlainText(),
            'base_salary': self.text_master_salary.toPlainText(),
            'subordinates': self.list_combo_box_employee  # подчиненные
        }
        print(self.data)
        self.clear_master()

    def save_data_supervisor_control(self):
        """Сохранение данных инжкнера при нажатии на кнопку 'создать'"""
        while "" in self.list_combo_box_employee:
            index_none = self.list_combo_box_employee.index("")
            self.list_combo_box_employee.pop(index_none)
        while "" in self.list_combo_box_equipment:
            index_none = self.list_combo_box_equipment.index("")
            self.list_combo_box_equipment.pop(index_none)
        self.data = {
            'name': self.text_n_utaa_ln.toPlainText(),
            'surname': self.text_n_utaa_fn.toPlainText(),
            'patronymic': self.text_n_utaa_pn.toPlainText(),
            'age': self.text_n_utaa_age.toPlainText(),
            'base_salary': self.text_n_utaa_salary.toPlainText(),
            'subordinates': self.list_combo_box_employee,  # подчиненные
            'equipment_list': self.list_combo_box_equipment  # оборудование
        }
        print(self.data)
        self.clear_supervisor_control()

    def save_data_mechanic(self):
        """Сохранение данных механика при нажатии на кнопку 'создать'"""
        print(self.list_combo_box_equipment)
        while "" in self.list_combo_box_employee:
            index_none = self.list_combo_box_employee.index("")
            self.list_combo_box_employee.pop(index_none)
        while "" in self.list_combo_box_transport:
            index_none = self.list_combo_box_transport.index("")
            self.list_combo_box_transport.pop(index_none)
        self.data = {
            'name': self.text_mechanic_ln.toPlainText(),
            'surname': self.text_mechanic_fn.toPlainText(),
            'patronymic': self.text_mechanic_pn.toPlainText(),
            'age': self.text_mechanic_age.toPlainText(),
            'base_salary': self.text_mechanic_salary.toPlainText(),
            'category_driver_license': self.list_box,
            'subordinates': self.list_combo_box_employee,  # подчиненные
            'transport_list': self.list_combo_box_transport  # транспорт
        }
        print(self.data)
        self.clear_mechanic()

    def save_data_supervisor_dispatcher(self):
        """Сохранение данных начальника одг при нажатии на кнопку 'создать'"""
        print(self.list_combo_box_equipment)
        while "" in self.list_combo_box_employee:
            index_none = self.list_combo_box_employee.index("")
            self.list_combo_box_employee.pop(index_none)
        while "" in self.list_combo_box_equipment:
            index_none = self.list_combo_box_equipment.index("")
            self.list_combo_box_equipment.pop(index_none)
        self.data = {
            'name': self.text_disp_ln_2.toPlainText(),
            'surname': self.text_disp_fn_2.toPlainText(),
            'patronymic': self.text_disp_pn_2.toPlainText(),
            'age': self.text_disp_age_2.toPlainText(),
            'base_salary': self.text_disp_salary_2.toPlainText(),
            'subordinates': self.list_combo_box_employee,  # подчиненные
            'equipment_list': self.list_combo_box_equipment  # оборудование
        }
        print(self.data)
        self.clear_supervisor_dispatcher()

    def save_data_electrician(self):
        """Сохранение данных электромонтера при нажатии на кнопку 'создать'"""
        self.data = {
            'name': self.text_el_monter_ln.toPlainText(),
            'surname': self.text_el_monter_fn.toPlainText(),
            'patronymic': self.text_el_monter_pn.toPlainText(),
            'age': self.text_el_monter_age.toPlainText(),
            'base_salary': self.text_el_monter_salary.toPlainText(),
        }
        print(self.data)
        self.clear_electrician()


    def save_data_driver(self):
        """Сохранение данных водителя при нажатии на кнопку 'создать'"""
        print(self.list_combo_box_equipment)
        while "" in self.list_combo_box_employee:
            index_none = self.list_combo_box_employee.index("")
            self.list_combo_box_employee.pop(index_none)
        while "" in self.list_combo_box_transport:
            index_none = self.list_combo_box_transport.index("")
            self.list_combo_box_transport.pop(index_none)
        self.data = {
            'name': self.text_driver_ln.toPlainText(),
            'surname': self.text_driver_fn.toPlainText(),
            'patronymic': self.text_driver_pn.toPlainText(),
            'age': self.text_driver_age.toPlainText(),
            'base_salary': self.text_driver_salary.toPlainText(),
            'category_driver_license': self.list_box,
            'transport_list': self.list_combo_box_transport  # транспорт
        }
        print(self.data)
        self.clear_driver()

    def save_data_inspector(self):
        """Сохранение данных инспектора при нажатии на кнопку 'создать'"""
        while "" in self.list_combo_box_equipment:
            index_none = self.list_combo_box_equipment.index("")
            self.list_combo_box_equipment.pop(index_none)
        self.data = {
            'name': self.text_ispector_ln.toPlainText(),
            'surname': self.text_ispector_fn.toPlainText(),
            'patronymic': self.text_ispector_pn.toPlainText(),
            'age': self.text_ispector_age.toPlainText(),
            'base_salary': self.text_ispector_salary.toPlainText(),
            'equipment_list': self.list_combo_box_equipment  # оборудование
        }
        print(self.data)
        self.clear_inspector()

    def save_data_electrician_control(self):
        """Сохранение данных электромонтера утээ при нажатии на кнопку 'создать'"""
        self.data = {
            'name': self.text_el_monter_ut_ln_3.toPlainText(),
            'surname': self.text_el_monter_ut_fn_3.toPlainText(),
            'patronymic': self.text_el_monter_ut_pn_3.toPlainText(),
            'age': self.text_el_monter_ut_age_3.toPlainText(),
            'base_salary': self.text_el_monter_ut_salary_3.toPlainText(),
        }
        print(self.data)
        self.clear_electrician_control()

    def save_data_dispatcher(self):
        """Сохранение данных начальника одг при нажатии на кнопку 'создать'"""
        while "" in self.list_combo_box_equipment:
            index_none = self.list_combo_box_equipment.index("")
            self.list_combo_box_equipment.pop(index_none)
        self.data = {
            'name': self.text_disp_ln.toPlainText(),
            'surname': self.text_disp_fn.toPlainText(),
            'patronymic': self.text_disp_pn.toPlainText(),
            'age': self.text_disp_age.toPlainText(),
            'base_salary': self.text_disp_salary.toPlainText(),
            'equipment_list': self.list_combo_box_equipment  # оборудование
        }
        print(self.data)
        self.clear_dispatcher()

    def save_data_transformer(self):
        """Сохранение данных трансформатора при нажатии на кнопку 'создать'"""
        data = {
            'name': self.text_trans_name.toPlainText(),
            'assignment': self.text_trans_assignment.toPlainText(),
            'voltage_kilovolt': self.double_spin_1,
            'weight_oil': self.double_spin_2,
            'voltage_transformation': self.text_voltage_transform.toPlainText(),
            'power_kva': self.spin_1
        }
        print(data)
        self.clear_transformer()

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
        if s == Qt.CheckState.Checked.value:
            self.list_box.append("A")
        else:
            b = self.list_box.index("A")
            self.list_box.pop(b)

    def __show_state_b(self, s):
        if s == Qt.CheckState.Checked.value:
            self.list_box.append("B")
        else:
            b = self.list_box.index("B")
            self.list_box.pop(b)

    def __show_state_c(self, s):
        if s == Qt.CheckState.Checked.value:
            self.list_box.append("C")
        else:
            b = self.list_box.index("C")
            self.list_box.pop(b)

    def __show_state_d(self, s):
        if s == Qt.CheckState.Checked.value:
            self.list_box.append("D")
        else:
            b = self.list_box.index("D")
            self.list_box.pop(b)

    def __show_state_e(self, s):
        if s == Qt.CheckState.Checked.value:
            self.list_box.append("E")
        else:
            b = self.list_box.index("E")
            self.list_box.pop(b)

    def list_combo_box_manager_add(self): # вставка items из файла или БД
        """Функция управления и вывода данных комбо бокса начальника"""
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
        """Функция управления и вывода данных комбо бокса инженера"""
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

    def list_combo_box_master_add(self): # вставка items из файла или БД
        """Функция управления и вывода данных комбо бокса мастера"""
        self.original_values_combo_box['combo_box_manager_employee'] = ["", "One", "Two", "Three"]

        self.comboBox_master_1.addItems(self.original_values_combo_box['combo_box_manager_employee'])
        self.comboBox_master_2.addItems(self.original_values_combo_box['combo_box_manager_employee'])
        self.comboBox_master_3.addItems(self.original_values_combo_box['combo_box_manager_employee'])
        self.comboBox_master_4.addItems(self.original_values_combo_box['combo_box_manager_employee'])
        self.comboBox_master_5.addItems(self.original_values_combo_box['combo_box_manager_employee'])

        self.original_combo_box['original_combo_box_employee'] = self.comboBox_engineer_1.currentText()

        self.comboBox_master_1.currentTextChanged.connect(self.__text_changed1)
        self.comboBox_master_2.currentTextChanged.connect(self.__text_changed2)
        self.comboBox_master_3.currentTextChanged.connect(self.__text_changed3)
        self.comboBox_master_4.currentTextChanged.connect(self.__text_changed4)
        self.comboBox_master_5.currentTextChanged.connect(self.__text_changed5)

    def list_combo_box_supervisor_control_add(self): # вставка items из файла или БД
        """Функция управления и вывода данных комбо бокса начальника утээ"""
        self.original_values_combo_box['combo_box_manager_employee'] = ["", "One", "Two", "Three"]
        self.original_values_combo_box['combo_box_manager_equipment'] = ["", "One", "Two", "Three"]

        self.comboBox_n_utaa.addItems(self.original_values_combo_box['combo_box_manager_employee'])
        self.comboBox_n_utaa_1.addItems(self.original_values_combo_box['combo_box_manager_employee'])
        self.comboBox_n_utaa_2.addItems(self.original_values_combo_box['combo_box_manager_employee'])
        self.comboBox_n_utaa_3.addItems(self.original_values_combo_box['combo_box_manager_employee'])
        self.comboBox_n_utaa_4.addItems(self.original_values_combo_box['combo_box_manager_employee'])
        self.comboBox_n_utaa_5.addItems(self.original_values_combo_box['combo_box_manager_equipment'])
        self.comboBox_n_utaa_6.addItems(self.original_values_combo_box['combo_box_manager_equipment'])
        self.comboBox_n_utaa_7.addItems(self.original_values_combo_box['combo_box_manager_equipment'])
        self.comboBox_n_utaa_8.addItems(self.original_values_combo_box['combo_box_manager_equipment'])
        self.comboBox_n_utaa_9.addItems(self.original_values_combo_box['combo_box_manager_equipment'])

        self.original_combo_box['original_combo_box_employee'] = self.comboBox_n_utaa_1.currentText()
        self.original_combo_box['combo_box_manager_equipment'] = self.comboBox_n_utaa_6.currentText()

        self.comboBox_n_utaa.currentTextChanged.connect(self.__text_changed6)
        self.comboBox_n_utaa_1.currentTextChanged.connect(self.__text_changed7)
        self.comboBox_n_utaa_2.currentTextChanged.connect(self.__text_changed8)
        self.comboBox_n_utaa_3.currentTextChanged.connect(self.__text_changed9)
        self.comboBox_n_utaa_4.currentTextChanged.connect(self.__text_changed10)
        self.comboBox_n_utaa_5.currentTextChanged.connect(self.__text_changed1)
        self.comboBox_n_utaa_6.currentTextChanged.connect(self.__text_changed2)
        self.comboBox_n_utaa_7.currentTextChanged.connect(self.__text_changed3)
        self.comboBox_n_utaa_8.currentTextChanged.connect(self.__text_changed4)
        self.comboBox_n_utaa_9.currentTextChanged.connect(self.__text_changed5)

    def list_combo_box_mechanic_add(self): # вставка items из файла или БД
        """Функция управления и вывода данных комбо бокса механика"""
        self.original_values_combo_box['combo_box_manager_employee'] = ["", "One", "Two", "Three"]
        self.original_values_combo_box['combo_box_manager_transport'] = ["", "One", "Two", "Three"]

        self.comboBox_mechanic_1.addItems(self.original_values_combo_box['combo_box_manager_employee'])
        self.comboBox_mechanic_2.addItems(self.original_values_combo_box['combo_box_manager_employee'])
        self.comboBox_mechanic_3.addItems(self.original_values_combo_box['combo_box_manager_employee'])
        self.comboBox_mechanic_4.addItems(self.original_values_combo_box['combo_box_manager_employee'])
        self.comboBox_mechanic_5.addItems(self.original_values_combo_box['combo_box_manager_employee'])
        self.combo_driver_tech_4.addItems(self.original_values_combo_box['combo_box_manager_transport'])
        self.combo_driver_tech_5.addItems(self.original_values_combo_box['combo_box_manager_transport'])
        self.combo_driver_tech_6.addItems(self.original_values_combo_box['combo_box_manager_transport'])

        self.original_combo_box['original_combo_box_employee'] = self.comboBox_mechanic_1.currentText()
        self.original_combo_box['combo_box_manager_transport'] = self.combo_driver_tech_4.currentText()

        self.comboBox_mechanic_1.currentTextChanged.connect(self.__text_changed1)
        self.comboBox_mechanic_2.currentTextChanged.connect(self.__text_changed2)
        self.comboBox_mechanic_3.currentTextChanged.connect(self.__text_changed3)
        self.comboBox_mechanic_4.currentTextChanged.connect(self.__text_changed4)
        self.comboBox_mechanic_5.currentTextChanged.connect(self.__text_changed5)
        self.combo_driver_tech_4.currentTextChanged.connect(self.__text_changed_transport_1)
        self.combo_driver_tech_5.currentTextChanged.connect(self.__text_changed_transport_2)
        self.combo_driver_tech_6.currentTextChanged.connect(self.__text_changed_transport_3)

    def list_combo_box_supervisor_dispatcher_add(self): # вставка items из файла или БД
        """Функция управления и вывода данных комбо бокса начальника одг"""
        self.original_values_combo_box['combo_box_manager_employee'] = ["", "One", "Two", "Three"]
        self.original_values_combo_box['combo_box_manager_equipment'] = ["", "Трансформ", "Выключатель 10", "Выключатель 110"]

        self.comboBox_disp_11.addItems(self.original_values_combo_box['combo_box_manager_employee'])
        self.comboBox_disp_12.addItems(self.original_values_combo_box['combo_box_manager_employee'])
        self.comboBox_disp_13.addItems(self.original_values_combo_box['combo_box_manager_employee'])
        self.comboBox_disp_14.addItems(self.original_values_combo_box['combo_box_manager_employee'])
        self.comboBox_disp_15.addItems(self.original_values_combo_box['combo_box_manager_employee'])
        self.comboBox_disp_6.addItems(self.original_values_combo_box['combo_box_manager_equipment'])
        self.comboBox_disp_7.addItems(self.original_values_combo_box['combo_box_manager_equipment'])
        self.comboBox_disp_8.addItems(self.original_values_combo_box['combo_box_manager_equipment'])
        self.comboBox_disp_9.addItems(self.original_values_combo_box['combo_box_manager_equipment'])
        self.comboBox_disp_10.addItems(self.original_values_combo_box['combo_box_manager_equipment'])

        self.original_combo_box['original_combo_box_employee'] = self.comboBox_disp_6.currentText()
        self.original_combo_box['combo_box_manager_equipment'] = self.comboBox_disp_11.currentText()

        self.comboBox_disp_6.currentTextChanged.connect(self.__text_changed1)
        self.comboBox_disp_7.currentTextChanged.connect(self.__text_changed2)
        self.comboBox_disp_8.currentTextChanged.connect(self.__text_changed3)
        self.comboBox_disp_9.currentTextChanged.connect(self.__text_changed4)
        self.comboBox_disp_10.currentTextChanged.connect(self.__text_changed5)
        self.comboBox_disp_11.currentTextChanged.connect(self.__text_changed6)
        self.comboBox_disp_12.currentTextChanged.connect(self.__text_changed7)
        self.comboBox_disp_13.currentTextChanged.connect(self.__text_changed8)
        self.comboBox_disp_14.currentTextChanged.connect(self.__text_changed9)
        self.comboBox_disp_15.currentTextChanged.connect(self.__text_changed10)

    def list_combo_box_driver_add(self): # вставка items из файла или БД
        """Функция управления и вывода данных комбо бокса механика"""
        self.original_values_combo_box['combo_box_manager_employee'] = ["", "One", "Two", "Three"]
        self.original_values_combo_box['combo_box_manager_transport'] = ["", "One", "Two", "Three"]

        self.combo_driver_tech_1.addItems(self.original_values_combo_box['combo_box_manager_transport'])
        self.combo_driver_tech_2.addItems(self.original_values_combo_box['combo_box_manager_transport'])
        self.combo_driver_tech_3.addItems(self.original_values_combo_box['combo_box_manager_transport'])

        self.original_combo_box['combo_box_manager_transport'] = self.combo_driver_tech_1.currentText()

        self.combo_driver_tech_1.currentTextChanged.connect(self.__text_changed_transport_1)
        self.combo_driver_tech_2.currentTextChanged.connect(self.__text_changed_transport_2)
        self.combo_driver_tech_3.currentTextChanged.connect(self.__text_changed_transport_3)

    def list_combo_box_inspector_add(self): # вставка items из файла или БД
        """Функция управления и вывода данных комбо бокса начальника утээ"""
        self.original_values_combo_box['combo_box_manager_equipment'] = ["", "One", "Two", "Three"]

        self.comboBox_ispector.addItems(self.original_values_combo_box['combo_box_manager_equipment'])
        self.comboBox_ispector_1.addItems(self.original_values_combo_box['combo_box_manager_equipment'])
        self.comboBox_ispector_2.addItems(self.original_values_combo_box['combo_box_manager_equipment'])
        self.comboBox_ispector_3.addItems(self.original_values_combo_box['combo_box_manager_equipment'])
        self.comboBox_ispector_4.addItems(self.original_values_combo_box['combo_box_manager_equipment'])

        self.original_combo_box['combo_box_manager_equipment'] = self.comboBox_ispector_1.currentText()

        self.comboBox_ispector.currentTextChanged.connect(self.__text_changed6)
        self.comboBox_ispector_1.currentTextChanged.connect(self.__text_changed7)
        self.comboBox_ispector_2.currentTextChanged.connect(self.__text_changed8)
        self.comboBox_ispector_3.currentTextChanged.connect(self.__text_changed9)
        self.comboBox_ispector_4.currentTextChanged.connect(self.__text_changed10)

    def list_combo_box_dispatcher_add(self): # вставка items из файла или БД
        """Функция управления и вывода данных комбо бокса диспетрера"""
        self.original_values_combo_box['combo_box_manager_employee'] = ["", "One", "Two", "Three"]
        self.original_values_combo_box['combo_box_manager_equipment'] = ["", "Трансформ", "Выключатель 10", "Выключатель 110"]

        self.comboBox_disp_1.addItems(self.original_values_combo_box['combo_box_manager_equipment'])
        self.comboBox_disp_2.addItems(self.original_values_combo_box['combo_box_manager_equipment'])
        self.comboBox_disp_3.addItems(self.original_values_combo_box['combo_box_manager_equipment'])
        self.comboBox_disp_4.addItems(self.original_values_combo_box['combo_box_manager_equipment'])
        self.comboBox_disp_5.addItems(self.original_values_combo_box['combo_box_manager_equipment'])

        self.original_combo_box['combo_box_manager_equipment'] = self.comboBox_disp_1.currentText()

        self.comboBox_disp_1.currentTextChanged.connect(self.__text_changed6)
        self.comboBox_disp_2.currentTextChanged.connect(self.__text_changed7)
        self.comboBox_disp_3.currentTextChanged.connect(self.__text_changed8)
        self.comboBox_disp_4.currentTextChanged.connect(self.__text_changed9)
        self.comboBox_disp_5.currentTextChanged.connect(self.__text_changed10)

    def click_item_button_transformer(self):
        """Фунция выбора спин бокса и передачи сигнала нажатия на кнопки"""
        self.doubleSpinBox_ot_1.textChanged.connect((lambda num: setattr(self, 'double_spin_1', num)))
        self.doubleSpinBox_ot_2.textChanged.connect(lambda num: setattr(self, 'double_spin_2', num))
        self.spinBox_ot_3.textChanged.connect((lambda num: setattr(self, 'spin_1', num)))


    def click_item_button(self):
        """Фунция выбора спин бокса и передачи сигнала нажатия на кнопки"""
        # Действие выбора спин бокса (сделать одельной функцией на каждый виджет)
        self.spinBox_ptr_1.textChanged.connect((lambda num: setattr(self, 'pt', num)))
        self.doubleSpinBox_ptr_2.textChanged.connect(lambda num: setattr(self, 'pt_1', num))
        self.spinBox_ptr_3.textChanged.connect((lambda num: setattr(self, 'pt_2', num)))


    def __text_changed1(self, s):
        self.list_combo_box_employee[0] = s

    def __text_changed2(self, s):
        self.list_combo_box_employee[1] = s

    def __text_changed3(self, s):
        self.list_combo_box_employee[2] = s

    def __text_changed4(self, s):
        self.list_combo_box_employee[3] = s

    def __text_changed5(self, s):
        self.list_combo_box_employee[4] = s

    def __text_changed6(self, s):
        self.list_combo_box_equipment[0] = s

    def __text_changed7(self, s):
        self.list_combo_box_equipment[1] = s

    def __text_changed8(self, s):
        self.list_combo_box_equipment[2] = s

    def __text_changed9(self, s):
        self.list_combo_box_equipment[3] = s

    def __text_changed10(self, s):
        self.list_combo_box_equipment[4] = s

    def __text_changed_transport_1(self, s):
        self.list_combo_box_transport[0] = s

    def __text_changed_transport_2(self, s):
        self.list_combo_box_transport[1] = s

    def __text_changed_transport_3(self, s):
        self.list_combo_box_transport[2] = s

