
from PySide6.QtWidgets import QMessageBox
from duckduckgo_search.exceptions import DuckDuckGoSearchException, RatelimitException, TimeoutException

ERROR_MESSAGES = {
    RatelimitException: "This program uses the free DuckDuckGo search functionality that has a limited number search per minute so just be patient",
    TimeoutException: "DuckDuckGo has a problem on their side",
    RuntimeError: "DuckDuckGo has a problem on their side",
    #DuckDuckGoSearchException: "There are no wikipedia results for what you searched",
    FileNotFoundError: "The file you are trying to load doesn't exist"

}

def show_error(error):
    msg_box = QMessageBox()
    msg_box.setIcon(QMessageBox.Critical)
    msg_box.setWindowTitle("Small error happened")
    msg_box.setInformativeText(ERROR_MESSAGES.get(type(error), f"Unexpected error: {str(error)}"))
    msg_box.exec()