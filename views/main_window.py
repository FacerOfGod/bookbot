import os

from PySide6.QtCore import Qt
from PySide6.QtWidgets import *
from PySide6.QtGui import QFont
from controllers.main_controller import MainController

#TODO figure a better way to implement styles
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

        self.empty_box = QWidget()
        self.empty_box.setMinimumSize(200, 150)
        self.empty_box.setStyleSheet("background-color: #f0f0f0; border: 2px solid #333; border-radius: 10px;")

        self.buttonUpload = QPushButton("Upload file here")
        self.buttonUpload.setFont(QFont("Arial", 12, QFont.Bold))
        self.buttonUpload.setStyleSheet("""
        QPushButton {
                background-color: #2196F3;
                color: white;
                border: none;
                padding: 10px 20px;
                border-radius: 5px;
                min-width: 120px;
            }
            QPushButton:hover {
                background-color: #1976D2;
            }
            QPushButton:pressed {
                background-color: #1565C0;
            }
        """)
        self.buttonUpload.clicked.connect(self.controller.upload_document)


        self.button = QPushButton("Click Me!")
        self.button.setFont(QFont("Arial", 12, QFont.Bold))
        self.button.setStyleSheet("""
        QPushButton {
                background-color: #4CAF50;
                color: white;
                border: none;
                padding: 10px 20px;
                border-radius: 5px;
                min-width: 120px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
            QPushButton:pressed {
                background-color: #3d8b40;
            }
        """)
        self.button.clicked.connect(self.controller.the_button_was_clicked)

        layout.addWidget(self.empty_box, alignment=Qt.AlignCenter)
        layout.addWidget(self.buttonUpload, alignment=Qt.AlignCenter)
        layout.addWidget(self.button, alignment=Qt.AlignCenter)

    def update_buttonUpload_text(self, new_text):
        self.buttonUpload.setText(new_text)
    
