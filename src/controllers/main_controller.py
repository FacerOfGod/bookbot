import os

from PySide6.QtWidgets import QFileDialog

from src.utils import scraper

output_folder = "ressources/wikipedia"

class MainController:

    def __init__(self, view):
        self.view: MainController = view
        self.file_path = None


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
        self.view.bar_chart.create_chart(file_path)
        self.file_path = file_path
        self.view.buttonDelete.setVisible(file_path is not None)

        if file_path:
            self.view.buttonUpload.setText(os.path.basename(file_path))
            self.view.buttonDelete.move(self.view.buttonUpload.width() - 25, (self.view.buttonUpload.height() - 20) // 2)
        else:
            self.reset_graph()

    def toggle_button_wiki(self):
        if self.view.input_box.text():  
            self.view.button.setEnabled(True) 
        else:
            self.view.button.setEnabled(False)

       
    def reset_graph(self):
        self.file_path = None
        self.view.bar_chart.clear()
        self.view.buttonDelete.setVisible(False)
        self.view.buttonUpload.setText("Upload file here")
    
       