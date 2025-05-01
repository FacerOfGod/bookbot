import os

from PySide6.QtWidgets import QFileDialog

class MainController:
    def __init__(self, view):
        self.view = view

    def the_button_was_clicked(self):
        self.button.setText("You clicked me!")
        self.button.setEnabled(False)
        self.setWindowTitle("Button Clicked!")

    def upload_document(self):
        file_path, _ = QFileDialog.getOpenFileName(None, "Choose file", "", "All Files (*)")
        self.view.set_file_path(file_path)
    