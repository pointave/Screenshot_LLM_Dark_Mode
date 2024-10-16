# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets 

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.MainWindow = MainWindow

        self.MainWindow.setObjectName("MainWindow")
        self.MainWindow.resize(640, 794)
        self.MainWindow.setStyleSheet(self.get_stylesheet())
        font = QtGui.QFont("Segoe UI", 10)

        # Set window flags to make it always on top
        self.MainWindow.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.setContentsMargins(20, 20, 20, 20)
        self.verticalLayout.setSpacing(20)

        self.setup_main_tab(font)
        self.setup_settings_tab(font)

        self.tab_widget = QtWidgets.QTabWidget(self.centralwidget)
        self.tab_widget.setFont(font)
        self.tab_widget.setObjectName("tab_widget")
        self.tab_widget.addTab(self.tab1, "Main")
        self.tab_widget.addTab(self.tab2, "Settings")
        self.verticalLayout.addWidget(self.tab_widget)

        # Add grey text at the bottom
        self.credit_label = QtWidgets.QLabel(self.centralwidget)
        self.credit_label.setStyleSheet("color: #a0a0a0; font-size: 10px;")
        self.credit_label.setText("Created by <a href='https://github.com/ThanabordeeN/Screenshot_LLM'>ThanabordeeN</a>")
        self.credit_label.setAlignment(QtCore.Qt.AlignCenter)
        self.credit_label.setOpenExternalLinks(True)
        self.verticalLayout.addWidget(self.credit_label)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Set default position to top-right corner of the screen
        screen_geometry = QtWidgets.QDesktopWidget().screenGeometry()
        x = screen_geometry.width() - self.MainWindow.width()
        y = 0
        self.MainWindow.move(x, y)

        # Set window icon (use a light-colored icon for dark theme)
        icon = QtGui.QIcon("icon_light.ico")  # Make sure you have a light version of your icon
        self.MainWindow.setWindowIcon(icon)

    def setup_main_tab(self, font):
        self.tab1 = QtWidgets.QWidget()
        self.tab1.setObjectName("tab1")
        self.tab1_layout = QtWidgets.QVBoxLayout(self.tab1)
        self.tab1_layout.setObjectName("tab1_layout")

        self.image_label = self.create_label()
        self.tab1_layout.addWidget(self.image_label)

        self.conversation = self.create_text_edit()
        self.tab1_layout.addWidget(self.conversation)

        self.entry = self.create_line_edit(font)
        self.tab1_layout.addWidget(self.entry)

        self.loading_label = self.create_label()
        self.loading_label.setStyleSheet("color: #4a9eff;")
        self.loading_label.setFont(font)
        self.tab1_layout.addWidget(self.loading_label)

        self.send_button = QtWidgets.QPushButton(self.tab1)
        self.send_button.setFont(font)
        self.send_button.setObjectName("send_button")
        self.tab1_layout.addWidget(self.send_button)

        self.reset_memory = QtWidgets.QPushButton(self.tab1)
        self.reset_memory.setFont(font)
        self.reset_memory.setObjectName("reset_memory")
        self.reset_memory.setText("Reset Memory")
        self.tab1_layout.addWidget(self.reset_memory)

    def setup_settings_tab(self, font):
        self.tab2 = QtWidgets.QWidget()
        self.tab2.setObjectName("tab2")
        self.tab2_layout = QtWidgets.QVBoxLayout(self.tab2)
        self.tab2_layout.setObjectName("tab2_layout")

        self.api_key_label = QtWidgets.QLabel(self.tab2)
        self.api_key_label.setFont(font)
        self.api_key_label.setObjectName("api_key_label")
        self.api_key_label.setText("LLM API Key \n (Any API Key for Ollama)")
        self.api_key_label.setAlignment(QtCore.Qt.AlignCenter)
        self.tab2_layout.addWidget(self.api_key_label)

        self.api_key_input = QtWidgets.QLineEdit(self.tab2)
        self.api_key_input.setFont(font)
        self.api_key_input.setObjectName("api_key_input")
        self.api_key_input.setPlaceholderText("Get your API key from Provider's website")
        self.api_key_input.setAlignment(QtCore.Qt.AlignCenter)
        self.api_key_input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.tab2_layout.addWidget(self.api_key_input)

        self.model_id_label = QtWidgets.QLabel(self.tab2)
        self.model_id_label.setAlignment(QtCore.Qt.AlignCenter)
        self.model_id_label.setFont(font)
        self.model_id_label.setObjectName("model_id_label")
        self.model_id_label.setText("Model ID")
        self.tab2_layout.addWidget(self.model_id_label)

        self.model_id_input = QtWidgets.QLineEdit(self.tab2)
        self.model_id_input.setFont(font)
        self.model_id_input.setObjectName("model_id_input")
        self.model_id_input.setAlignment(QtCore.Qt.AlignCenter)
        self.model_id_input.setPlaceholderText("Default : minicpm-v:latest")
        self.tab2_layout.addWidget(self.model_id_input)
        
        self.description_label = QtWidgets.QLabel(self.tab2)
        self.description_label.setFont(font)
        self.description_label.setObjectName("description_label")
        self.description_label.setText("<b>Description</b> \n Powered by Ollama and LiteLLM. \
            <a href='https://docs.litellm.ai/docs/'>LiteLLM Documentation</a>\n  ")
        self.description_label.setAlignment(QtCore.Qt.AlignCenter)
        self.tab2_layout.addWidget(self.description_label)
        
        self.ollama_checkbox = QtWidgets.QCheckBox(self.tab2)
        self.ollama_checkbox.setFont(font)
        self.ollama_checkbox.setObjectName("ollama_checkbox")
        self.ollama_checkbox.setText("Ollama")
        self.tab2_layout.addWidget(self.ollama_checkbox)
        
        self.save_button = QtWidgets.QPushButton(self.tab2)
        self.save_button.setFont(font)
        self.save_button.setObjectName("save_button")
        self.save_button.setText("Save")
        self.tab2_layout.addWidget(self.save_button)

        self.reset_config = QtWidgets.QPushButton(self.tab2)
        self.reset_config.setFont(font)
        self.reset_config.setObjectName("reset_config")
        self.reset_config.setText("Reset Config")
        self.tab2_layout.addWidget(self.reset_config)

    def get_stylesheet(self):
        return """
            QMainWindow, QTabWidget, QWidget {
                background-color: #2b2b2b;
                color: #e0e0e0;
            }
            QTabWidget::pane {
                border: 1px solid #555555;
            }
            QTabBar::tab {
                background-color: #3a3a3a;
                color: #e0e0e0;
                padding: 8px 12px;
                border-top-left-radius: 4px;
                border-top-right-radius: 4px;
            }
            QTabBar::tab:selected {
                background-color: #4a4a4a;
            }
            QLabel, QTextEdit, QLineEdit, QPushButton, QCheckBox {
                border: none;
                border-radius: 6px;
                padding: 8px;
                background-color: #3a3a3a;
                color: #e0e0e0;
            }
            QScrollBar {
                background: #3a3a3a;
                border-radius: 6px;
            }
            QScrollBar::handle {
                background: #5a5a5a;
                border-radius: 6px;
            }
            QScrollBar::handle::pressed {
                background: #6a6a6a;
            }
            QLabel {
                background-color: #333333;
            }
            QTextEdit, QLineEdit {
                background-color: #333333;
                border: 1px solid #555555;
            }
            QPushButton {
                background-color: #0056b3;
                color: #ffffff;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #0066cc;
            }
            QPushButton:pressed {
                background-color: #004080;
            }
            QCheckBox {
                spacing: 5px;
            }
            QCheckBox::indicator {
                width: 18px;
                height: 18px;
                border-radius: 3px;
                border: 1px solid #555555;
            }
            QCheckBox::indicator:unchecked {
                background-color: #2b2b2b;
            }
            QCheckBox::indicator:checked {
                background-color: #0056b3;
            }
        """

    def create_label(self):
        label = QtWidgets.QLabel(self.centralwidget)
        label.setAlignment(QtCore.Qt.AlignCenter)
        label.setStyleSheet("border-radius: 10px;")
        label.setObjectName("image_label")
        label.setFont(QtGui.QFont("Segoe UI", 10))
        return label

    def create_text_edit(self):
        text_edit = QtWidgets.QTextEdit(self.centralwidget)
        text_edit.setReadOnly(True)
        text_edit.setStyleSheet("border-radius: 10px;")
        text_edit.setObjectName("conversation")
        text_edit.setFont(QtGui.QFont("Segoe UI", 10))
        return text_edit

    def create_line_edit(self, font):
        line_edit = QtWidgets.QLineEdit(self.centralwidget)
        line_edit.setPlaceholderText("Type your message here...")
        line_edit.setFocus()
        line_edit.setFont(font)
        line_edit.setObjectName("entry")
        return line_edit

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Screenshot LLM"))
        self.send_button.setText(_translate("MainWindow", "Send"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
