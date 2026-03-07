# Program Name: Assignment3.py
# Course: IT3883/Section W01
# Student Name: Richard Rodriguez Martinez
# Assignment Number: Assignment 3
# Due Date: 3/6/2026
# Purpose: This program converts Miles per Gallon (MPG) to Kilometers per Liter (km/L)
# using a graphical user interface. The result updates automatically as the user types.
# Resources Used: Python documentation, Tkinter documentation, instructor materials.

import tkinter as tk

# Conversion constant
MPG_TO_KML = 0.425143707

# Function to update the conversion
def convert(event=None):
    try:
        mpg = float(mpg_entry.get())  # Get user input
        kml = mpg * MPG_TO_KML        # Convert to km/l
        result_var.set(f"{kml:.3f}")  # Display result
    except:
        # If user types letters or leaves blank, show nothing
        result_var.set("")

# Create main window
window = tk.Tk()
window.title("MPG to KM/L Converter")
window.geometry("300x150")

# MPG label and entry
mpg_label = tk.Label(window, text="Miles per Gallon (MPG):")
mpg_label.pack()

mpg_entry = tk.Entry(window)
mpg_entry.pack()
mpg_entry.bind("<KeyRelease>", convert)  # Update when user types

# Result label
result_label = tk.Label(window, text="Kilometers per Liter (km/L):")
result_label.pack()

# Variable to store result
result_var = tk.StringVar()

# Result display
result_display = tk.Label(window, textvariable=result_var, font=("Arial", 14))
result_display.pack()

# Run the program
window.mainloop()