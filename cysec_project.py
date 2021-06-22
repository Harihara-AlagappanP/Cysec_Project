import requests
from datetime import datetime

api_key = '358f3cd51eae9bdadd90319f1df5c925'
loc = input("Enter the city name: ")

comp_api_link = "https://api.openweathermap.org/data/2.5/weather?q=" + loc + "&appid=" + api_key
api_link = requests.get(comp_api_link)
api_data = api_link.json()

temp_city = (api_data['main']['temp']) - 273.15
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time =  datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

print("-------------------------------------------------------------")
print("Weather stats for {}  || {}". format(loc.upper(),date_time))
print("-------------------------------------------------------------")

print("Current temperature is: {:.2f} deg C". format(temp_city))
print("Current weather desc  :",weather_desc)
print("Current Humidity      :",hmdt,'%')
print("Current wind speed    :",wind_spd,"kmph")

pjt_obj = open("cysec project.txt","w")
pjt_obj.write("-------------------------------------------------------------" + "\n")
pjt_obj.write("Weather stats for {}  || {}". format(loc.upper(),date_time) + "\n")
pjt_obj.write("-------------------------------------------------------------" + "\n")
pjt_obj.write("Current temperature is: {:.2f} deg C". format(temp_city) + "\n")
pjt_obj.write("Current weather desc  :")
pjt_obj.write(weather_desc + "\n")
pjt_obj.write("Current Humidity      :")
pjt_obj.write(str(hmdt) + "%" + "\n")
pjt_obj.write("Current wind speed    :")
pjt_obj.write(str(wind_spd) + "kmph")
pjt_obj.close()
