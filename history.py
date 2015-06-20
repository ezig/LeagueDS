import urllib2
import simplejson
import api
import numpy

def data_gen(url):
	json_obj = urllib2.urlopen(url)
	data = simplejson.load(json_obj)
	return data

def gamecount(name):
	URI = api.accountID(name)
	URL = "https://acs.leagueoflegends.com" + URI
	data = data_gen(URL)
	return data['games']['gameCount']


def url_gen3(name):
	URI = api.accountID(name)
	count = gamecount(name)
	temp = numpy.arange(0,count,20).tolist()
	URLS = []
	for i in range(0, len(temp)):
		if i != 0:
			start = temp[i]
		else:
			start = temp[i]
		if i != len(temp) - 1:
			end = temp[i+1]
		else:
			end = count
		URLS.append("https://acs.leagueoflegends.com" + URI + "?begIndex=" + str(start) + "&endIndex=" + str(end))
	return URLS	

def gameids(name):
	urls = url_gen3(name)
	ids = []
	for i in range(0,len(urls)):
		data = data_gen(urls[i])
		for item in data['games']['games']:
			ids.append(item['gameId'])
	return ids

def winloss(name):
	urls = url_gen3(name)
	win_loss = {}
	for i in range(0,len(urls)):
		data = data_gen(urls[i])
		for item in data['games']['games']:
			win_loss[item['gameId']] = item['participants'][0]['stats']['win']
	return win_loss

def kda_per_game(name):
	urls = url_gen3(name)
	KDA = {}
	for i in range(0,len(urls)):
		data = data_gen(urls[i])
		for item in data['games']['games']:
			game_kda = {}
			game_kda['assists'] = item['participants'][0]['stats']['assists']
			game_kda['deaths'] = item['participants'][0]['stats']['deaths']
			game_kda['kills'] = item['participants'][0]['stats']['kills']
			if game_kda['deaths'] != 0:
				game_kda['kda'] = round(float(game_kda['kills'] + game_kda['assists'])/float(game_kda['deaths']),2)
			else:
				# need to tweek this
				game_kda['kda']	= round(float(game_kda['kills'] + game_kda['assists']),2)
			KDA[item['gameId']] = game_kda
	return KDA	


def overall_kda(name):
	urls = url_gen3(name)
	KDA = {'kills': 0, 'assists': 0, 'deaths': 0}
	for i in range(0,len(urls)):
		data = data_gen(urls[i])
		for item in data['games']['games']:
			KDA['kills'] = KDA['kills'] + item['participants'][0]['stats']['kills']
			KDA['deaths'] = KDA['deaths'] + item['participants'][0]['stats']['deaths']
			KDA['assists'] = KDA['assists'] + item['participants'][0]['stats']['assists']
	return KDA, round((float(KDA['kills']) + float(KDA['assists']))/float(KDA['deaths']),2)










