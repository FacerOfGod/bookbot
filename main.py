import sys
import time
import argparse
import os

from pathlib import Path

from PySide6.QtWidgets import QApplication, QSplashScreen, QLabel
from PySide6.QtGui import QPixmap 
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import Qt

from src.cli.cli_app import run_cli_app 
from src.views.main_window import MainWindow
from src.utils import *


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.abspath("."))
    return os.path.join(base_path, relative_path)

icon_path_splash = resource_path("src/images/bookbot_logo.png")


def parse_args():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description="BookBot - A tool for analyzing text files and books",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
            Examples:
            python main.py cli --file book.txt
            python main.py cli -f book.txt
        """
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    cli_parser = subparsers.add_parser('cli', help='Run BookBot in CLI mode')
    
    cli_parser.add_argument(
        '-f', '--file',
        required=True,
        type=str,
        help='Path to the text file to analyze'
    )
    
    return parser.parse_args()


def main():
    try:
        args = parse_args()
        
        if args.command == 'cli':
            file_path = Path(args.file)
            if not file_path.exists():
                print(f"Error: File '{args.file}' does not exist")
                sys.exit(1)
            if not file_path.is_file():
                print(f"Error: '{args.file}' is not a file")
                sys.exit(1)
            
            run_cli_app(str(file_path))
        else:
            app = QApplication([]) 

            splash_pix = QPixmap(icon_path_splash)
            splash_pix = splash_pix.scaled(150, 150)
            splash = QSplashScreen(splash_pix)
            splash.setWindowFlag(Qt.WindowStaysOnTopHint)

            splash.show()

            time.sleep(2)

            window = MainWindow()
            window.setWindowFlag(Qt.WindowStaysOnTopHint)
            window.show()


            splash.finish(window)
            sys.exit(app.exec())
            
    except argparse.ArgumentError as e:
        print(f"Error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()


