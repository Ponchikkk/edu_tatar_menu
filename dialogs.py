import sys

from Error_post_dialog import Ui_Error_post_dialog
from Successfully_post_dialog import Ui_Successfully_post_dialog
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QDialog


class Error_post_dialog(QDialog, Ui_Error_post_dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.close_button.clicked.connect(lambda: self.close())


def error_post_dialog_show():
    dialog = Error_post_dialog()
    dialog.show()
    dialog.exec_()


class Succefully_post_dialog(QDialog, Ui_Successfully_post_dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.close_button.clicked.connect(lambda: self.close())


def succefully_post_dialog_show():
    dialog = Succefully_post_dialog()
    dialog.show()
    dialog.exec_()
