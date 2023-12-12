import tkinter as tk
from tkinter import *
from tkinter import messagebox
import ttkbootstrap as tkb
from ttkbootstrap.constants import *
import requests
from PIL import Image, ImageTk
import os

# Functions
def get_weather(city):
    API_key = "63a94bc3b86f53b49ce38778a3b579a2"
    URL = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_key}" #BSP https://api.openweathermap.org/data/2.5/weather?q=Markdorf&appid=63a94bc3b86f53b49ce38778a3b579a2
    result = requests.get(URL)

    if result.status_code == 404:
        messagebox.showerror("Error", "City not found")
        return None
    

    weather = result.json()
    icon_id = weather["weather"][0]["icon"]
    city = weather["name"]
    country = weather["sys"]["country"]
    temp = weather["main"]["temp"] - 273.15
    feels_like_temp = weather["main"]["feels_like"] - 273.15
    temp_min = weather["main"]["temp_min"] - 273.15
    temp_max = weather["main"]["temp_max"] - 273.15

    current_pressure = weather["main"]["pressure"] #pressure in millibar
    humidity = weather["main"]["humidity"] #% humidity

    wind_speed = weather["wind"]["speed"]
    wind_direction = weather["wind"]["deg"]

    longitude = weather["coord"]["lon"]
    latitude = weather["coord"]["lat"]


    icon_url = f"http://openweathermap.org/img/wn/{icon_id}@2x.png"
    return (icon_url, temp, city, country, feels_like_temp, temp_min, temp_max, current_pressure, humidity, wind_speed, wind_direction, longitude, latitude)

def search():
    city = searchbar.get()
    result = get_weather(city)
    if result is None:
        return

    icon_url, temp, city, country, feels_like_temp, temp_min, temp_max, current_pressure, humidity, wind_speed, wind_direction, longitude, latitude = result
    location_label.config(text=f"{city}, {country}")

    image = Image.open(requests.get(icon_url, stream=True).raw)
    icon = ImageTk.PhotoImage(image)
    icon_label.config(image=icon)
    icon_label.image = icon
    temp_label.config(text=f"Temperature: {temp:.2f} °C")
    temp_feel_label.config(text=f"Feels like: {feels_like_temp:.2f} °C")
    temp_min_label.config(text=f"Min. Temperature: {temp_min:.2f} °C")
    temp_max_label.config(text=f"Max. Temperature: {temp_max:.2f} °C")
    pressure_label.config(text=f"Current Pressure: {current_pressure} millibar")
    humidity_label.config(text=f"Humidity: {humidity}%")
    wind_speed_label.config(text=f"Wind Speed: {wind_speed}m/s")

    wind_direction = int(wind_direction)
    if wind_direction in range(0, 22) or wind_direction in range(338, 360):
        wind_direction_label.config(text=f"Wind Direction: North ({wind_direction})")
    elif wind_direction in range(22, 67):
        wind_direction_label.config(text=f"Wind Direction: North-Northeast ({wind_direction})")
    elif wind_direction in range(67, 112):
        wind_direction_label.config(text=f"Wind Direction: Northeast ({wind_direction})")
    elif wind_direction in range(112, 157):
        wind_direction_label.config(text=f"Wind Direction: East-Northeast ({wind_direction})")
    elif wind_direction in range(157, 202):
        wind_direction_label.config(text=f"Wind Direction: East ({wind_direction})")
    elif wind_direction in range(202, 247):
        wind_direction_label.config(text=f"Wind Direction: East-Southeast ({wind_direction})")
    elif wind_direction in range(247, 292):
        wind_direction_label.config(text=f"Wind Direction: Southeast ({wind_direction})")
    elif wind_direction in range(292, 337):
        wind_direction_label.config(text=f"Wind Direction: South-Southeast ({wind_direction})")
    else:
        wind_direction_label.config(text=f"Wind Direction: Unknown ({wind_direction})")

    lon_label.config(text=f"Longitude: {longitude}")
    lat_label.config(text=f"Latitude: {latitude}")


