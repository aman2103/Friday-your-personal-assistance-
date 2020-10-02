import os
import sys
import datetime
import pyttsx3
import speech_recognition as sr 
import wikipedia
import wolframalpha
import webbrowser
import smtplib
import random
import time
import json
import requests
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
		
from googlesearch import search
engine = pyttsx3.init('sapi5')
client = wolframalpha.Client("api")
voices = engine.getProperty("voices")
engine.setProperty("voice",voices[len(voices)-1].id)
def talk(audio):
	print('Friday:'+audio)
	engine.say(audio)
	engine.runAndWait()

def wishme():
	currentHour=int(datetime.datetime.now().hour)
	if currentHour>=0 and currentHour<12:
		talk('Good Morning!!')
	elif currentHour>=12 and currentHour<18:
		talk("Good Afternoon!!!")
	else :
		talk('Good Evening!!')

wishme()
talk("Hello Buddy, it's your  personal assistant Friday")
talk("i can answer to computational and geographical questions too...try Command ask")


def GiveCommand():
	a=sr.Recognizer()
	with sr.Microphone() as source:
		print("Listening......")
		#a.pause_threshold=1
		a.adjust_for_ambient_noise(source, duration=1)
		audio = a.listen(source)
	try:
		Input=a.recognize_google(audio,language='en-in')
		print('Aman :'+Input+"\n")

	except:
		talk("Sorry ! I didn't get that ! try typing it here...")
		Input=str(input("Command:"))

	return Input

if  __name__ =="__main__":
	while  True:
			talk("How can i help you????")
			Input = GiveCommand().lower()
			if "good bye" in Input or "ok bye" in Input or "stop" in Input or "bye" in Input: 
				talk("Have a great day....")
				print("Have a great day....")
				talk("your personal assistant Friday  is shutting down,Good bye")
				sys.exit()
			elif "open youtube" in Input:
				webbrowser.open_new_tab("https://www.youtube.com")
				talk("opening youtube now, happy to help you buddy")
			elif "open google" in Input:
				webbrowser.open_new_tab("https://www.google.com")
				talk("opening google now, happy to help you buddy")
			elif "what's up" in Input or "how are you" in Input:
				setreply=["just doing some stuff!","I am good.." ,"I am feeling awesome..","I am here to help you", "you are pretty amazing"]
				talk(random.choice(setreply))
			elif "open gmail" in Input or "gmail" in Input:
				webbrowser.open_new_tab("https://www.gmail.com")
				talk("opening gmail now, happy to help you buddy")

			elif "email" in Input:
				talk("who is the recipient?")
				recipient = GiveCommand()
				if "send" in recipient:
					try:
						talk("what should i say??")
						content=GiveCommand()
						server=smtplib.SMTP('smtp.gmail.com',587)
						server.ehlo()
						server.strattls()
						server.login("your username"," your password")
						server.sendmail("your username","Recipient username",content)
						server.close()
						talk("email sent!!")
					except:
						talk("sorry!! I am unable to send your message at this moment!!")

			elif "about" in Input or "what" in Input or "where" in Input or "who" in Input or "when" in Input:
				talk("Searcing please wait....")
				try:
					try:
						res=clint.Input(Input)
						output=next(res.output).text
						talk("Gotcha")
						talk(output)
						talk("you are looking for this")
					except:
						output=wikipedia.summary(Input,sentences=5)
						talk("Gotcha")
						talk("wikipedia says")
						talk(output)
						talk("are you looking for this..")
						talk("hope you like my service")
						if "yes" in Input:
							talk("i m glad you like it..next time i will try my better")
						elif "no" in Input:
							talk("i am really sorry.......  i will try better next time")
				except:
					talk("Searcing on google for" + Input)
					say=Input.replace(" ","+")
					webbrowser.open("https://www.google.co.in/search?q="+Input)

			elif "news" in Input:
				talk("here are someheadline from timesofindia")
				webbrowser.open_new_tab("https://timesofindia.com/home/headlines")
				talk(" are you looking for this")
			elif "ask" in Input:
				talk("what question do you wanna ask")
				while True:
					talk("ask now")
					question=GiveCommand()
					if "no" in question:
						talk("hope you like my service..")
						break
					res=client.query(question)
					answer=next(res.results).text
					talk(answer)
					talk("anything else you wanna ask??")
			elif "play music" in Input or "play song" in Input or "music" in Input:
				try:
					talk("which song you wanna listen??")
					song=GiveCommand()
					driver = webdriver.Chrome(r"C:/Users/asus/Downloads/chromedriver_win32/chromedriver.exe")	
					driver.get("https://wynk.in/music/detailsearch/"+song+"?q=")
					#search_bar=driver.find_element_by_xpath("/html/body/app-root/app-home/app-top-nav/nav/div/div[2]/div[1]/input")				#search_bar=search_bar.send_keys(Keys.ENTER)
					driver.find_elements_by_class_name("railContent")[0].click()
					time.sleep(3)
					driver.find_element_by_xpath("/html/body/app-root/app-home/div[2]/div/song-info/div/div[1]/div[3]/div[2]/div[1]/button[1]").click()
				except:
					talk("sorry,unable to find this song....")
					pass			
			
			elif "weather" in Input:
				api_key="api"
				base_url="https://api.openweathermap.org/data/2.5/weather?"
				talk("what is the city name")
				city=GiveCommand()
				url=base_url+"appid="+api_key+"&q="+city
				response=requests.get(url)
				x=response.json()
				if["cod"]!="404":
					y=x["main"]
					current_temp=y["temp"]
					current_humidity=y["humidity"]
					z=x["weather"]
					weather_desc=z[0]["description"]
					talk("Temperature in kelvin unit is"+
						str(current_temp)+
						"\n Humidity in "+
						str(current_humidity)+" % "+
						"\n description is "+
						str(weather_desc))
			else:
				talk("Searcing on google for" + Input)
				say=Input.replace(" ","+")
				webbrowser.open("https://www.google.co.in/search?q="+Input)

		
