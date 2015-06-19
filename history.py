import urllib2
import simplejson
import api
import numpy

def gameCount(name):
	URI = api.accountID(name)
	URL = "https://acs.leagueoflegends.com" + URI
	json_obj = urllib2.urlopen(URL)
	data = simplejson.load(json_obj)
	return data['games']['gameCount']

# have to fix this
# def url_gen3(name):
# 	URI = api.accountID(name)
# 	count = gameCount(name)
# 	temp = numpy.arange(0,count,20).tolist()
# 	URLS = []
# 	for i in range(0, len(temp)):
# 		if i != 0:
# 			start = temp[i] + 1
# 		else:
# 			start = temp[i]
# 		if i != len(temp) - 1:
# 			end = temp[i+1]
# 		else:
# 			end = count
# 		URLS.append("https://acs.leagueoflegends.com" + URI + "?begIndex=" + str(start) + "&endIndex=" + str(end))
# 	return URLS	