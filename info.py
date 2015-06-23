import history
import pickle

def gameids(name):
	urls = history.url_gen3(name)
	ids = []
	for i in range(0,len(urls)):
		data = history.data_gen(urls[i])
		for item in data['games']['games']:
			ids.append(item['gameId'])
	return ids

# TODO: write another program that creates a dictionary of champId to champ
def champions(name):
	ids = pickle.load(open('champions.p','rb'))
	urls = history.url_gen3(name)
	champs = {}
	for i in range(0,len(urls)):
		data = history.data_gen(urls[i])
		for item in data['games']['games']:
			champs[item['gameId']] = ids[str(item['participants'][0]['championId'])]
	return champs		

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

def vision_per_game(name):
	urls = history.url_gen3(name)
	vision = {}
	for i in range(0,len(urls)):
		data = history.data_gen(urls[i])
		for item in data['games']['games']:
			vision_game = {}
			vision_game['placed'] = item['participants'][0]['stats']['wardsPlaced']
			vision_game['killed'] = item['participants'][0]['stats']['wardsKilled']
			vision[item['gameId']] = vision_game
	return vision
	
def average_vision(name):
	visions = vision_per_game(name).values()
	overall = {'placed': 0, 'killed': 0}
	for i in range(0,len(visions)):
		overall['placed'] = overall['placed'] + visions[i]['placed']
		overall['killed'] = overall['killed'] + visions[i]['killed']
	overall['placed'] = round(float(overall['placed'])/float(len(visions)),2)
	overall['killed'] = round(float(overall['killed'])/float(len(visions)),2)
	return overall

def kills_per_game(name):
	urls = history.url_gen3(name)
	kills = {}
	for i in range(0,len(urls)):
		data = history.data_gen(urls[i])
		for item in data['games']['games']:
			kills_game = {}
			# consecutive kills before death
			kills_game['largest spree'] = item['participants'][0]['stats']['largestKillingSpree']
			# largest number of kills in a period of time
			kills_game['largest multikill'] = item['participants'][0]['stats']['largestMultiKill']
			kills_game['killingsprees'] = item['participants'][0]['stats']['killingSprees']
			kills_game['double'] = item['participants'][0]['stats']['doubleKills']
			kills_game['triple'] = item['participants'][0]['stats']['tripleKills']
			kills_game['quadra'] = item['participants'][0]['stats']['quadraKills']
			kills_game['penta'] = item['participants'][0]['stats']['pentaKills']
			kills[item['gameId']] = kills_game
	return kills		


def turrets_inhibitors_per_game(name):
	urls = history.url_gen3(name)
	turrets_inhibitors = {}
	for i in range(0,len(urls)):
		data = history.data_gen(urls[i])
		for item in data['games']['games']:
			per_game = {}
			per_game['turrets'] = item['participants'][0]['stats']['turretKills']
			per_game['inhibitors'] = item['participants'][0]['stats']['inhibitorKills']
			turrets_inhibitors[item['gameId']] = per_game
	return turrets_inhibitors		

def average_ti(name):
	ti = turrets_inhibitors_per_game(name).values()
	overall = {'turrets':0, 'inhibitors': 0}
	for i in range(0,len(ti)):
		overall['turrets'] = overall['turrets'] + ti[i]['turrets']
		overall['inhibitors'] = overall['inhibitors'] + ti[i]['inhibitors']
	overall['turrets'] = round(float(overall['turrets'])/float(len(ti)),2)
	overall['inhibitors'] = round(float(overall['inhibitors'])/float(len(ti)),2)	
	return overall

# dealt to champions
def damage_dealt_per_game(name):
	urls = history.url_gen3(name)
	damage = {}
	for i in range(0,len(urls)):
		data = history.data_gen(urls[i])
		for item in data['games']['games']:
			per_game = {}
			per_game['total'] = item['participants'][0]['stats']['totalDamageDealtToChampions']
			per_game['magic'] = item['participants'][0]['stats']['magicDamageDealtToChampions']
			per_game['physical'] = item['participants'][0]['stats']['physicalDamageDealtToChampions']
			per_game['true'] = item['participants'][0]['stats']['trueDamageDealtToChampions']
			damage[item['gameId']] = per_game
	return damage
	
def average_dd(name):
	dd = damage_dealt_per_game(name).values()
	overall = {'total':0, 'magic': 0,'physical':0,'true': 0}
	for i in range(0,len(dd)):
		overall['total'] = overall['total'] + dd[i]['total']
		overall['magic'] = overall['magic'] + dd[i]['magic']
		overall['physical'] = overall['physical'] + dd[i]['physical']
		overall['true'] = overall['true'] + dd[i]['true']
	overall['total'] = round(float(overall['total'])/float(len(dd)),2)
	overall['magic'] = round(float(overall['magic'])/float(len(dd)),2)
	overall['physical'] = round(float(overall['physical'])/float(len(dd)),2)
	overall['true'] = round(float(overall['true'])/float(len(dd)),2)				
	return overall

