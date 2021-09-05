import json
import requests

r= requests.get('http://api.weatherapi.com/v1/current.json?key=070da05176b74140a98104030210509&q=Hyderabad&aqi=no')

print((r.json()))