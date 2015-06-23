from lxml import html
import ast 
import requests
import urllib2

# name has to be a string
def url_gen(name):
	template = 'http://na.op.gg/summoner/ajax/mmr.json/userName='
	# escapes the space character and adds %20
	name = urllib.quote(name,'')
	URL = template + name
	return URL

# to test, use either "jo1345" or "NME Flaresz x"
def mmr_return(name):
	page = requests.get(url_gen(name))
	temp = ast.literal_eval(page.content)
	if 'error' in temp.keys():
		return None
	else:	
		mmr = temp['mmr'].replace(',','')
		return int(mmr)

	# 	2(name))
	# data = simplejson.load(json_obj)