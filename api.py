from lxml import html
import requests
import ast
import urllib 
import urllib2
import simplejson

api_key = "5812433f-6e68-4c43-973f-9a5d21d50503"

def url_gen1(name):
	name = urllib.quote(name,'')
	URL = "https://na.api.pvp.net/api/lol/na/v1.4/summoner/by-name/" + name +"?api_key=" + api_key
	return URL 

def summonerID(name):
	page = requests.get(url_gen1(name))
	temp = ast.literal_eval(page.content)
	name = name.replace(' ', '').lower()
	summonerID = temp[name]['id']
	return summonerID

def url_gen2(name):
	s_id = str(summonerID(name))
	URL = "https://na.api.pvp.net/api/lol/na/v2.2/matchhistory/" + s_id + "?rankedQueues=RANKED_SOLO_5x5&api_key=" + api_key
	return URL

def accountID(name):
	json_obj = urllib2.urlopen(url_gen2(name))
	data = simplejson.load(json_obj)
	URI = data['matches'][0]['participantIdentities'][0]['player']['matchHistoryUri']
	return URI