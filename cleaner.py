# converts temp.txt into format for dictionary
import pickle

def cleaner():
	with open("temp.txt", "r") as f:
	   		content = f.read().splitlines()   		
	f.close()

	temp = []
	for item in content:
		temp.append(item.replace('\t', ' '))

	champions = {}
	for item in temp:
		champ_id = item.split()
		champions[champ_id[-1]] =  ' '.join(champ_id[:-1])

	# used pickle for convenience of storing dict
	pickle.dump(champions,open('champions.p','wb'))