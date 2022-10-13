import os
import json

if 'analytics.json' not in os.listdir():
	os.system('touch analytics.json')
	with open('analytics.json') as file:
		json.dump({},file)