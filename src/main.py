import os
import pickle
import gtk
from weather_widget import WeatherPad

config_dir = os.path.expanduser(r"~/.config/deepin-weather/")
if(not os.path.exists(config_dir)):
    os.makedirs(config_dir)
    open(config_dir + "weather_info_file", "w").close

weather_info_file = open(config_dir + r"weather_info_file")
weather_info = {}
if(not weather_info_file.read()):
    weather_info["text"] = "Unknown"
    weather_info["pic"] = "smile"
    weather_info["temp"] = "5"
    weather_info["location"] = "Location."
else:    
    weather_info = pickle.load(weather_info_file)
# weather_info["from"] = "from_file"

WeatherPad(weather_info)
gtk.main()