def clear():
    placeholder_image = ImageTk.PhotoImage(Image.new("RGBA", (1, 1), (0, 0, 0, 0)))

    location_label.config(text="")
    icon_label.config(text="")
    icon_label.config(image=placeholder_image)
    icon_label.image = placeholder_image
    temp_label.config(text="")
    temp_feel_label.config(text="")
    temp_min_label.config(text="")
    temp_max_label.config(text="")
    pressure_label.config(text="")
    humidity_label.config(text="")
    wind_speed_label.config(text="")
    lon_label.config(text="")
    lat_label.config(text="")
    wind_direction_label.config(text="")


# Frame
app = tkb.Window(themename="darkly")
app.geometry("1280x720")
app.minsize(1280, 720)
app.resizable(0, 0)
app.title("Wetterapp v0.1")
app.place_window_center()

script_dir = os.path.dirname(os.path.abspath(__file__))
icon_path = os.path.join(script_dir, "icon.ico")
icon_image = Image.open(icon_path)
photo_image = ImageTk.PhotoImage(icon_image)
app.wm_iconphoto(True, photo_image)

# components
search_label = tkb.Label(app, text="Enter your City",font=("Helvetica",12))
search_label.grid(row=0,column=0,columnspan=1,pady=(15,150),padx=(50,0))

searchbar = tkb.Entry(app, width=65, style="light", justify="center")
searchbar.grid(row=0, column=1, columnspan=1, pady=(15,150), padx=20)

search_button = tkb.Button(app, text="Search", command=search, style="light",width=25)
search_button.grid(row=0, column=2, columnspan=1, pady=(15, 150), padx=(20, 10), sticky="e")

clear_button = tkb.Button(app, text="clear", command=clear, style="light", width=25)
clear_button.grid(row=0, column=3, columnspan=1, pady=(15, 150), padx=(10, 20), sticky="w")

location_label = tkb.Label(app, text="" ,font=("Helvetica",12))
location_label.grid(row=1,column=0,columnspan=2,pady=(5,0))

icon_label = tkb.Label(app, text="" ,font=("Helvetica",12))
icon_label.grid(row=2,column=0,columnspan=2,pady=(5,0))

temp_label = tkb.Label(app, text="" ,font=("Helvetica",12))
temp_label.grid(row=3,column=0,columnspan=2,pady=(5,0))

temp_feel_label = tkb.Label(app, text="" ,font=("Helvetica",12))
temp_feel_label.grid(row=4,column=0,columnspan=2,pady=(5,0))

temp_min_label = tkb.Label(app, text="" ,font=("Helvetica",12))
temp_min_label.grid(row=5,column=0,columnspan=2,pady=(5,0))

temp_max_label = tkb.Label(app, text="" ,font=("Helvetica",12))
temp_max_label.grid(row=6,column=0,columnspan=2,pady=(5,0))

pressure_label = tkb.Label(app, text="" ,font=("Helvetica",12))
pressure_label.grid(row=1,column=2,columnspan=2,pady=(5,0))

humidity_label = tkb.Label(app, text="" ,font=("Helvetica",12))
humidity_label.grid(row=2,column=2,columnspan=2,pady=(5,0))

wind_speed_label = tkb.Label(app, text="" ,font=("Helvetica",12))
wind_speed_label.grid(row=3,column=2,columnspan=2,pady=(5,0))

wind_direction_label = tkb.Label(app, text="" ,font=("Helvetica",12))
wind_direction_label.grid(row=4,column=2,columnspan=2,pady=(5,0))

lon_label = tkb.Label(app, text="" ,font=("Helvetica",12))
lon_label.grid(row=5,column=2,columnspan=2,pady=(5,0))

lat_label = tkb.Label(app, text="" ,font=("Helvetica",12))
lat_label.grid(row=6,column=2,columnspan=2,pady=(5,0))


# grid config
app.columnconfigure(0)
app.columnconfigure(1)
app.columnconfigure(2)
app.columnconfigure(3)
app.rowconfigure(0)
app.rowconfigure(1)
app.rowconfigure(2)
app.rowconfigure(3)
app.rowconfigure(4)
app.rowconfigure(5)
app.rowconfigure(6)


app.mainloop()
