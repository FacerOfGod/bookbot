class StyleManager:
    @staticmethod
    def get_button_style():
        return """
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
        """

    @staticmethod
    def get_upload_button_style():
        return """
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
        """

    @staticmethod
    def get_empty_box_style():
        return """
        background-color: #f0f0f0;
        border: 2px solid #333;
        border-radius: 10px;
        """ 