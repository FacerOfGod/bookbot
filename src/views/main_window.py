import os

from PySide6.QtCore import Qt
from PySide6.QtWidgets import *
from PySide6.QtGui import QFont
from src.controllers.main_controller import MainController
from src.utils.style_manager import StyleManager

class MainWindow(QMainWindow):
    file_path = None

    def __init__(self):
        super().__init__()
        self.controller = MainController(self)

        self.setWindowTitle("Cool Interface")
        self.setMinimumSize(400, 300)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # Empty box that is later going to be the graph
        self.empty_box = QWidget()
        self.empty_box.setMinimumSize(200, 150)
        self.empty_box.setStyleSheet(StyleManager.get_empty_box_style())

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

        layout.addWidget(self.empty_box, alignment=Qt.AlignCenter)
        layout.addWidget(self.buttonUpload, alignment=Qt.AlignCenter)
        layout.addWidget(self.button, alignment=Qt.AlignCenter)

    def update_buttonUpload_text(self, new_text):
        self.buttonUpload.setText(new_text)
    
