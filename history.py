import urllib2
import simplejson
import api
import numpy

def gamecount(name):
	URI = api.accountID(name)
	URL = "https://acs.leagueoflegends.com" + URI
	data = data_gen(URL)
	return data['games']['gameCount']

# queue = 04 is soloqueue, queue = 42 is team
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
		URLS.append("https://acs.leagueoflegends.com" + URI + "?begIndex=" + str(start) + "&endIndex=" + str(end) +"&queue=04")
	return URLS	

def data_gen(url):
	json_obj = urllib2.urlopen(url)
	data = simplejson.load(json_obj)
	return data