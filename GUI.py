import tkinter as tk
from tkinter import scrolledtext

# Initialize Tkinter window
root = tk.Tk()
root.title("Scanned Boxes")

# Add a scrolled text widget to display boxes
text_area = scrolledtext.ScrolledText(root, width=40, height=20, font=("Arial", 10))
text_area.pack(padx=10, pady=10)

# Function to update the text widget with boxes info
def update_boxes_display(boxes):
    text_area.delete('1.0', tk.END)
    for i, scanned_box in enumerate(boxes[-10:]):  # last 10 scanned boxes
        comp_names = ", ".join([comp.name for comp in scanned_box.components])
        text_area.insert(tk.END, f"Box {i+1}: {comp_names}\n")

# This function will be called periodically from the main loop to keep GUI responsive
def gui_loop():
    root.update()