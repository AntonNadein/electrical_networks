from src.program_management import ProgramManagement


class ProgramManagementClear(ProgramManagement):
    def clear_data(self):
        if self.page_number == 1:
            self.clear_manadger()
            self.data = {}
        elif self.page_number == 2:
            self.clear_engenear()
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



    def clear_manadger(self):
        """Фунция очистки карточки водителя"""
        self.checkBox_driver_a_3.setChecked(self.original_values['checkBox_driver_a'])
        self.checkBox_driver_b_3.setChecked(self.original_values['checkBox_driver_b'])
        self.checkBox_driver_c_3.setChecked(self.original_values['checkBox_driver_c'])
        self.checkBox_driver_d_3.setChecked(self.original_values['checkBox_driver_d'])
        self.checkBox_driver_e_3.setChecked(self.original_values['checkBox_driver_e'])

    def clear_engenear(self):
        self.checkBox_driver_a_4.setChecked(self.original_values['checkBox_driver_a'])
        self.checkBox_driver_b_4.setChecked(self.original_values['checkBox_driver_b'])
        self.checkBox_driver_c_4.setChecked(self.original_values['checkBox_driver_c'])
        self.checkBox_driver_d_4.setChecked(self.original_values['checkBox_driver_d'])
        self.checkBox_driver_e_4.setChecked(self.original_values['checkBox_driver_e'])

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