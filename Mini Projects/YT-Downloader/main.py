import tkinter
import customtkinter
from pytube import YouTube

# System Settings
customtkinter.set_appearance_mode("System") #uses system settings (light/dark mode)
customtkinter.set_default_color_theme("blue")

#Functions

def startDownload():
    try:
        ytLink = link.get
        ytObject = YouTube(ytLink)
        video_highRes = ytObject.streams.get_highest_resolution()
        video_highRes.download
    except:
        print("Youtube link is invalid")
    print("Download Complete")


# App Frame

app = customtkinter.CTk()
app.geometry("720x480")
app.title("YouTube Downloader")

# UI Elements

# Title
title = customtkinter.CTkLabel(app, text="Insert YouTube Link")
title.pack()

# Link Input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack()

#Button
download_button = customtkinter.CTkButton(app, text="Download!", command=startDownload)
download_button.pack(padx=10,pady=10)































# Run App

app.mainloop()
