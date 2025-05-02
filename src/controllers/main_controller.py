import os

from PySide6.QtWidgets import QFileDialog

from src.utils import scraper

output_folder = "ressources/wikipedia"

class MainController:

    def __init__(self, view):
        self.view: MainController = view

    def the_button_was_clicked(self):
        user_input = self.view.input_box.text()
        summary = scraper.search_and_summarize(user_input)


        if not os.path.exists(output_folder):
            os.makedirs(output_folder, exist_ok=True)

        file_path = f"{output_folder}/{user_input}.txt"

        with open(file_path, "w", encoding="utf-8") as file:
            file.write(summary)

        self.view.set_file_path(file_path)


    def upload_document(self):
        file_path, _ = QFileDialog.getOpenFileName(None, "Choose file", "", "All Files (*)")
        self.view.set_file_path(file_path)

    def toggle_button_wiki(self):
        if self.view.input_box.text():  
            self.view.button.setEnabled(True) 
        else:
            self.view.button.setEnabled(False)
    