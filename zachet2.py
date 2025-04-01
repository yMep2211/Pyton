import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, 
                            QLabel, QLineEdit, QTextEdit, QComboBox, QCheckBox, 
                            QRadioButton, QSlider, QProgressBar, QSpinBox, QDoubleSpinBox,
                            QDateEdit, QTimeEdit, QDateTimeEdit, QListWidget, QTabWidget,
                            QMessageBox, QFileDialog, QInputDialog, QGroupBox,QHBoxLayout)
from PyQt6.QtCore import Qt, QDate, QTime, QDateTime

class MultiFunctionApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Зачет №2")
        self.setGeometry(100, 100, 800, 600)
        
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        
        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)
        
        self.tabs = QTabWidget()
        self.layout.addWidget(self.tabs)
        
        self.create_ui_tab()
        self.create_calculations_tab()
        self.create_text_operations_tab()
        self.create_file_operations_tab()
        self.create_settings_tab()
        
    
    def create_styled_group(self, title=None, color="#ffffff"):
        group = QGroupBox(title)
        group.setStyleSheet(f"""
            QGroupBox {{
                background-color: {color};
                border: 2px solid gray;
                border-radius: 5px;
                margin-top: 1ex;
                padding: 10px;
            }}
            QGroupBox::title {{
                subcontrol-origin: margin;
                left: 10px;
                padding: 0 3px;
            }}
        """)
        layout = QVBoxLayout()
        group.setLayout(layout)
        return group
    
    def create_ui_tab(self):
        tab = QWidget()
        self.tabs.addTab(tab, "UI Элементы")
        layout = QVBoxLayout()
        tab.setLayout(layout)
        
        # 1. Кнопка с сообщением (синяя группа)
        message_group = self.create_styled_group("Сообщения", "#e6f3ff")
        self.btn_show_message = QPushButton("Показать сообщение")
        self.btn_show_message.clicked.connect(self.show_message)
        message_group.layout().addWidget(self.btn_show_message)
        layout.addWidget(message_group)
        
        # 2. Метка с изменяемым текстом (оранжевая группа)
        label_group = self.create_styled_group("Метка", "#fff0e6")
        self.label = QLabel("Текст будет изменён")
        label_group.layout().addWidget(self.label)
        self.btn_change_label = QPushButton("Изменить текст метки")
        self.btn_change_label.clicked.connect(self.change_label_text)
        label_group.layout().addWidget(self.btn_change_label)
        layout.addWidget(label_group)
        
        # 3. Поле ввода с отображением текста (зелёная группа)
        input_group = self.create_styled_group("Поле ввода", "#e6ffe6")
        self.line_edit = QLineEdit()
        input_group.layout().addWidget(self.line_edit)
        self.btn_show_input = QPushButton("Показать введённый текст")
        self.btn_show_input.clicked.connect(self.show_input_text)
        input_group.layout().addWidget(self.btn_show_input)
        layout.addWidget(input_group)
        
        # 4. Выпадающий список (красная группа)
        combo_group = self.create_styled_group("Выбор варианта", "#ffe6e6")
        self.combo_box = QComboBox()
        self.combo_box.addItems(["Вариант 1", "Вариант 2", "Вариант 3"])
        combo_group.layout().addWidget(self.combo_box)
        self.btn_show_combo = QPushButton("Показать выбранный вариант")
        self.btn_show_combo.clicked.connect(self.show_combo_selection)
        combo_group.layout().addWidget(self.btn_show_combo)
        layout.addWidget(combo_group)
        
        # 5. Чекбоксы (фиолетовая группа)
        checkbox_group = self.create_styled_group("Чекбокс", "#f0e6ff")
        self.checkbox = QCheckBox("Согласен с условиями")
        checkbox_group.layout().addWidget(self.checkbox)
        self.btn_check_state = QPushButton("Проверить состояние")
        self.btn_check_state.clicked.connect(self.check_checkbox_state)
        checkbox_group.layout().addWidget(self.btn_check_state)
        layout.addWidget(checkbox_group)
    
    def create_calculations_tab(self):
        tab = QWidget()
        self.tabs.addTab(tab, "Вычисления")
        layout = QVBoxLayout()
        tab.setLayout(layout)
        
        # 6. Сложение чисел (голубая группа)
        sum_group = self.create_styled_group("Сложение чисел", "#e6f9ff")
        self.spin_box1 = QSpinBox()
        self.spin_box2 = QSpinBox()
        sum_group.layout().addWidget(QLabel("Число 1:"))
        sum_group.layout().addWidget(self.spin_box1)
        sum_group.layout().addWidget(QLabel("Число 2:"))
        sum_group.layout().addWidget(self.spin_box2)
        self.btn_calculate_sum = QPushButton("Сложить")
        self.btn_calculate_sum.clicked.connect(self.calculate_sum)
        sum_group.layout().addWidget(self.btn_calculate_sum)
        self.label_sum_result = QLabel("Результат: ")
        sum_group.layout().addWidget(self.label_sum_result)
        layout.addWidget(sum_group)
        
        # 7. Умножение (розовая группа)
        mul_group = self.create_styled_group("Умножение", "#ffebf3")
        self.double_spin1 = QDoubleSpinBox()
        self.double_spin2 = QDoubleSpinBox()
        mul_group.layout().addWidget(QLabel("Число 1:"))
        mul_group.layout().addWidget(self.double_spin1)
        mul_group.layout().addWidget(QLabel("Число 2:"))
        mul_group.layout().addWidget(self.double_spin2)
        self.btn_calculate_mul = QPushButton("Умножить")
        self.btn_calculate_mul.clicked.connect(self.calculate_multiplication)
        mul_group.layout().addWidget(self.btn_calculate_mul)
        self.label_mul_result = QLabel("Результат: ")
        mul_group.layout().addWidget(self.label_mul_result)
        layout.addWidget(mul_group)
        
        # 8. Прогресс бар (светло-зелёная группа)
        '''
        progress_group = self.create_styled_group("Прогресс", "#ebffe6")
        self.slider = QSlider(Qt.Orientation.Horizontal)
        self.progress_bar = QProgressBar()
        progress_group.layout().addWidget(self.slider)
        progress_group.layout().addWidget(self.progress_bar)
        self.slider.valueChanged.connect(self.progress_bar.setValue)
        layout.addWidget(progress_group)
        '''
        progress_group = self.create_styled_group("Прогресс-бар", "#ebffe6")
        self.slider = QSlider(Qt.Orientation.Horizontal)
        self.slider.setRange(0, 100)
        self.progress_bar = QProgressBar()
        progress_group.layout().addWidget(self.slider)
        progress_group.layout().addWidget(self.progress_bar)
        self.slider.valueChanged.connect(self.progress_with_bug)
        layout.addWidget(progress_group)
        
        # 9. Радио кнопки (светло-жёлтая группа)
        radio_group = self.create_styled_group("Выбор варианта", "#fffae6")
        self.radio1 = QRadioButton("Вариант 1")
        self.radio2 = QRadioButton("Вариант 2")
        radio_group.layout().addWidget(self.radio1)
        radio_group.layout().addWidget(self.radio2)
        self.btn_show_radio = QPushButton("Показать выбор")
        self.btn_show_radio.clicked.connect(self.show_radio_selection)
        radio_group.layout().addWidget(self.btn_show_radio)
        layout.addWidget(radio_group)
    
    def create_text_operations_tab(self):
        tab = QWidget()
        self.tabs.addTab(tab, "Текст")
        layout = QVBoxLayout()
        tab.setLayout(layout)
        
        # 10. Текстовое поле (светло-голубая группа)
        text_group = self.create_styled_group("Текстовое поле", "#e6f7ff")
        self.text_edit = QTextEdit()
        text_group.layout().addWidget(self.text_edit)
        layout.addWidget(text_group)
        
        # 11-14. Операции с текстом (разные группы)
        ops_group = self.create_styled_group("Операции с текстом", "#f5e6ff")
        self.btn_count_chars = QPushButton("Подсчитать символы")
        self.btn_count_chars.clicked.connect(self.count_characters)
        ops_group.layout().addWidget(self.btn_count_chars)
        self.label_char_count = QLabel("Символов: 0")
        ops_group.layout().addWidget(self.label_char_count)
        
        self.btn_count_words = QPushButton("Подсчитать слова")
        self.btn_count_words.clicked.connect(self.count_words)
        ops_group.layout().addWidget(self.btn_count_words)
        self.label_word_count = QLabel("Слов: 0")
        ops_group.layout().addWidget(self.label_word_count)
        
        self.btn_uppercase = QPushButton("В ВЕРХНИЙ РЕГИСТР")
        self.btn_uppercase.clicked.connect(self.convert_to_uppercase)
        ops_group.layout().addWidget(self.btn_uppercase)
        
        self.btn_clear_text = QPushButton("Очистить текст")
        self.btn_clear_text.clicked.connect(self.clear_text)
        ops_group.layout().addWidget(self.btn_clear_text)
        layout.addWidget(ops_group)
    
    def create_file_operations_tab(self):
        tab = QWidget()
        self.tabs.addTab(tab, "Файлы")
        layout = QVBoxLayout()
        tab.setLayout(layout)
        
        # 15-16. Файловые операции (бежевая группа)
        file_group = self.create_styled_group("Файловые операции", "#fff5e6")
        self.btn_open_file = QPushButton("Открыть файл")
        self.btn_open_file.clicked.connect(self.open_file)
        file_group.layout().addWidget(self.btn_open_file)
        self.label_file_content = QTextEdit()
        self.label_file_content.setReadOnly(True)
        file_group.layout().addWidget(self.label_file_content)
        
        self.btn_save_file = QPushButton("Сохранить файл")
        self.btn_save_file.clicked.connect(self.save_file)
        file_group.layout().addWidget(self.btn_save_file)
        layout.addWidget(file_group)
        
        # 17-18. Дата и время (мятная группа)
        datetime_group = self.create_styled_group("Дата и время", "#e6fff0")
        self.btn_show_date = QPushButton("Показать текущую дату")
        self.btn_show_date.clicked.connect(self.show_current_date)
        datetime_group.layout().addWidget(self.btn_show_date)
        self.label_date = QLabel()
        datetime_group.layout().addWidget(self.label_date)
        
        self.date_edit = QDateEdit()
        self.time_edit = QTimeEdit()
        self.date_time_edit = QDateTimeEdit()
        datetime_group.layout().addWidget(self.date_edit)
        datetime_group.layout().addWidget(self.time_edit)
        datetime_group.layout().addWidget(self.date_time_edit)
        self.btn_show_datetime = QPushButton("Показать выбранное")
        self.btn_show_datetime.clicked.connect(self.show_selected_datetime)
        datetime_group.layout().addWidget(self.btn_show_datetime)
        layout.addWidget(datetime_group)
    
    def create_settings_tab(self):
        tab = QWidget()
        self.tabs.addTab(tab, "Настройки")
        layout = QVBoxLayout()
        tab.setLayout(layout)
        
        # 19-21. Настройки (светло-розовая группа)
        settings_group = self.create_styled_group("Настройки", "#ffe6f0")
        self.btn_toggle_theme = QPushButton("Тёмная тема")
        self.btn_toggle_theme.clicked.connect(self.toggle_theme)
        settings_group.layout().addWidget(self.btn_toggle_theme)
        
        self.list_widget = QListWidget()
        self.list_widget.addItems(["Элемент 1", "Элемент 2", "Элемент 3"])
        settings_group.layout().addWidget(self.list_widget)
        
        buttons_layout = QHBoxLayout()
        self.btn_add_item = QPushButton("Добавить элемент")
        self.btn_add_item.clicked.connect(self.add_list_item)
        buttons_layout.addWidget(self.btn_add_item)
        
        self.btn_remove_item = QPushButton("Удалить выбранный")
        self.btn_remove_item.clicked.connect(self.remove_list_item)
        buttons_layout.addWidget(self.btn_remove_item)
        
        settings_group.layout().addLayout(buttons_layout)
        layout.addWidget(settings_group)
    
    # Реализации функций
    
    def progress_with_bug(self, value):
        if value == 100:
            value = 99 
            # БАГ №2 ОГРАНИЧЕНИЕ ПРОГРЕСС БАРА УСТРОНЕНИЕ ПРОСТО УБРАТЬ ОГРАНИЧЕНИЕ
        self.progress_bar.setValue(value)
    
    def show_message(self):
        QMessageBox.information(self, "Сообщение", "Это окно сообщения!")
    
    def change_label_text(self):
        self.label.setText("Текст изменился!")
    
    def show_input_text(self):
        text = self.line_edit.text()
        QMessageBox.information(self, "Введённый текст", f"Вы ввели: {text}")
    
    def show_combo_selection(self):
        text = self.combo_box.currentText()
        QMessageBox.information(self, "Выбор", f"Вы выбрали: {text}")
    
    def check_checkbox_state(self):
        state = "согласен" if self.checkbox.isChecked() else "не согласен"
        QMessageBox.information(self, "Состояние", f"Пользователь {state} с условиями")
    
    def calculate_sum(self):
        #БАГ №3 ОБЪЕДЕНЕНИЕ ЧИСЕЛ ВМЕСТО СЛОЖЕНИЕ
        num1 = self.spin_box1.value()
        num2 = self.spin_box2.value()
        self.label_sum_result.setText(f"Результат: {str(num1) + str(num2)}")
        # Правильная реализация
        # self.label_sum_result.setText(f"Результат: {num1 + num2}")
    
    def calculate_multiplication(self):
        num1 = self.double_spin1.value()
        num2 = self.double_spin2.value()
        self.label_mul_result.setText(f"Результат: {num1 * num2:.2f}")
    
    def show_radio_selection(self):
        if self.radio1.isChecked():
            text = "Вариант 1"
            # БАГ: При выборе варианта B ничего не показывается
            QMessageBox.information(self, "Выбор", f"Выбрано: {text}")
            # Правильная реализация должна быть:
            # text = "Вариант A" if self.radio1.isChecked() else "Вариант B"
            # QMessageBox.information(self, "Выбор", f"Выбрано: {text}")
    
    def count_characters(self):
        text = self.text_edit.toPlainText()
        self.label_char_count.setText(f"Символов: {len(text)}")
    
    def count_words(self):
        text = self.text_edit.toPlainText()
        words = len(text.split())
        self.label_word_count.setText(f"Слов: {words}")
    
    def convert_to_uppercase(self):
        text = self.text_edit.toPlainText()
        self.text_edit.setPlainText(text.upper())
    
    def clear_text(self):
        #БАГ №4 НЕ ОЧИЩАЕТСЯ ПОЛЕ ТЕКСТ
        # ПРАВИЛЬНАЯ РЕАЛИЗАЦИЯ self.text_edit.clear()
        pass
    
    def open_file(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Открыть файл", "", "Текстовые файлы (*.txt);;Все файлы (*)")
        if file_name:
            with open(file_name, 'r', encoding='utf-8') as file:
                self.label_file_content.setPlainText(file.read())
    
    def save_file(self):
        file_name, _ = QFileDialog.getSaveFileName(self, "Сохранить файл", "", "Текстовые файлы (*.txt);;Все файлы (*)")
        if file_name:
            with open(file_name, 'w', encoding='utf-8') as file:
                file.write(self.label_file_content.toPlainText())
            QMessageBox.information(self, "Сохранение", "Файл успешно сохранён")
    
    def show_current_date(self):
        current_date = QDate.currentDate().toString("dd.MM.yyyy")
        self.label_date.setText(f"Текущая дата: {current_date}")
    
    def show_selected_datetime(self):
        date = self.date_edit.date().toString("dd.MM.yyyy")
        time = self.time_edit.time().toString("hh:mm")
        datetime = self.date_time_edit.dateTime().toString("dd.MM.yyyy hh:mm")
        QMessageBox.information(self, "Дата и время", 
                               f"Дата: {date}\nВремя: {time}\nДата и время: {datetime}")
    
    def toggle_theme(self):
        #БАГ №5 ПЕРЕКЛЮЧЕНИЕ ТЕМЫ НЕ РАБОТАЕТ
        pass
        '''
        ПРАВИЛЬНАЯ РЕАЛИЗАЦИЯ
        if self.btn_toggle_theme.text() == "Тёмная тема":
            self.setStyleSheet("background-color: #333; color: white;")
            self.btn_toggle_theme.setText("Светлая тема")
        else:
            self.setStyleSheet("")
            self.btn_toggle_theme.setText("Тёмная тема")
        '''
    
    def add_list_item(self):
        #text, ok = QInputDialog.getText(self, "Добавить элемент", "Введите текст:")
        #if ok and text:
        #    self.list_widget.addItem(text)
        text, ok = QInputDialog.getText(self, "Добавить элемент", "Введите текст:")
        if ok and text:
        # Проверяем, существует ли уже такой элемент
            items = [self.list_widget.item(i).text() for i in range(self.list_widget.count())]
            if text not in items:
                self.list_widget.addItem(text)
            else:
                QMessageBox.warning(self, "Ошибка", "Такой элемент уже существует!")
    
    def remove_list_item(self):
        current_item = self.list_widget.currentItem()
        if current_item:
            self.list_widget.takeItem(self.list_widget.row(current_item))
            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MultiFunctionApp()
    window.show()
    sys.exit(app.exec())
