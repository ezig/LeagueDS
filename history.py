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