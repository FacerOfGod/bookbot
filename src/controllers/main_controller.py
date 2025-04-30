import os

from PySide6.QtWidgets import QFileDialog

class MainController:
    def __init__(self, view):
        self.view = view

    def the_button_was_clicked(self):
        self.button.setText("You clicked me!")
        self.button.setEnabled(False)
        self.setWindowTitle("Button Clicked!")

    def upload_document(self) -> str:
        file_path, _ = QFileDialog.getOpenFileName(None, "Choose file", "", "All Files (*)")
        if file_path:
            file_name = os.path.basename(file_path)
        else:
            file_name = "Error File"
        self.view.set_file_path(file_path)
        self.view.update_buttonUpload_text(file_name)
        return file_name
    