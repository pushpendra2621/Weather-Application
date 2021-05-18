from django.shortcuts import render, redirect
import requests
import json

# Create your views here.

def index(request):
	if request.method=="POST":
		station = request.POST['station']
		url = 'http://api.weatherapi.com/v1/current.json?key=9370fe6bd5f942a3a6c93909212504&q=' +station+'&aqi=no'
		response = requests.get(url)
		json_response = response.json()
		context ={
			'country':json_response['location']['country'],
			'temp':json_response['current']['temp_c'],
			'weather_text': json_response['current']['condition']['text'],
			'img':json_response['current']['condition']['icon'],
			'latitude':json_response['location']['lat'],
			'longitude':json_response['location']['lon'],
			'humidity':json_response['current']['humidity'],
		}
	else:
		context={}
	return render(request, 'form.html', context)