import os

from PySide6.QtCore import Qt
from PySide6.QtWidgets import *
from PySide6.QtGui import QFont, QIcon, QPainter, QColor
from src.controllers.main_controller import MainController
from src.utils.bar_chart import BarChart
from src.utils.style_manager import StyleManager

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.controller = MainController(self)
        self.bar_chart = BarChart()
        self.file_path = None

        self.setWindowTitle("Cool Interface")
        self.setMinimumSize(400, 300)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # Button to upload file that we want chatacter statics
        self.buttonUpload = QPushButton("Upload file here")
        self.buttonUpload.setFont(QFont("Arial", 12, QFont.Bold))
        self.buttonUpload.setStyleSheet(StyleManager.get_upload_button_style())
        self.buttonUpload.clicked.connect(self.controller.upload_document)
        self.buttonUpload.setSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)

        # Create a custom light red delete icon
        delete_icon = QIcon.fromTheme("edit-delete")
        pixmap = delete_icon.pixmap(16, 16)
        painter = QPainter(pixmap)
        painter.setCompositionMode(QPainter.CompositionMode_SourceIn)
        painter.fillRect(pixmap.rect(), QColor("#FFFFFF"))
        painter.end()
        custom_icon = QIcon(pixmap)

        # Delete icon button
        self.buttonDelete = QToolButton(self.buttonUpload)
        self.buttonDelete.setIcon(custom_icon)
        self.buttonDelete.setStyleSheet(StyleManager.get_delete_button_style())
        self.buttonDelete.clicked.connect(self.reset_graph)
        self.buttonDelete.setVisible(False)
        self.buttonDelete.setFixedSize(20, 20)

        # Connect resize event to update delete button position
        self.buttonUpload.installEventFilter(self)

        # Create input box
        self.input_box = QLineEdit()
        self.input_box.setPlaceholderText("Type here...")
        self.input_box.setStyleSheet(StyleManager.get_input_box_style())
        self.input_box.textChanged.connect(self.controller.toggle_button_wiki)



        # Button to later confirm the fact that we what to analyse the current file
        self.button = QPushButton("Wiki search")
        self.button.setFont(QFont("Arial", 12, QFont.Bold))
        self.button.setStyleSheet(StyleManager.get_button_style())
        self.button.clicked.connect(self.controller.the_button_was_clicked)
        self.button.setEnabled(False)

        h_layout = QHBoxLayout()
        h_layout.addWidget(self.buttonUpload)
        h_layout.addWidget(self.input_box)
        h_layout.addWidget(self.button)

        layout.addWidget(self.bar_chart, alignment=Qt.AlignCenter)
        layout.addLayout(h_layout)

    def eventFilter(self, obj, event):
        if obj == self.buttonUpload and event.type() == event.Type.Resize:
            if self.buttonDelete.isVisible():
                self.buttonDelete.move(self.buttonUpload.width() - 25, (self.buttonUpload.height() - 20) // 2)
        return super().eventFilter(obj, event)
    
    def set_file_path(self, file_path):
        self.bar_chart.create_chart(file_path)
        self.file_path = file_path
        self.buttonDelete.setVisible(file_path is not None)

        if file_path:
            self.buttonUpload.setText(os.path.basename(file_path))
            self.buttonDelete.move(self.buttonUpload.width() - 25, (self.buttonUpload.height() - 20) // 2)
        else:
            self.reset_graph()

    def reset_graph(self):
        self.file_path = None
        self.bar_chart.clear()
        self.buttonDelete.setVisible(False)
        self.buttonUpload.setText("Upload file here")
