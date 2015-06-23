# converts temp.txt into format for dictionary
import pickle

def cleaner():
	with open("temp.txt", "r") as f:
	   		content = f.read().splitlines()

	# split each item into [champion, ID]
	content = map(lambda s: s.split('\t'), content)

	# create dictionary of champion ID's to names
	champions = {champ[1] : champ[0] for champ in content}

	# used pickle for convenience of storing dict
	pickle.dump(champions,open('champions.p','wb'))