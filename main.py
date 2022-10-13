from flask import Flask , send_file ,request ,render_template
from flask_cors import CORS
import os
from template import renderTemplate , getTemplates
from analytics import record
from random import randint
from zipfile import ZipFile
import datetime
import checks

app = Flask('Guruji Backend')
CORS(app)


@app.route('/')
def home():
	return render_template('index.html',temps=getTemplates())
	
@app.route('/new')
def newTheme():
	return render_template('index-new.html',temps=getTemplates())

@app.route('/favicon.ico')
def favicon():
	return send_file('static/favicon.ico')

@app.route('/api/generate/<templateId>')
def generateFromTemplate(templateId):
	templateId = templateId.lower().strip()
	args = request.args.to_dict()
	args['template'] = templateId
	args['timestamp'] = datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')
	outputFileName = str(randint(1000,9999)) +'!' + templateId + '.docx'
	renderTemplate(templateId,args,outputFileName)
	record(args)
	return outputFileName

@app.route('/<filecode>')
def send_File(filecode):
	templateId = filecode.split('!')[1].split('.')[0]
	for temp in getTemplates():
		if temp['id'] == templateId:
			try:
				templateChild = temp['data']['child'].split('&')
			except KeyError:
				return send_file('outputs/'+filecode)
	with ZipFile(filecode.split('.')[0]+'.zip',mode='a') as zip:
		os.rename('outputs/'+filecode,filecode)
		zip.write(filecode)
		os.remove(filecode)
		for i in templateChild:
			os.rename('projectTemplates/'+i,i)
			zip.write(i)
			os.rename(i,'projectTemplates/'+i)
		os.rename(filecode.split('.')[0]+'.zip','outputs/'+filecode.split('.')[0]+'.zip')
	return send_file('outputs/'+filecode.split('.')[0]+'.zip')

@app.route('/admin/ping')
def ping():
  for file in os.listdir('outputs'):
    os.remove('outputs/'+file)
  return ''
app.run('0.0.0.0',port='8080')