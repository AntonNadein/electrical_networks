from src.program_management_clear import ProgramManagementClear


class ProgramManagementSwitchingWidgets(ProgramManagementClear):

    def click_item_tree(self):
        """Фунция получения и передачи сигнала нажатия на элементы дерева"""
        self.treeWidget.itemClicked.connect(self.on_item_clicked)
        self.treeWidget.itemDoubleClicked.connect(self.on_item_double_clicked)

    def on_item_clicked(self, item, column):
        """Реализация одинарного клика по объекту дерева"""
        print(f"Одиночный клик: {item.text(column)}")

    def on_item_double_clicked(self, item, column):
        """Реализация двойного клика по объекту дерева"""
        print(f"Двойной клик: {item.text(column)}")
        if item.text(0) == "Начальник РЭС":
            self.stackedWidget.setCurrentIndex(1)
            self.page_number = 1
        elif item.text(0) == "Инженер":
            self.stackedWidget.setCurrentIndex(2)
            self.page_number = 2
        elif item.text(0) == "Мастер УЭС":
            self.stackedWidget.setCurrentIndex(3)
            self.page_number = 3
        elif item.text(0) == "Начальник УТЭЭ":
            self.stackedWidget.setCurrentIndex(4)
            self.page_number = 4
        elif item.text(0) == "Механик":
            self.stackedWidget.setCurrentIndex(5)
            self.page_number = 5
        elif item.text(0) == "Начальник ОДГ":
            self.stackedWidget.setCurrentIndex(6)
            self.page_number = 6
        elif item.text(0) == "Электромонтер":
            self.stackedWidget.setCurrentIndex(7)
            self.page_number = 7
        elif item.text(0) == "Водитель":
            self.stackedWidget.setCurrentIndex(8)
            self.page_number = 8
        elif item.text(0) == "Инспектор УТЭЭ":
            self.stackedWidget.setCurrentIndex(9)
            self.page_number = 9
        elif item.text(0) == "Электромонтер УТЭЭ":
            self.stackedWidget.setCurrentIndex(10)
            self.page_number = 10
        elif item.text(0) == "Диспетчер ОДГ":
            self.stackedWidget.setCurrentIndex(11)
            self.page_number = 11
        elif item.text(0) == "Трансформатор":
            self.stackedWidget.setCurrentIndex(12)
            self.page_number = 12
        elif item.text(0) == "Выключатель":
            self.stackedWidget.setCurrentIndex(13)
            self.page_number = 13
        elif item.text(0) == "Измерительное":
            self.stackedWidget.setCurrentIndex(14)
            self.page_number = 14
        elif item.text(0) == "Пассажирский":
            self.stackedWidget.setCurrentIndex(15)
            self.page_number = 15
        elif item.text(0) == "Грузовой":
            self.stackedWidget.setCurrentIndex(16)
            self.page_number = 16
        elif item.text(0) == "Спецтранспорт":
            self.stackedWidget.setCurrentIndex(17)
            self.page_number = 17
        else:
            self.stackedWidget.setCurrentIndex(0)

    def click_button(self, text):
        """Реализация кнопок вперед и назад для перелистывания виджетов"""
        if text == "Вперед":
            self.clear_data() # очищение данных при движении вперед
            self.page_number += 1
            if self.page_number > 17:
                self.page_number = 0
            self.stackedWidget.setCurrentIndex(self.page_number)
        elif text == "Назад":
            if self.page_number == 0:
                self.page_number = 18
            self.page_number -= 1
            self.stackedWidget.setCurrentIndex(self.page_number)


    def click_item_button_next_back(self):
        """Фунция получения и передачи сигнала нажатия на кнопки"""
        self.pbn_1.clicked.connect(lambda: (self.click_button(self.pbn_1.text())))
        self.pbn_2.clicked.connect(lambda: (self.click_button(self.pbn_2.text())))
        self.pushButton.clicked.connect(lambda: (self.save_data()))  # save
        self.pushButton_2.clicked.connect(self.clear_data)  # clear
