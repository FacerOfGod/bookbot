import sys

from PySide6.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget
from src.cli.cli_app import run_cli_app 
from src.views.main_window import MainWindow
from src.utils import *

def main():
    if len(sys.argv) > 1 and sys.argv[1] == "cli":
        run_cli_app()
    else:

        app = QApplication([]) # Putting [] because for now I don't see the point of argv
        window = MainWindow()
        window.show()
        app.exec()


if __name__ == "__main__":
    main()


