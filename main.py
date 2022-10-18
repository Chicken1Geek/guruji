from flask import Flask , send_file ,request ,render_template ,jsonify, redirect
from flask_cors import CORS
import os
from template import renderTemplate , getTemplates ,getTemplate
from analytics import record
from random import randint
from zipfile import ZipFile
import datetime
import checks
from sibEmail import sendProjectEmail
app = Flask('Guruji Backend')
CORS(app)


@app.route('/')
def home():
	return render_template('index.html',temps=getTemplates())

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
	resultArray = [outputFileName]
	for temp in getTemplates():
		if temp['id'] == templateId:
			print(temp.keys())
			if 'child' in list(temp['data'].keys()):
				for i in temp['data']['child'].split('&'):
					resultArray.append(i)
	record(args)
	urlString = ''
	for i in resultArray:
		urlString += i+','
	return jsonify({'urls':resultArray,'data':{'name': args['name'],'file':outputFileName,'templateId':templateId,'filesurl':urlString.strip(',')}})

@app.route('/cdn/<filecode>')
def serveFile(filecode):
	if '!' in filecode:
		return send_file('outputs/'+ filecode)
	else:
		return send_file('projectTemplates/'+filecode)

@app.route('/api/email')
def serveEmail():
	args = request.args.to_dict()
	
	sendProjectEmail(args['toemail'],args['name'],args['template'],args['file'])
	return redirect('/')

@app.route('/source/<template>')
def source(template):
	temp = getTemplate(template)
	files = temp['data']['child'].split('&')
	print(temp['data']['child'].split('&'))
	name = temp['name']
	return render_template('source.html',name=name,files=files)
	
@app.route('/admin/ping')
def ping():
  for file in os.listdir('outputs'):
    os.remove('outputs/'+file)
  return ''
app.run('0.0.0.0',port='8080')