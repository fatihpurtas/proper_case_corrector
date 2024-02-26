import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

def type_corrector(txt):
    txt = txt.lower()
    lines = txt.split('\n')
    for i in range(len(lines)):
        words = lines[i].split()
        for j in range(len(words)):
            words[j] = words[j][0].upper() + words[j][1:]
        lines[i] = ' '.join(words)
    return '\n'.join(lines)

def process_file():
    file_path = filedialog.askopenfilename()
    if not file_path:
        messagebox.showerror("Error", "No file selected.")
        return

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            txt = file.read()
    except FileNotFoundError:
        messagebox.showerror("Error", f"{file_path} file not found.")
        return

    output = type_corrector(txt)

    new_file_path = "edited_" + file_path
    with open(new_file_path, "w", encoding="utf-8") as file:
        file.write(output)

    messagebox.showinfo("Success", f"New text file created: {new_file_path}")

# Create main window
root = tk.Tk()
root.title("Text Type Corrector")

# Create a button for selecting file
select_button = tk.Button(root, text="Select File", command=process_file)
select_button.pack(pady=20)

root.mainloop()
