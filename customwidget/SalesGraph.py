import matplotlib.backends.backend_tkagg
from matplotlib import pyplot
from tkinter import Frame, TOP, BOTH
from customtkinter import CTkFrame
from utils import itemdata

class SalesGraph(Frame):
    def __init__(self, parent, days_limit=7, theme="light"):
        super().__init__(parent)
        self.days_limit = days_limit
        self.theme = theme
        self.create_widgets()

    def create_widgets(self):
        # Fetch sales data from the itemdata module
        sales_data = itemdata.get_sales_data()

        # Limit the sales data to the last `days_limit` days
        total_sales = [sale[0] for sale in sales_data[-self.days_limit:]]
        dates = [sale[1] for sale in sales_data[-self.days_limit:]]

        # Set the theme for the plot
        if self.theme == "light":
            pyplot.style.use("seaborn-whitegrid")
        elif self.theme == "dark":
            pyplot.style.use("seaborn-darkgrid")

        # Create a figure for the plot
        fig = pyplot.Figure(figsize=(4, 3), dpi=100)
        axis = fig.add_subplot(111)

        # Add a title and labels to the x and y axis
        axis.set_title("TOTAL SALES IN PAST WEEK", fontdict={'fontname': 'Arial', 'fontweight': 'bold', 'fontsize': 11})
        axis.set_xlabel("Date", fontdict={'fontname': 'Arial', 'fontweight': 'bold', 'fontsize': 10})
        axis.set_ylabel("Total Sales", fontdict={'fontname': 'Arial', 'fontweight': 'bold', 'fontsize': 10})


        # Plot the sales data
        axis.plot(dates, total_sales)
        axis.plot(dates, total_sales, 'o')

        # Set the size of the x and y tick labels
        for label in axis.get_xticklabels():
            label.set_fontsize(9)
        for label in axis.get_yticklabels():
            label.set_fontsize(9)

        # Adjust the bottom margin of the plot to ensure that the x-axis label is not cut off
        fig.subplots_adjust(bottom=0.15)

        # Add the plot to the Tkinter frame
        canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

    def refresh_plot(self):
        # Remove the old plot
        for widget in self.winfo_children():
            widget.destroy()

        # Re-create the plot
        self.create_widgets()
