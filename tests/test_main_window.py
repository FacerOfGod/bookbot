import pytest
from PySide6.QtCore import Qt
from src.views.main_window import MainWindow 

@pytest.fixture
def main_window(qtbot):
    """Fixture to create the main window."""
    window = MainWindow()
    qtbot.addWidget(window)
    window.show()
    return window

def test_initial_state(main_window):
    """Check initial GUI state."""
    assert main_window.file_path is None
    assert main_window.buttonUpload.text() == "Upload file here"
    assert not main_window.buttonDelete.isVisible()

def test_wiki_button(main_window, ):
    """Check Wiki button state."""
    assert main_window.file_path is None
    assert main_window.button.text() == "Wiki search"
    assert not main_window.button.isEnabled()
    main_window.input_box.setText("Test")
    assert main_window.button.isEnabled()


def test_set_file_path(main_window, tmp_path):
    """Test that setting a file path updates the GUI."""
    dummy_file = tmp_path / "dummy.txt"
    dummy_file.write_text("dummy content")

    main_window.set_file_path(str(dummy_file))

    assert main_window.file_path == str(dummy_file)
    assert main_window.buttonUpload.text() == "dummy.txt"
    assert main_window.buttonDelete.isVisible()

def test_reset_graph(main_window, qtbot, tmp_path):
    """Test reset_graph clears the chart and resets the button."""
    dummy_file = tmp_path / "dummy.txt"
    dummy_file.write_text("dummy content")

    main_window.set_file_path(str(dummy_file))
    assert main_window.buttonDelete.isVisible()

    qtbot.mouseClick(main_window.buttonDelete, Qt.LeftButton)

    assert main_window.file_path is None
    assert main_window.buttonUpload.text() == "Upload file here"
    assert not main_window.buttonDelete.isVisible()