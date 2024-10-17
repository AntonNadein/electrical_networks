from src.program_management import ProgramManagement


class ProgramManagementClear(ProgramManagement):
    def clear_data(self):
        if self.page_number == 1:
            self.clear_manager()
            self.data = {}
        elif self.page_number == 2:
            self.clear_engineer()
            self.data = {}
        elif self.page_number == 3:
            self.clear_master()
        elif self.page_number == 4:
            self.clear_supervisor_control()
        elif self.page_number == 5:
            self.clear_mechanic()
        elif self.page_number == 6:
            self.clear_supervisor_control()
        elif self.page_number == 7:
            self.clear_electrician()
        elif self.page_number == 8:
            self.clear_driver()
        elif self.page_number == 9:
            self.clear_inspector()
        elif self.page_number == 10:
            self.clear_electrician_control()
        elif self.page_number == 11:
            self.clear_dispetcher()
        elif self.page_number == 12:
            self.clear_transformer()
        elif self.page_number == 13:
            self.clear_switch()
        elif self.page_number == 14:
            self.clear_metering_device()
        elif self.page_number == 15:
            self.clear_passenger_transport()
        elif self.page_number == 16:
            self.clear_freight_transport()
        elif self.page_number == 17:
            self.clear_special_transport()
        # else:
        #     self.stackedWidget.setCurrentIndex(0)



    def clear_manager(self):
        """Фунция очистки карточки начальника"""
        self.text_manager_ln.setPlainText(self.original_values['clear_plain_text'])
        self.text_manager_fn.setPlainText(self.original_values['clear_plain_text'])
        self.text_manager_pn.setPlainText(self.original_values['clear_plain_text'])
        self.text_manager_age.setPlainText(self.original_values['clear_plain_text'])
        self.text_manager_salary.setPlainText(self.original_values['clear_plain_text'])
        self.checkBox_driver_a_3.setChecked(self.original_values['checkBox_driver_a'])
        self.checkBox_driver_b_3.setChecked(self.original_values['checkBox_driver_b'])
        self.checkBox_driver_c_3.setChecked(self.original_values['checkBox_driver_c'])
        self.checkBox_driver_d_3.setChecked(self.original_values['checkBox_driver_d'])
        self.checkBox_driver_e_3.setChecked(self.original_values['checkBox_driver_e'])
        self.list_combo_box_employee = ["", "", "", "", ""]
        self.list_combo_box_equipment = ["", "", "", "", ""]
        self.comboBox_manager_1.setCurrentText(self.original_combo_box['original_combo_box_employee'])
        self.comboBox_manager_2.setCurrentText(self.original_combo_box['original_combo_box_employee'])
        self.comboBox_manager_3.setCurrentText(self.original_combo_box['original_combo_box_employee'])
        self.comboBox_manager_4.setCurrentText(self.original_combo_box['original_combo_box_employee'])
        self.comboBox_manager_5.setCurrentText(self.original_combo_box['original_combo_box_employee'])
        self.comboBox_manager_6.setCurrentText(self.original_combo_box['combo_box_manager_equipment'])
        self.comboBox_manager_7.setCurrentText(self.original_combo_box['combo_box_manager_equipment'])
        self.comboBox_manager_8.setCurrentText(self.original_combo_box['combo_box_manager_equipment'])
        self.comboBox_manager_9.setCurrentText(self.original_combo_box['combo_box_manager_equipment'])
        self.comboBox_manager_10.setCurrentText(self.original_combo_box['combo_box_manager_equipment'])

    def clear_engineer(self):
        self.text_engineer_ln.setPlainText(self.original_values['clear_plain_text'])
        self.text_engineer_fn.setPlainText(self.original_values['clear_plain_text'])
        self.text_engineer_pn.setPlainText(self.original_values['clear_plain_text'])
        self.text_engineer_age.setPlainText(self.original_values['clear_plain_text'])
        self.text_engineer_salary.setPlainText(self.original_values['clear_plain_text'])
        self.checkBox_driver_a_4.setChecked(self.original_values['checkBox_driver_a'])
        self.checkBox_driver_b_4.setChecked(self.original_values['checkBox_driver_b'])
        self.checkBox_driver_c_4.setChecked(self.original_values['checkBox_driver_c'])
        self.checkBox_driver_d_4.setChecked(self.original_values['checkBox_driver_d'])
        self.checkBox_driver_e_4.setChecked(self.original_values['checkBox_driver_e'])
        self.list_combo_box_employee = ["", "", "", "", ""]
        self.list_combo_box_equipment = ["", "", "", "", ""]
        self.comboBox_engineer_1.setCurrentText(self.original_combo_box['original_combo_box_employee'])
        self.comboBox_engineer_2.setCurrentText(self.original_combo_box['original_combo_box_employee'])
        self.comboBox_engineer_3.setCurrentText(self.original_combo_box['original_combo_box_employee'])
        self.comboBox_engineer_4.setCurrentText(self.original_combo_box['original_combo_box_employee'])
        self.comboBox_engineer_5.setCurrentText(self.original_combo_box['original_combo_box_employee'])
        self.comboBox_engineer_6.setCurrentText(self.original_combo_box['combo_box_manager_equipment'])
        self.comboBox_engineer_7.setCurrentText(self.original_combo_box['combo_box_manager_equipment'])
        self.comboBox_engineer_8.setCurrentText(self.original_combo_box['combo_box_manager_equipment'])
        self.comboBox_engineer_9.setCurrentText(self.original_combo_box['combo_box_manager_equipment'])
        self.comboBox_engineer_10.setCurrentText(self.original_combo_box['combo_box_manager_equipment'])

    def clear_master(self):
        pass

    def clear_supervisor_control(self):
        pass

    def clear_mechanic(self):
        """Фунция очистки карточки водителя"""
        self.checkBox_driver_a_2.setChecked(self.original_values['checkBox_driver_a'])
        self.checkBox_driver_b_2.setChecked(self.original_values['checkBox_driver_b'])
        self.checkBox_driver_c_2.setChecked(self.original_values['checkBox_driver_c'])
        self.checkBox_driver_d_2.setChecked(self.original_values['checkBox_driver_d'])
        self.checkBox_driver_e_2.setChecked(self.original_values['checkBox_driver_e'])

    def clear_supervisor_dispatcher(self):
        pass

    def clear_electrician(self):
        pass

    def clear_driver(self):
        """Фунция очистки карточки водителя"""
        self.checkBox_driver_a.setChecked(self.original_values['checkBox_driver_a'])
        self.checkBox_driver_b.setChecked(self.original_values['checkBox_driver_b'])
        self.checkBox_driver_c.setChecked(self.original_values['checkBox_driver_c'])
        self.checkBox_driver_d.setChecked(self.original_values['checkBox_driver_d'])
        self.checkBox_driver_e.setChecked(self.original_values['checkBox_driver_e'])

    def clear_inspector(self):
        pass

    def clear_electrician_control(self):
        pass

    def clear_dispetcher(self):
        pass

    def clear_transformer(self):
        pass

    def clear_switch(self):
        pass

    def clear_metering_device(self):
        pass

    def clear_passenger_transport(self):
        pass

    def clear_freight_transport(self):
        pass

    def clear_special_transport(self):
        pass