from PyQt6 import QtWidgets

from src.program_management_click_button import ProgramManagementSwitchingWidgets

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()

    ui = ProgramManagementSwitchingWidgets()
    ui.setupUi(MainWindow)
    ui.click_item_tree()
    ui.click_item_button()
    ui.click_item_button_next_back()
    ui.check_box_driver()
    ui.check_box_mechanic()
    ui.check_box_manager()
    ui.check_box_engineer()
    ui.list_combo_box_manager_add()
    ui.list_combo_box_engineer_add()
    ui.list_combo_box_master_add()
    ui.list_combo_box_supervisor_control_add()
    ui.list_combo_box_mechanic_add()

    MainWindow.show()
    sys.exit(app.exec())

# продолжить добавление функционала с монтера