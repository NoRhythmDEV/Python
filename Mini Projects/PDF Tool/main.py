import tkinter as tk
from tkinter import messagebox, filedialog
import ttkbootstrap as tkb
import os
from PyPDF2 import *

# Functions

def merge_pdf():
    input_path = filedialog.askdirectory()
    if not input_path:
        return

    pdf_files = [file for file in os.listdir(input_path) if file.endswith(".pdf")]

    if not pdf_files:
        messagebox.showerror("ERROR", f"No .pdf files found in: {input_path}")
        return

    output_path = os.path.join(input_path, "output")
    os.makedirs(output_path, exist_ok=True)
    files_to_remove = []

    merger = PdfMerger()

    for file in pdf_files:
        file_path = os.path.join(input_path, file)
        print(file_path)
        merger.append(file_path)
        files_to_remove.append(file_path)

    output_file_path = os.path.join(output_path, "merged.pdf")
    messagebox.showinfo("Success", f"Done! Files output: {output_path}")
    merger.write(output_file_path)
    merger.close()

    for i in files_to_remove:
        os.remove(i)
        
# Main Window

app = tkb.Window(themename="darkly")
app.geometry("1280x720")
app.minsize(1280, 720)
app.resizable(0, 0)
app.title("PDF Tools")
app.place_window_center()

button1 = tkb.Button(app, text="Merge PDF", command=merge_pdf, width=50)
button1.grid(row=0, column=0, columnspan=1, pady=15, padx=15)

app.columnconfigure(1, weight=1)
app.rowconfigure(1)



# Start Window
app.mainloop()