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

        QPushButton:disabled {
            background-color: #d3d3d3;  
            color: #a9a9a9;             
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
    def get_delete_button_style():
        return """
        QToolButton {
            border: none;
            background: transparent;
            padding: 2px;
            color: #ff6b6b;
            font-weight: bold;
        }
        QToolButton:hover {
            background: rgba(255, 0, 0, 0.5);
            border-radius: 4px;
        }
        """

    @staticmethod
    def get_empty_box_style():
        return """
        background-color: #f0f0f0;
        border: 2px solid #333;
        border-radius: 10px;
        """ 
    
    @staticmethod
    def get_input_box_style():
        return """
        QLineEdit {
            padding: 8px 12px;
            border: 2px solid #2196F3;
            border-radius: 5px;
            font-size: 14px;
            background-color: #ffffff;
            color: #333;
        }
        QLineEdit:focus {
            border-color: #1976D2;
            background-color: #f0f8ff;
        }
        """