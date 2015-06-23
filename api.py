import requests
import urllib2

api_key = "5812433f-6e68-4c43-973f-9a5d21d50503"

def summonerID(name):
	# set up the URL
	name = urllib2.quote(name,'')
	url = "https://na.api.pvp.net/api/lol/na/v1.4/summoner/by-name/" + name +"?api_key=" + api_key

	response = requests.get(url).json()
	name = name.replace(' ', '').lower()

	# return the summoner ID
	return response[name]['id']

def accountID(name):
	s_id = str(summonerID(name))
	url = "https://na.api.pvp.net/api/lol/na/v2.2/matchhistory/" + s_id + "?rankedQueues=RANKED_SOLO_5x5&api_key=" + api_key

	response = requests.get(url).json()

	# return the URI
	return str(response['matches'][0]['participantIdentities'][0]['player']['matchHistoryUri'])