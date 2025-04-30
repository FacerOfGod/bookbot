import os

from PySide6.QtCore import Qt
from PySide6.QtWidgets import *
from PySide6.QtGui import QFont
from src.controllers.main_controller import MainController
from src.utils.bar_chart import BarChart
from src.utils.style_manager import StyleManager

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.controller = MainController(self)
        self.bar_chart = BarChart()

        self.setWindowTitle("Cool Interface")
        self.setMinimumSize(400, 300)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # Bar chart widget
        self.bar_chart.setMinimumSize(200, 150)
        self.bar_chart.setStyleSheet(StyleManager.get_empty_box_style())

        # Button to upload file that we want chatacter statics
        self.buttonUpload = QPushButton("Upload file here")
        self.buttonUpload.setFont(QFont("Arial", 12, QFont.Bold))
        self.buttonUpload.setStyleSheet(StyleManager.get_upload_button_style())
        self.buttonUpload.clicked.connect(self.controller.upload_document)

        # Button to later confirm the fact that we what to analyse the current file
        self.button = QPushButton("Click Me!")
        self.button.setFont(QFont("Arial", 12, QFont.Bold))
        self.button.setStyleSheet(StyleManager.get_button_style())
        self.button.clicked.connect(self.controller.the_button_was_clicked)

        layout.addWidget(self.bar_chart, alignment=Qt.AlignCenter)
        layout.addWidget(self.buttonUpload, alignment=Qt.AlignCenter)
        layout.addWidget(self.button, alignment=Qt.AlignCenter)

    def update_buttonUpload_text(self, new_text):
        self.buttonUpload.setText(new_text)
        print(self.file_path)
    
    def set_file_path(self, file_path):
        self.bar_chart.create_chart(file_path)
        self.file_path = file_path


    
