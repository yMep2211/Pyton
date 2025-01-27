'''
#ЗАДАНИЕ 3
import sys

from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QComboBox, QCheckBox, QLabel, QRadioButton, QLineEdit,QPushButton,QMessageBox
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__() 
        self.setWindowTitle("Задание 3")

        self.fio = QLabel("Введите ФИО")
        self.fio.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        self.surname = QLineEdit()
        self.surname.setPlaceholderText("Фамилия")

        self.name = QLineEdit()
        self.name.setPlaceholderText("Имя")

        self.lastname = QLineEdit()
        self.lastname.setPlaceholderText("Отчество")

        self.city_choice = QLabel("Выберите город") 
        self.city_choice.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        self.city = QComboBox()
        self.city.addItems(['Абакан', 'Боград', 'Черногорск'])

        self.sex_choice = QLabel("Укажите пол") 
        self.sex_choice.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        self.sexLayout = QVBoxLayout()

        self.man = QRadioButton('Мужской')
        self.woman = QRadioButton('Женский')

        self.sexLayout.addWidget(self.man)
        self.sexLayout.addWidget(self.woman)
        

        self.sexContainer = QWidget()
        self.sexContainer.setLayout(self.sexLayout)

        self.info = QPushButton("Вывести информацию")
        self.info.clicked.connect(self.pin)

        self.label = QLabel()
        self.label.setAlignment(Qt.AlignmentFlag.AlignHCenter)




        layout = QVBoxLayout()
        layout.addWidget(self.fio)
        layout.addWidget(self.surname)
        layout.addWidget(self.name)
        layout.addWidget(self.lastname)
        layout.addWidget(self.city_choice)
        layout.addWidget(self.city)
        layout.addWidget(self.sex_choice)
        layout.addWidget(self.sexContainer)
        layout.addWidget(self.info)
        layout.addWidget(self.label)
        
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def pin(self):
        
        surname = self.surname.text()
        name = self.name.text()
        lastname = self.lastname.text()
        city = self.city.currentText()

        if not surname:
            QMessageBox.warning(self, "Внимание", "Поле ~фамилия~ не должно быть пустым!")
            return
        if not name:
            QMessageBox.warning(self, "Внимание", "Поле ~имя~ не должно быть пустым!")
            return
        
        if self.man.isChecked():
            sex = "Мужской"
        elif self.woman.isChecked():
            sex = "Женский"
        else:
            QMessageBox.warning(self, "Внимание", "Поле ~пол~ не должно быть пустым!")
            return

        info = f"ФИО: {surname} {name} {lastname}\n Город: {city}\n Пол: {sex}" 
        
        self.label.setText(info)

        self.surname.clear()
        self.name.clear()
        self.lastname.clear()
        

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
'''


'''
#Задание 4
import sys

from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QComboBox, QCheckBox, QLabel, QRadioButton, QLineEdit,QPushButton,QMessageBox
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__() 
        self.setWindowTitle("Задание 3")

        self.fio = QLabel("Введите ФИО")
        self.fio.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        self.surname = QLineEdit()
        self.surname.setPlaceholderText("Фамилия")
        self.surname.textChanged.connect(self.pin)

        self.name = QLineEdit()
        self.name.setPlaceholderText("Имя")
        self.name.textChanged.connect(self.pin)

        self.lastname = QLineEdit()
        self.lastname.setPlaceholderText("Отчество")
        self.lastname.textChanged.connect(self.pin)

        self.city_choice = QLabel("Выберите город") 
        self.city_choice.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        self.city = QComboBox()
        self.city.addItems(['Абакан', 'Боград', 'Черногорск'])
        self.city.currentIndexChanged.connect(self.pin)

        self.sex_choice = QLabel("Укажите пол") 
        self.sex_choice.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        self.sexLayout = QVBoxLayout()

        self.man = QRadioButton('Мужской')
        self.woman = QRadioButton('Женский')

        self.man.toggled.connect(self.pin)
        self.woman.toggled.connect(self.pin)

        self.sexLayout.addWidget(self.man)
        self.sexLayout.addWidget(self.woman)
        

        self.sexContainer = QWidget()
        self.sexContainer.setLayout(self.sexLayout)

        # self.info = QPushButton("Вывести информацию")
        # self.info.clicked.connect(self.pin)

        self.label = QLabel()
        self.label.setAlignment(Qt.AlignmentFlag.AlignHCenter)


        layout = QVBoxLayout()
        layout.addWidget(self.fio)
        layout.addWidget(self.surname)
        layout.addWidget(self.name)
        layout.addWidget(self.lastname)
        layout.addWidget(self.city_choice)
        layout.addWidget(self.city)
        layout.addWidget(self.sex_choice)
        layout.addWidget(self.sexContainer)
        #layout.addWidget(self.info)
        layout.addWidget(self.label)
        
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def pin(self):
        
        surname = self.surname.text()
        name = self.name.text()
        lastname = self.lastname.text()
        city = self.city.currentText()

        # if not surname:
        #     QMessageBox.warning(self, "Внимание", "Поле ~фамилия~ не должно быть пустым!")
        #     return
        # if not name:
        #     QMessageBox.warning(self, "Внимание", "Поле ~имя~ не должно быть пустым!")
        #     return
        
        if self.man.isChecked():
            sex = "Мужской"
        elif self.woman.isChecked():
            sex = "Женский"
        else:
            sex = "Нету"

        info = f"ФИО: {surname} {name} {lastname}\n Город: {city}\n Пол: {sex}" 
        
        self.label.setText(info)

        # self.surname.clear()
        # self.name.clear()
        # self.lastname.clear()
        

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
'''