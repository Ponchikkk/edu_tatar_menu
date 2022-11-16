import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QDialog
from untitled import Ui_QMainWindow
import sqlite3
from eduauth import edu_auth
from edu_tatar_functions import upload_files, post_page, get_files
from dialogs import error_post_dialog_show, succefully_post_dialog_show


class MainWindow(QMainWindow, Ui_QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.db = sqlite3.connect("edu_tatar_ru_menu.db")
        self.launch_data()
        self.path_file = ""
        self.show()
        self.pushButton_save_data.clicked.connect(self.save_data)
        self.pushBatton_download_file.clicked.connect(self.download_file)
        self.pushButton_delete_file.clicked.connect(self.delete_file)
        self.pushButton_close_application.clicked.connect(self.exit)
        self.pushButton_send.clicked.connect(self.send_file)

    def exit(self):
        sys.exit()

    def launch_data(self):
        data = self.db.execute(
            '''SELECT login, password, link_folder_food, page_folder_food, proxy FROM users_data''').fetchall()
        self.lineEdit_login_edu_tatar.setText(str(data[0][0]))
        self.linEedit_password_edu_tatar.setText(str(data[0][1]))
        self.lineEdit_link_to_the_folder_food.setText(data[0][2])
        self.lineEdit_link_to_the_page_food.setText(data[0][3])
        self.lineEdit_proxy.setText(data[0][4])

    def links(self):
        self.lineEdit_link_to_the_folder_food.split("/")

    def save_data(self):
        login = self.lineEdit_login_edu_tatar.text()
        password = self.linEedit_password_edu_tatar.text()
        folder_food = self.lineEdit_link_to_the_folder_food.text()
        page_food = self.lineEdit_link_to_the_page_food.text()
        proxy = self.lineEdit_proxy.text()
        self.db.execute('''DELETE FROM users_data''')
        self.db.execute(
            f'''INSERT INTO users_data  VALUES ("{login}", "{password}", "{folder_food}", "{page_food}", "{proxy}")''')
        self.db.commit()
        self.statusbar.showMessage("Данные сохранены")

    def download_file(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', 'c:\\')
        self.path_file = fname[0]
        self.label_file_path.setText(self.path_file.split("/")[-1])
        self.statusbar.showMessage("Файл загружен")

    def delete_file(self):
        self.label_file_path.setText("")
        self.path_file = ""
        self.statusbar.showMessage("Файл удален")

    def send_file(self):
        login = self.lineEdit_login_edu_tatar.text()
        password = self.linEedit_password_edu_tatar.text()
        proxy = {"http": self.lineEdit_proxy.text()}
        self.statusbar.showMessage("Операция выполняется...")
        # edu_session = edu_auth(login, password, proxy)

        #fp = open(self.path_file, "rb")
        #fn = self.path_file.split("/")[-1]
        #print(fn)
        #files = {'file': (fn, fp, 'application/vnd.ms-excel')}
        # upload_files(edu_session, files, proxy)
        # post_page(edu_session, page_id=800107, data=get_files(edu_session), proxy=proxy)
        try:
            link_to_the_folder_food = "/".join(self.lineEdit_link_to_the_folder_food.text().split("/")[:7])
            link_to_the_page_food = self.lineEdit_link_to_the_page_food.text()
            fp = open(self.path_file, "rb")
            fn = self.path_file.split("/")[-1]
            print(fn)
            files = {'file': (fn, fp, 'application/vnd.ms-excel')}
            edu_session = edu_auth(login, password, proxy)
            upload_files(edu_session, files, proxy)
            post_page(edu_session, link_to_the_page_food, get_files(edu_session, link_to_the_folder_food), proxy, link_to_the_folder_food)
            succefully_post_dialog_show()
            self.statusbar.showMessage("Успешно!")
        except:
            self.statusbar.showMessage("Ошибка!")
            error_post_dialog_show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainwindow = MainWindow()

    sys.exit(app.exec_())
