import sys
import tkinter as tk
from tkinter import filedialog
import os

def type_corrector(txt):
    txt = txt.lower()
    lines = txt.split('\n')
    for i in range(len(lines)):
        words = lines[i].split()
        for j in range(len(words)):
            words[j] = words[j][0].upper() + words[j][1:]
        lines[i] = ' '.join(words)
    return '\n'.join(lines)

def select_file():
    file_name = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file_name:
        file_entry.delete(0, tk.END)
        file_entry.insert(0, file_name)

def save_file(output):
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(output)
        result_label.config(text=f"New text file created: {file_path}")

def process_file():
    file_name = file_entry.get()
    if not file_name:
        result_label.config(text="No file selected.")
        return

    try:
        with open(file_name, "r", encoding="utf-8") as file:
            txt = file.read()
    except FileNotFoundError:
        result_label.config(text=f"{file_name} file not found..")
        return

    output = type_corrector(txt)

    save_file(output)

# Create GUI
root = tk.Tk()
root.title("Proper Case Corrector")

file_label = tk.Label(root, text="Select TXT file:")
file_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")

file_entry = tk.Entry(root, width=50)
file_entry.grid(row=0, column=1, padx=5, pady=5)

select_button = tk.Button(root, text="Select", command=select_file)
select_button.grid(row=0, column=2, padx=5, pady=5)

process_button = tk.Button(root, text="Process", command=process_file)
process_button.grid(row=1, column=1, padx=5, pady=5)

result_label = tk.Label(root, text="")
result_label.grid(row=2, column=1, padx=5, pady=5)

root.mainloop()
