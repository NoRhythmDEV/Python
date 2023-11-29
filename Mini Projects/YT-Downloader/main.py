import tkinter
import customtkinter
from pytube import YouTube

# System Settings
customtkinter.set_appearance_mode("System") #uses system settings (light/dark mode)
customtkinter.set_default_color_theme("blue")

#Functions

def hideErrorMessage():
    errorMessage.configure(text="")

def startDownload_highres():
    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink)
        video_highRes = ytObject.streams.get_highest_resolution()
        video_highRes.download() 
        finishLabel.configure(text="Download Complete")
    except:
        errorMessage.configure(text="Invalid Link")
        app.after(5000, hideErrorMessage)

def startDownload_audioOnly():
    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink)
        audioOnly = ytObject.streams.get_audio_only()
        audioOnly.download()
        finishLabel.configure(text="Download Complete")
    except:
        errorMessage.configure(text="Invalid Link")
        app.after(5000, hideErrorMessage)

# App Frame

app = customtkinter.CTk()
app.geometry("720x480")
app.title("YouTube Downloader")

# ------------------------------------------------- UI Elements -------------------------------------------------

# Title
title = customtkinter.CTkLabel(app, text="Video: ")
title.pack()

# Link Input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack()

# Button high_res
download_button_highRes = customtkinter.CTkButton(app, text="Download Mp4 (Highest Res)", command=startDownload_highres,width=200,height=40)
download_button_highRes.pack(padx=10,pady=10)

# Button audioOnly
download_button_audioOnly = customtkinter.CTkButton(app, text="Download Mp3", command=startDownload_audioOnly,width=200,height=40)
download_button_audioOnly.pack(padx=10, pady=10)

# Finished Downloading
finishLabel = customtkinter.CTkLabel(app,text="",text_color="green",font=("Helvatica",25))
finishLabel.pack()

# Error Message if link Invalid
errorMessage = customtkinter.CTkLabel(app, text="", text_color="red",font=("Helvatica",25))
errorMessage.pack()

























# Run App

app.mainloop()
