import tkinter
import customtkinter
from pytube import YouTube
from PIL import Image, ImageTk, ImageFilter
from urllib.request import urlopen
import requests
import os
from tkinter import filedialog
from moviepy.editor import *


# Functions

def hideErrorMessage():
    errorMessage.configure(text="")

def hideSuccessMessage():
    successMessage.configure(text="")

def hideThumbail():
    thumbnailDisplay.configure(image=placeholder_image, width=400, height=225)

def hideTitle():
    titleDisplay.configure(text="")

# Test Video https://www.youtube.com/watch?v=PP7yRXdHAT0

def startDownloadVideo():
    global url
    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink, on_progress_callback=on_progress)

        # Ask the user to choose the download directory
        path_to_download = filedialog.askdirectory()
        path_to_download = path_to_download+"/Video"

        if not path_to_download:  # If the user cancels the file dialog
            return

        url = str(ytObject.thumbnail_url)
        response = requests.get(url, stream=True)
        image = Image.open(response.raw)
        image = image.resize((400, 225), Image.LANCZOS)  # Resize the image
        thumbnail_image = ImageTk.PhotoImage(image)

        titleDisplay.configure(text=f"Downloading: {ytObject.title}")
        thumbnailDisplay.configure(image=thumbnail_image, width=400, height=225)

        videofile = ytObject.streams.get_highest_resolution()
        videofile.download(path_to_download)

        successMessage.configure(text=f"Download Complete")

        # Remove Titles and Displays
        app.after(5000, hideSuccessMessage)
        app.after(5000, hideThumbail)
        app.after(5000, hideTitle)
    except Exception as e:
        print(e)
        errorMessage.configure(text="Invalid Link")
        app.after(5000, hideErrorMessage)

def startDownloadAudio():
    global url
    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink, on_progress_callback=on_progress)

        # Ask the user to choose the download directory
        path_to_download = filedialog.askdirectory()
        path_to_download = path_to_download+"/Audio"

        if not path_to_download:  # If the user cancels the file dialog
            return

        url = str(ytObject.thumbnail_url)
        response = requests.get(url, stream=True)
        image = Image.open(response.raw)
        image = image.resize((400, 225), Image.LANCZOS)  # Resize the image
        thumbnail_image = ImageTk.PhotoImage(image)

        titleDisplay.configure(text=f"Downloading: {ytObject.title}")
        thumbnailDisplay.configure(image=thumbnail_image, width=400, height=225)

        audiofile = ytObject.streams.get_audio_only()
        audiofile.download(path_to_download)

        successMessage.configure(text=f"Download Complete")

        convert_Audio_file = AudioFileClip(path_to_download + "/" + audiofile.default_filename)
        convert_Audio_file.write_audiofile(path_to_download+"/"+audiofile.default_filename[:-4]+".mp3")
        convert_Audio_file.close()
        os.remove(path_to_download+"/"+audiofile.default_filename[:-4]+".mp4")
                                                 
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
app.minsize(1280,720)
app.resizable(0, 0)

app.title("YouTube Downloader")

# ------------------------------------------------- UI Elements -------------------------------------------------
# Title
title = customtkinter.CTkLabel(app, text="Download any YouTube Video - Insert link Below")
title.grid(row=0, column=0, columnspan=4, pady=(30, 10), padx=10)

# Link Input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=550, height=40, textvariable=url_var)
link.grid(row=1, column=0, columnspan=4, padx=10, pady=10)

# Button Video
download_button_Video = customtkinter.CTkButton(app, text="Download Video", command=startDownloadVideo,width=200,height=40)
download_button_Video.grid(row=2, column=1, columnspan=1, pady=10)

# Button Audio
download_button_Audio = customtkinter.CTkButton(app, text="Download Audio", command=startDownloadAudio,width=200,height=40)
download_button_Audio.grid(row=2, column=2, columnspan=1, pady=10)

# Progress
pPercantage = customtkinter.CTkLabel(app, text="0%")
pPercantage.grid(row=3, column=0, columnspan=4, padx=5, pady=5)

pBar = customtkinter.CTkProgressBar(app, width=400)
pBar.set(0)
pBar.grid(row=4, column=0, columnspan=4, padx=5, pady=5)

# Title Display
titleDisplay = customtkinter.CTkLabel(app, text="", font=("Helvetica",18))
titleDisplay.grid(row=5, column=0, columnspan=4, padx=5, pady=5)

# Thumbnail Display
placeholder_image = ImageTk.PhotoImage(Image.new("RGB", (0, 0), "white"))
thumbnailDisplay = customtkinter.CTkLabel(app, text="", image=placeholder_image, width=400, height=225)
thumbnailDisplay.grid(row=6, column=0, columnspan=4, padx=5, pady=5)

# Finished Downloading
successMessage = customtkinter.CTkLabel(app,text="",text_color="green",font=("Helvetica",25))
successMessage.grid(row=7, column=0, columnspan=4, padx=5, pady=5)

# Error Message if link Invalid
errorMessage = customtkinter.CTkLabel(app, text="", text_color="red",font=("Helvetica",25))
errorMessage.grid(row=8, column=0, columnspan=4)

# Configure the grid
app.columnconfigure(0, weight=1)
app.columnconfigure(1, weight=1)
app.columnconfigure(2, weight=1)
app.columnconfigure(3, weight=1)
app.rowconfigure(0, weight=1)
app.rowconfigure(1, weight=1)
app.rowconfigure(2, weight=1)
app.rowconfigure(3, weight=1)
app.rowconfigure(4, weight=1)
app.rowconfigure(5, weight=1)
app.rowconfigure(6, weight=1)
app.rowconfigure(7, weight=1)
app.rowconfigure(8, weight=1)

# Run App
app.mainloop()