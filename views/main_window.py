from PySide6.QtCore import Qt
from PySide6.QtWidgets import *
from PySide6.QtGui import QFont

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Cool Interface")
        self.setMinimumSize(400, 300)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        self.empty_box = QWidget()
        self.empty_box.setMinimumSize(200, 150)
        self.empty_box.setStyleSheet("background-color: #f0f0f0; border: 2px solid #333; border-radius: 10px;")

        self.button = QPushButton("Click Me!")
        self.button.setFont(QFont("Arial", 12, QFont.Bold))

        #TODO figure a better way to implement styles
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
        self.button.clicked.connect(self.the_button_was_clicked)

        layout.addWidget(self.empty_box, alignment=Qt.AlignCenter)
        layout.addWidget(self.button, alignment=Qt.AlignCenter)
    
    def the_button_was_clicked(self):
        self.button.setText("You clicked me!")
        self.button.setEnabled(False)
        self.setWindowTitle("Button Clicked!")