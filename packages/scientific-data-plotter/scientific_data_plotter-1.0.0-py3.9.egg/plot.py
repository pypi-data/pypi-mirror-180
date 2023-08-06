import sys
import tkinter as tk
from tkinter import filedialog
import pandas as pd
import matplotlib.pyplot as plt

# Use tkinter to open a file browser and select a file
root = tk.Tk()
root.withdraw()
filepath = filedialog.askopenfilename()

# Load the file using pandas
if filepath.endswith(".xlsx"):
    # Excel file
    df = pd.read_excel(filepath)
elif filepath.endswith(".csv"):
    # CSV file
    df = pd.read_csv(filepath)
elif filepath.endswith(".xy"):
    # .xy file
    df = pd.read_csv(filepath, sep=" ", names=["x", "y"])
else:
    # Unrecognized file type
    print("Error: Unrecognized file type")
    sys.exit(1)

# Check if the first row contains column headers
if df.iloc[0].dtype == object:
    # First row is a header row, skip it
    data = df.iloc[1:]
else:
    # First row is not a header row, use all rows
    data = df

# Plot all of the data
plt.plot(data["x"], data["y"])

# Prompt user to use a GUI to change x, y limits and axes titles
plt.xlim(xmin=0)
plt.ylim(ymin=0)
plt.xlabel("X data")
plt.ylabel("Y data")
plt.show()

# Save the plot to the same folder as the input file
plt.savefig(filepath.rsplit("/", 1)[0] + "/plot.png")

