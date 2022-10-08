from json import load,dump

def loadDatabase():
	with open('analytics.json','r+') as file:
		db = load(file)
		return db

def dumpDatabase(db):
	with open('analytics.json','w+') as file:
		dump(db,file)

def record(name):
	db = loadDatabase()
	try:
		db['fileCount'] += 1
	except KeyError:
		db['fileCount'] = 1
	try:
		db['names'].append(name)
	except:
		db['names'] = [name]
	dumpDatabase(db)
	