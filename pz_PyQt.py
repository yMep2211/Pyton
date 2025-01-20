'''
#Задание 1 Кликер
from PyQt6.QtWidgets import QApplication, QPushButton, QMainWindow, QLabel, QVBoxLayout, QWidget
from PyQt6.QtCore import Qt
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.count = 0
        self.setWindowTitle("ПЗ для крутых ребзей")
        self.button = QPushButton("Нажми меня")
        self.label = QLabel("0")
        self.label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.button.clicked.connect(self.schetchik)
        
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button)
        
        widget = QWidget()
        widget.setLayout(layout)
        
        self.setCentralWidget(widget)
          
    def schetchik(self):
        self.count += 1
        self.label.setText(str(self.count))
'''        


'''
#Задание 2 Редактор текста
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QComboBox, QCheckBox, QLabel, QRadioButton, QLineEdit
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Моё приложение")

        color = QLabel('Выбрать цвет текста')
        color.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.colorComboBox = QComboBox()
        self.colorComboBox.addItems(['Черный', 'Зеленый', 'Синий'])

        style = QLabel('Выбрать стиль текста')
        style.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.styleB = QCheckBox('Жирный')
        self.styleEM = QCheckBox('Курсив')

        size = QLabel('Выбрать размер текста')
        size.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        radioButtonLayout = QVBoxLayout()

        self.rb1 = QRadioButton('12')
        self.rb2 = QRadioButton('14')
        self.rb3 = QRadioButton('16')

        radioButtonLayout.addWidget(self.rb1)
        radioButtonLayout.addWidget(self.rb2)
        radioButtonLayout.addWidget(self.rb3)

        radioButtonContainer = QWidget()
        radioButtonContainer.setLayout(radioButtonLayout)

        inputText = QLabel('Введите текст')
        inputText.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        self.label = QLabel()
        self.input = QLineEdit()
        self.input.textChanged.connect(self.updateT)

        self.colorComboBox.currentIndexChanged.connect(self.updateT)
        self.styleB.stateChanged.connect(self.updateT)
        self.styleEM.stateChanged.connect(self.updateT)
        self.rb1.toggled.connect(self.updateT)
        self.rb2.toggled.connect(self.updateT)
        self.rb3.toggled.connect(self.updateT)

        layout = QVBoxLayout()
        layout.addWidget(color)
        layout.addWidget(self.colorComboBox)
        layout.addWidget(style)
        layout.addWidget(self.styleB)
        layout.addWidget(self.styleEM)
        layout.addWidget(size)
        layout.addWidget(radioButtonContainer)
        layout.addWidget(inputText)
        layout.addWidget(self.input)  
        layout.addWidget(self.label)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def updateT(self):
        
        text = self.input.text()  

        colorDict = {'Черный': 'black', 'Зеленый': 'green', 'Синий': 'blue'}
        color = colorDict[self.colorComboBox.currentText()]

        font = QFont()
        font.setBold(self.styleB.isChecked())
        font.setItalic(self.styleEM.isChecked())

        if self.rb1.isChecked():
            font.setPointSize(12)
        elif self.rb2.isChecked():
            font.setPointSize(14)
        elif self.rb3.isChecked():
            font.setPointSize(16)

        self.label.setText(text)
        self.label.setFont(font)
        self.label.setStyleSheet(f"color: {color}")
'''
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()