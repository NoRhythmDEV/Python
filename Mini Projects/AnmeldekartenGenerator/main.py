import tkinter as tk
import ttkbootstrap as tkb
from barcode import Code128
from barcode.writer import ImageWriter
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os
from ttkbootstrap.toast import ToastNotification
from tkinter import messagebox
import string

# Functions
def find_illegal_chars(text):
    chars = set(string.ascii_letters + string.digits + string.punctuation)
    illegal_chars = set(char for char in text if char not in chars)
    return illegal_chars if illegal_chars else None

def barcodegen_code_128():
    username = entry_username.get()
    password = entry_password.get()

    illegal_chars_username = find_illegal_chars(username)
    if illegal_chars_username:
        illegal_chars_str = ', '.join(f"'{char}'" for char in illegal_chars_username)
        messagebox.showerror("ERROR", f"Folgende zeichen: {illegal_chars_str} können nicht in einem Code-128 Barcode enthalten sein!\n\nEntferne diese bitte aus dem Nutzernamen!\nDu kannst ö z.B. mit oe ersätzen.")
        return

    illegal_chars_password = find_illegal_chars(password)
    if illegal_chars_password:
        illegal_chars_str = ', '.join(f"'{char}'" for char in illegal_chars_password)
        messagebox.showerror("ERROR", f"Folgende zeichen: {illegal_chars_str} können nicht in einem Code-128 Barcode enthalten sein!\n\nEntferne diese bitte aus dem Passwort!\nDu kannst ö z.B. mit oe ersätzen.")
        return

    # Generate Code 128 barcode for username
    code_username = Code128(username, writer=ImageWriter())
    code_username.save("username", options={"write_text":False})

    # Generate Code 128 barcode for password (without text)
    code_password = Code128(password, writer=ImageWriter())
    code_password.save("password", options={"write_text":False})

    # Create a PDF file and embed the barcode images
    pdf_filename = f"Anmeldekarte {username}.pdf"
    c = canvas.Canvas(pdf_filename, pagesize=letter)

    barcode_width = 200
    barcode_height = 50

    c.setFont("Helvetica", 12)
    c.drawString(20, 750, f"{username}")
    c.drawString(20, 700, f"Name")
    c.drawInlineImage('username.png', 0, 640, width=barcode_width, height=barcode_height)
    c.drawString(20, 600, f"Passwort")
    c.drawInlineImage('password.png', 0, 540, width=barcode_width, height=barcode_height)
    
    os.remove("password.png")
    os.remove("username.png")

    c.save()
    toast_done.show_toast()

# App Window
app = tkb.Window(themename="darkly")
app.title("Anmeldekarten Generator | v1.5")
app.geometry("400x500")
app.resizable(0, 0)
app.position_center()

username_label = tkb.Label(app, text="Nutzername", font=("Arial", 14))
username_label.grid(row=0, column=1, columnspan=1, pady=(85, 7))

username_var = tk.StringVar()
entry_username = tkb.Entry(app, width=40, justify="center", textvariable=username_var)
entry_username.grid(row=1, column=1, columnspan=1, pady=7)

password_label = tkb.Label(app, text="Passwort", font=("Arial", 14))
password_label.grid(row=2, column=1, columnspan=1, pady=7)

password_var = tk.StringVar()
entry_password = tkb.Entry(app, width=40,justify="center", textvariable=password_var)
entry_password.grid(row=3, column=1, columnspan=1, pady=7)

gen_button = tkb.Button(app, text="PDF generieren", width=40, command=barcodegen_code_128, style="primary.TButton")
gen_button.grid(row=4, column=1, columnspan=1, pady=(65,0))

# Toast Notification
toast_done = ToastNotification(
    title=f"Succesfully created File",
    message=f"The PDF is saved in the same folder as the Programm",
    duration=3000,
    bootstyle="darkly"
)

app.rowconfigure(0)
app.rowconfigure(1)
app.rowconfigure(2)
app.rowconfigure(3)
app.rowconfigure(4)
app.columnconfigure(1, weight=1)


app.mainloop()


