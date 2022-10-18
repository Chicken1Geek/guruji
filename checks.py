import os
import json

if 'analytics.json' not in os.listdir():
	os.system('touch analytics.json')
	with open('analytics.json','w') as file:
		json.dump({},file)
if 'outputs' not in os.listdir():
	os.mkdir('outputs')