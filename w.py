import requests
import emoji

api_address='http://api.openweathermap.org/data/2.5/weather?appid=c203e4316c17db1c1944eef0e8ebb2f2&q='
city = input('City Name :')
url = api_address + city
json_data = requests.get(url).json()
format_add = json_data['main']['temp']
a = int(format_add)-273.15
print(a)
f =json_data['weather'][0]['main']
if f == "Clear":
	print(emoji.emojize(":sun:"))
if f == "Haze":
	print(emoji.emojize(":cloud:"))
if f == "Rain":
	print(emoji.emojize(":umbrella:"))
if f == "Clouds":
	print(emoji.emojize(":cloud:"))
if f == "Snow":
	print(emoji.emojize(":snowflake:"))
if f == "Thunder":
	print(emoji.emojize(":zap:"))

