import history
# TODO: kills, damage to champs, damage taken?, crowd control dealt, vision, firsts

def gameids(name):
	urls = history.url_gen3(name)
	ids = []
	for i in range(0,len(urls)):
		data = history.data_gen(urls[i])
		for item in data['games']['games']:
			ids.append(item['gameId'])
	return ids

def duration(name):
	urls = history.url_gen3(name)
	duration = {}
	for i in range(0,len(urls)):
		data = history.data_gen(urls[i])
		for item in data['games']['games']:
			duration[item['gameId']] = round(float(item['gameDuration'])/60.,2)
	return duration		

def average_duration(name):
	durations = duration(name).values()
	total = 0. 
	for item in durations:
		total += item
	return round(total/float(len(durations)),2)

def winloss(name):
	urls = history.url_gen3(name)
	win_loss = {}
	for i in range(0,len(urls)):
		data = history.data_gen(urls[i])
		for item in data['games']['games']:
			win_loss[item['gameId']] = item['participants'][0]['stats']['win']
	return win_loss

def winloss_ratio(name):
	win_loss = winloss(name).values()
	wins = 0
	for item in win_loss:
		if item == True:
			wins += 1
	return round(float(wins)/float(len(win_loss)),4)

def kda_per_game(name):
	urls = history.url_gen3(name)
	KDA = {}
	for i in range(0,len(urls)):
		data = history.data_gen(urls[i])
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
	urls = history.url_gen3(name)
	KDA = {'kills': 0, 'assists': 0, 'deaths': 0}
	for i in range(0,len(urls)):
		data = history.data_gen(urls[i])
		for item in data['games']['games']:
			KDA['kills'] = KDA['kills'] + item['participants'][0]['stats']['kills']
			KDA['deaths'] = KDA['deaths'] + item['participants'][0]['stats']['deaths']
			KDA['assists'] = KDA['assists'] + item['participants'][0]['stats']['assists']
	return KDA, round((float(KDA['kills']) + float(KDA['assists']))/float(KDA['deaths']),2)


def role_and_lane(name):
	urls = history.url_gen3(name)
	rolelane = {}
	for i in range(0,len(urls)):
		data = history.data_gen(urls[i])
		for item in data['games']['games']:
			game = {}
			game['role'] = item['participants'][0]['timeline']['role']
			game['lane'] = item['participants'][0]['timeline']['lane']
			rolelane[item['gameId']] = game
	return rolelane

def gold_per_game(name):
	urls = history.url_gen3(name)
	gold = {}
	for i in range(0,len(urls)):
		data = history.data_gen(urls[i])
		for item in data['games']['games']:
			game_gold = {}
			game_gold['goldEarned'] = item['participants'][0]['stats']['goldEarned']
			game_gold['goldSpent'] = item['participants'][0]['stats']['goldSpent']
			gold[item['gameId']] = game_gold
	return gold		

def average_gold(name):
	golds = gold_per_game(name).values()
	overall = {'goldEarned': 0, 'goldSpent': 0}
	for i in range(0,len(golds)):
		overall['goldEarned'] = overall['goldEarned'] + golds[i]['goldEarned']
		overall['goldSpent'] = overall['goldSpent'] + golds[i]['goldSpent']
	overall['goldEarned'] = round(float(overall['goldEarned'])/float(len(golds)),2)
	overall['goldSpent'] = round(float(overall['goldSpent'])/float(len(golds)),2)
	return overall

def cc_per_game(name):
	urls = history.url_gen3(name)
	cc = {}
	for i in range(0,len(urls)):
		data = history.data_gen(urls[i])
		for item in data['games']['games']:
			cc[item['gameId']] = round(float(item['participants'][0]['stats']['totalTimeCrowdControlDealt'])/60.,2)
	return cc		

def average_cc(name):
	ccs = cc_per_game(name).values()
	time = 0.
	for item in ccs:
		time += item
	return round(time/float(len(ccs)),2)




