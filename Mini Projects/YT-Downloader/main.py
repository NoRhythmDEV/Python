import tkinter
import customtkinter
from pytube import YouTube
from PIL import Image, ImageTk, ImageFilter
from urllib.request import urlopen
import requests

# Functions

def hideErrorMessage():
    errorMessage.configure(text="")

def hideSuccessMessage():
    successMessage.configure(text="")

def hideThumbail():
    thumbnailDisplay.configure(image=placeholder_image, width=400, height=225)

def hideTitle():
    titleDisplay.configure(text="")

def startDownload():
    global url
    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink, on_progress_callback=on_progress)

        url = str(ytObject.thumbnail_url)
        response = requests.get(url, stream=True)
        image = Image.open(response.raw)
        image = image.resize((400, 225), Image.LANCZOS)  # Resize the image
        thumbnail_image = ImageTk.PhotoImage(image)

        titleDisplay.configure(text=f"Downloading: {ytObject.title}")
        thumbnailDisplay.configure(image=thumbnail_image, width=400, height=225)

        video_highRes = ytObject.streams.get_highest_resolution()
        video_highRes.download()

        successMessage.configure(text="Download Complete")

        # Remove Titles and Displays
        app.after(5000, hideSuccessMessage)
        app.after(5000, hideThumbail)
        app.after(5000, hideTitle)
    except Exception as e:
        print(e)
        errorMessage.configure(text="Invalid Link")
        app.after(5000, hideErrorMessage)

def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = (bytes_downloaded / total_size) * 100
    per = str(int(percentage_of_completion))
    pPercantage.configure(text=f"{per}%")
    pPercantage.update()

    #update pBar
    pBar.set(float(percentage_of_completion)/100)

# System Settings
customtkinter.set_appearance_mode("System") #uses system settings (light/dark mode)
customtkinter.set_default_color_theme("blue")

# App Frame
app = customtkinter.CTk()
app.geometry("1280x720")
app.title("YouTube Downloader")

# ------------------------------------------------- UI Elements -------------------------------------------------

# Link Input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack()

# Button high_res
download_button_highRes = customtkinter.CTkButton(app, text="Download Video", command=startDownload,width=200,height=40)
download_button_highRes.pack(padx=10,pady=10)

# Progress
pPercantage = customtkinter.CTkLabel(app, text="0%")
pPercantage.pack()

pBar = customtkinter.CTkProgressBar(app, width=400)
pBar.set(0)
pBar.pack()

# Title Display
titleDisplay = customtkinter.CTkLabel(app, text="", font=("Helvetica",18))
titleDisplay.pack()

# Thumbnail Display
placeholder_image = ImageTk.PhotoImage(Image.new("RGB", (0, 0), "white"))
thumbnailDisplay = customtkinter.CTkLabel(app, text="", image=placeholder_image, width=400, height=225)
thumbnailDisplay.pack()

# Finished Downloading
successMessage = customtkinter.CTkLabel(app,text="",text_color="green",font=("Helvetica",25))
successMessage.pack()

# Error Message if link Invalid
errorMessage = customtkinter.CTkLabel(app, text="", text_color="red",font=("Helvetica",25))
errorMessage.pack()

# Run App
app.mainloop()