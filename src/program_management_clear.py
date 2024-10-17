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
            self.data = {}
        elif self.page_number == 4:
            self.clear_supervisor_control()
        elif self.page_number == 5:
            self.clear_mechanic()
            self.data = {}
        elif self.page_number == 6:
            self.clear_supervisor_dispatcher()
            self.data = {}
        elif self.page_number == 7:
            self.clear_electrician()
            self.data = {}
        elif self.page_number == 8:
            self.clear_driver()
            self.data = {}
        elif self.page_number == 9:
            self.clear_inspector()
            self.data = {}
        elif self.page_number == 10:
            self.clear_electrician_control()
            self.data = {}
        elif self.page_number == 11:
            self.clear_dispetcher()
            self.data = {}
        elif self.page_number == 12:
            self.clear_transformer()
            self.data = {}
        elif self.page_number == 13:
            self.clear_switch()
            self.data = {}
        elif self.page_number == 14:
            self.clear_metering_device()
            self.data = {}
        elif self.page_number == 15:
            self.clear_passenger_transport()
            self.data = {}
        elif self.page_number == 16:
            self.clear_freight_transport()
            self.data = {}
        elif self.page_number == 17:
            self.clear_special_transport()
            self.data = {}
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
        """Фунция очистки карточки инженера"""
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
        """Фунция очистки карточки мастера"""
        self.text_master_ln.setPlainText(self.original_values['clear_plain_text'])
        self.text_master_fn.setPlainText(self.original_values['clear_plain_text'])
        self.text_master_pn.setPlainText(self.original_values['clear_plain_text'])
        self.text_master_age.setPlainText(self.original_values['clear_plain_text'])
        self.text_master_salary.setPlainText(self.original_values['clear_plain_text'])
        self.list_combo_box_employee = ["", "", "", "", ""]
        self.comboBox_master_1.setCurrentText(self.original_combo_box['original_combo_box_employee'])
        self.comboBox_master_2.setCurrentText(self.original_combo_box['original_combo_box_employee'])
        self.comboBox_master_3.setCurrentText(self.original_combo_box['original_combo_box_employee'])
        self.comboBox_master_4.setCurrentText(self.original_combo_box['original_combo_box_employee'])
        self.comboBox_master_5.setCurrentText(self.original_combo_box['original_combo_box_employee'])

    def clear_supervisor_control(self):
        """Фунция очистки карточки начальника утээ"""
        self.text_n_utaa_ln.setPlainText(self.original_values['clear_plain_text'])
        self.text_n_utaa_fn.setPlainText(self.original_values['clear_plain_text'])
        self.text_n_utaa_pn.setPlainText(self.original_values['clear_plain_text'])
        self.text_n_utaa_age.setPlainText(self.original_values['clear_plain_text'])
        self.text_n_utaa_salary.setPlainText(self.original_values['clear_plain_text'])
        self.list_combo_box_employee = ["", "", "", "", ""]
        self.list_combo_box_equipment = ["", "", "", "", ""]
        self.comboBox_n_utaa.setCurrentText(self.original_combo_box['combo_box_manager_equipment'])
        self.comboBox_n_utaa_1.setCurrentText(self.original_combo_box['original_combo_box_employee'])
        self.comboBox_n_utaa_2.setCurrentText(self.original_combo_box['original_combo_box_employee'])
        self.comboBox_n_utaa_3.setCurrentText(self.original_combo_box['original_combo_box_employee'])
        self.comboBox_n_utaa_4.setCurrentText(self.original_combo_box['original_combo_box_employee'])
        self.comboBox_n_utaa_5.setCurrentText(self.original_combo_box['original_combo_box_employee'])
        self.comboBox_n_utaa_6.setCurrentText(self.original_combo_box['combo_box_manager_equipment'])
        self.comboBox_n_utaa_7.setCurrentText(self.original_combo_box['combo_box_manager_equipment'])
        self.comboBox_n_utaa_8.setCurrentText(self.original_combo_box['combo_box_manager_equipment'])
        self.comboBox_n_utaa_9.setCurrentText(self.original_combo_box['combo_box_manager_equipment'])


    def clear_mechanic(self):
        """Фунция очистки карточки механика"""
        self.text_mechanic_ln.setPlainText(self.original_values['clear_plain_text'])
        self.text_mechanic_fn.setPlainText(self.original_values['clear_plain_text'])
        self.text_mechanic_pn.setPlainText(self.original_values['clear_plain_text'])
        self.text_mechanic_age.setPlainText(self.original_values['clear_plain_text'])
        self.text_mechanic_salary.setPlainText(self.original_values['clear_plain_text'])
        self.list_combo_box_employee = ["", "", "", "", ""]
        self.list_combo_box_transport = ["", "", "", "", ""]
        self.checkBox_driver_a_2.setChecked(self.original_values['checkBox_driver_a'])
        self.checkBox_driver_b_2.setChecked(self.original_values['checkBox_driver_b'])
        self.checkBox_driver_c_2.setChecked(self.original_values['checkBox_driver_c'])
        self.checkBox_driver_d_2.setChecked(self.original_values['checkBox_driver_d'])
        self.checkBox_driver_e_2.setChecked(self.original_values['checkBox_driver_e'])
        self.combo_driver_tech_4.setCurrentText(self.original_combo_box['combo_box_manager_transport'])
        self.combo_driver_tech_5.setCurrentText(self.original_combo_box['combo_box_manager_transport'])
        self.combo_driver_tech_6.setCurrentText(self.original_combo_box['combo_box_manager_transport'])
        self.comboBox_mechanic_1.setCurrentText(self.original_combo_box['original_combo_box_employee'])
        self.comboBox_mechanic_2.setCurrentText(self.original_combo_box['original_combo_box_employee'])
        self.comboBox_mechanic_3.setCurrentText(self.original_combo_box['original_combo_box_employee'])
        self.comboBox_mechanic_4.setCurrentText(self.original_combo_box['original_combo_box_employee'])
        self.comboBox_mechanic_5.setCurrentText(self.original_combo_box['original_combo_box_employee'])

    def clear_supervisor_dispatcher(self):
        """Фунция очистки карточки начальника одг"""
        self.text_disp_ln_2.setPlainText(self.original_values['clear_plain_text'])
        self.text_disp_fn_2.setPlainText(self.original_values['clear_plain_text'])
        self.text_disp_pn_2.setPlainText(self.original_values['clear_plain_text'])
        self.text_disp_age_2.setPlainText(self.original_values['clear_plain_text'])
        self.text_disp_salary_2.setPlainText(self.original_values['clear_plain_text'])
        self.list_combo_box_employee = ["", "", "", "", ""]
        self.list_combo_box_equipment = ["", "", "", "", ""]
        self.comboBox_disp_11.setCurrentText(self.original_combo_box['combo_box_manager_equipment'])
        self.comboBox_disp_12.setCurrentText(self.original_combo_box['combo_box_manager_equipment'])
        self.comboBox_disp_13.setCurrentText(self.original_combo_box['combo_box_manager_equipment'])
        self.comboBox_disp_14.setCurrentText(self.original_combo_box['combo_box_manager_equipment'])
        self.comboBox_disp_15.setCurrentText(self.original_combo_box['combo_box_manager_equipment'])
        self.comboBox_disp_6.setCurrentText(self.original_combo_box['original_combo_box_employee'])
        self.comboBox_disp_7.setCurrentText(self.original_combo_box['original_combo_box_employee'])
        self.comboBox_disp_8.setCurrentText(self.original_combo_box['original_combo_box_employee'])
        self.comboBox_disp_9.setCurrentText(self.original_combo_box['original_combo_box_employee'])
        self.comboBox_disp_10.setCurrentText(self.original_combo_box['original_combo_box_employee'])

    def clear_electrician(self):
        """Фунция очистки карточки монтера"""
        pass

    def clear_driver(self):
        """Фунция очистки карточки водителя"""
        self.checkBox_driver_a.setChecked(self.original_values['checkBox_driver_a'])
        self.checkBox_driver_b.setChecked(self.original_values['checkBox_driver_b'])
        self.checkBox_driver_c.setChecked(self.original_values['checkBox_driver_c'])
        self.checkBox_driver_d.setChecked(self.original_values['checkBox_driver_d'])
        self.checkBox_driver_e.setChecked(self.original_values['checkBox_driver_e'])

    def clear_inspector(self):
        """Фунция очистки карточки инспектора"""
        pass

    def clear_electrician_control(self):
        """Фунция очистки карточки монтера утээ"""
        pass

    def clear_dispetcher(self):
        """Фунция очистки карточки диспетчера"""
        pass

    def clear_transformer(self):
        """Фунция очистки карточки трансформатора"""
        pass

    def clear_switch(self):
        """Фунция очистки карточки выключателя"""
        pass

    def clear_metering_device(self):
        """Фунция очистки карточки измерительного прибора"""
        pass

    def clear_passenger_transport(self):
        """Фунция очистки карточки пассажирского транспорта"""
        pass

    def clear_freight_transport(self):
        """Фунция очистки карточки грузового транспорта"""
        pass

    def clear_special_transport(self):
        """Фунция очистки карточки спецтранспорта"""
        pass