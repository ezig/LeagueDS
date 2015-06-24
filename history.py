import requests

import api

def gamecount(name):
	URI = api.accountID(name)
	URL = "https://acs.leagueoflegends.com" + URI
	data = data_gen(URL)
	return data['games']['gameCount']

matches_per_url = 20
# queue = 04 is soloqueue, queue = 42 is team
def url_gen(name):
	uri = api.accountID(name)
	count = gamecount(name)

	urls = []
	# count up from 0 to count by matches_per_url
	for start in range(0, count, matches_per_url):
		# make sure not to go over the max number of counts
		end = min(start + matches_per_url, count)

		# if count % matches_per_url = 0, we could have the case where
		# start = end, which would not get any games that the previous 
		# url didn't already cover
		if start != end:
			urls.append("https://acs.leagueoflegends.com" + uri + "?begIndex=" + str(start) + "&endIndex=" + str(end) +"&queue=04")

	return urls	

def data_gen(url):
	return requests.get(url).json()