# damage taken overall (minions, neutrals, champs)
def damage_taken_per_game(name):
	urls = history.url_gen3(name)
	damage = {}
	for i in range(0,len(urls)):
		data = history.data_gen(urls[i])
		for item in data['games']['games']:
			per_game = {}
			per_game['total'] = item['participants'][0]['stats']['totalDamageTaken']
			per_game['magic'] = item['participants'][0]['stats']['magicalDamageTaken']
			per_game['physical'] = item['participants'][0]['stats']['physicalDamageTaken']
			per_game['true'] = item['participants'][0]['stats']['trueDamageTaken']
			damage[item['gameId']] = per_game
	return damage

def average_dt(name):
	dt = damage_dealt_per_game(name).values()
	overall = {'total':0, 'magic': 0,'physical':0,'true': 0}
	for i in range(0,len(dt)):
		overall['total'] = overall['total'] + dt[i]['total']
		overall['magic'] = overall['magic'] + dt[i]['magic']
		overall['physical'] = overall['physical'] + dt[i]['physical']
		overall['true'] = overall['true'] + dt[i]['true']
	overall['total'] = round(float(overall['total'])/float(len(dt)),2)
	overall['magic'] = round(float(overall['magic'])/float(len(dt)),2)
	overall['physical'] = round(float(overall['physical'])/float(len(dt)),2)
	overall['true'] = round(float(overall['true'])/float(len(dt)),2)				
	return overall

def minions_per_game(name):
	urls = history.url_gen3(name)
	minions = {}
	for i in range(0,len(urls)):
		data = history.data_gen(urls[i])
		for item in data['games']['games']:
			minions[item['gameId']] = item['participants'][0]['stats']['totalMinionsKilled']
	return minions		

def average_minions(name):
	minion = minions_per_game(name).values()
	overall = {'total': 0}
	for i in minion:
		overall['total'] +=  i
	overall['total'] = round(float(overall['total'])/float(len(minion)),2)
	return overall

def neutrals_per_game(name):
	urls = history.url_gen3(name)
	neutrals = {}
	for i in range(0,len(urls)):
		data = history.data_gen(urls[i])
		for item in data['games']['games']:
			per_game = {}
			# blue side - baron, red side - dragon
			per_game['total'] = item['participants'][0]['stats']['neutralMinionsKilled']
			per_game['team jungle']	= item['participants'][0]['stats']['neutralMinionsKilledTeamJungle']
			per_game['enemy jungle'] = item['participants'][0]['stats']['neutralMinionsKilledEnemyJungle']
			neutrals[item['gameId']] = per_game
	return neutrals

def average_neutrals(name):
	neutral = neutrals_per_game(name).values()
	overall = {'total': 0, 'team': 0, 'enemy': 0}
	for i in range(0,len(neutral)):
		overall['total'] = overall['total'] + neutral[i]['total']
		overall['team'] = overall['team'] + neutral[i]['team jungle']
		overall['enemy'] = overall['enemy'] + neutral[i]['enemy jungle']
	overall['total'] = round(float(overall['total'])/float(len(neutral)),2)
	overall['team'] = round(float(overall['team'])/float(len(neutral)),2)
	overall['enemy'] = round(float(overall['enemy'])/float(len(neutral)),2)	
	return overall

# this'll be kinda hard to use
def perten_per_game(name):
	urls = history.url_gen3(name)
	diffs = {}
	for i in range(0,len(urls)):
		data = history.data_gen(urls[i])
		for item in data['games']['games']:
			per_game = {}
			per_game['cs per 10'] = item['participants'][0]['timeline']['creepsPerMinDeltas']
			if 'csDiffPerMinDeltas' in item['participants'][0]['timeline'].keys():
				per_game['cs diff per 10'] = item['participants'][0]['timeline']['csDiffPerMinDeltas']
			else:
				per_game['cs diff per 10'] = "No enemy laner"
			diffs[item['gameId']] = per_game
	return diffs
			
# so yeah, the RIOT api is busted up in terms of first blood assist and anything related to first inhibitor takes
# idk how valuable this is anymore
def firsts(name):
	urls = history.url_gen3(name)
	first = {}
	for i in range(0,len(urls)):
		data = history.data_gen(urls[i])
		for item in data['games']['games']:
			per_game = {}
			per_game['first kill'] = item['participants'][0]['stats']['firstBloodKill']
			# i think the API is broken. no one ever has first blood assist
			# per_game['first kill assist'] = item['participants'][0]['stats']['firstBloodAssist']
			per_game['first turret'] = item['participants'][0]['stats']['firstTowerKill']
			per_game['first turret assist']= item['participants'][0]['stats']['firstTowerAssist']
			# for some reason, firstinhibitorkill/assist disappear when you put the data in a for loop. idk why. 
			# if you manually do data[0], data[1], etc. it shows up, but not in a for loop
			# per_game['first inhibitor'] = item['participants'][0]['stats']['firstInhibitorKill']
			# per_game['first inhibitor assist'] = item['participants'][0]['stats']['firstInhibitorAssist']
			first[item['gameId']] = per_game
	return first
	
def overall_firsts(name):
	fs = firsts(name).values()
	overall = {'first kill': 0, 'first turret':0, 'first turret assist':0}
	for i in range(len(fs)):
		if fs[i]['first kill'] == True:
			overall['first kill'] += 1
		if fs[i]['first turret'] == True:
			overall['first turret'] += 1
		if fs[i]['first turret assist'] == True:
			overall['first turret assist'] += 1	
	return overall					