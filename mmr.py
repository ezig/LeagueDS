import requests
import urllib2

# name has to be a string
def url_gen(name):
	template = 'http://na.op.gg/summoner/ajax/mmr.json/userName='
	# escapes the space character and adds %20
	name = urllib2.quote(name,'')
	URL = template + name
	return URL

# to test, use either "jo1345" or "NME Flaresz x"
def mmr_return(name):
	response = requests.get(url_gen(name)).json()
	if 'error' in response:
		return None
	else:	
		mmr = response['mmr'].replace(',','')
		return int(mmr)

print mmr_return("Valos4")