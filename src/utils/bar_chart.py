from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from PySide6.QtWidgets import QWidget, QVBoxLayout

from src.utils.stats import file_path_to_stats

class BarChart(QWidget):
    """
    A Qt widget that displays a bar chart of character occurrences from a text file.
    
    This class creates an interactive bar chart that can be embedded in a Qt application.
    It visualizes the frequency of characters in a given text file, with characters
    on the x-axis and their occurrence counts on the y-axis.
    
    Attributes:
        figure (Figure): The matplotlib figure object that contains the chart
        canvas (FigureCanvas): The Qt canvas that renders the matplotlib figure
        ax (Axes): The matplotlib axes object for the bar chart
    """
    
    def __init__(self, parent=None):
        """
        Initialize the BarChart widget.
        
        Args:
            parent (QWidget, optional): The parent widget. Defaults to None.
        """
        super().__init__(parent)
        self.figure = Figure(figsize=(5, 4), dpi=100)
        self.canvas = FigureCanvas(self.figure)
        self.ax = self.figure.add_subplot(111)
        
        layout = QVBoxLayout(self)
        layout.addWidget(self.canvas)
        self.setLayout(layout)
        
    def create_chart(self, file_path):
        """
        Create and display a bar chart from the character statistics of a file.
        
        This method reads the file, processes its contents to get character statistics,
        and creates a bar chart visualization. The chart shows each character on the
        x-axis and its occurrence count on the y-axis.
        
        Args:
            file_path (str): Path to the text file to analyze
            
        Note:
            The chart will automatically update if this method is called multiple times
            with different file paths.
        """
        self.ax.clear()
        if (file_path is None): return 
        _, total_number_words, data = file_path_to_stats(file_path)
        
        # Clear previous plot
        
        characters = [item[0] for item in data]
        occurrences = [item[1] for item in data]
        
        self.ax.bar(characters, occurrences)
        self.ax.set_xlabel('Characters')
        self.ax.set_ylabel('Occurrences')
        self.ax.set_title('Character Occurrences')
        
        # Adjust layout and redraw
        self.figure.tight_layout()
        self.canvas.draw()
        
        
    def clear(self):
        self.ax.clear()
        self.canvas.draw()
