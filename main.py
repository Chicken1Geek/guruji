from flask import Flask , send_file ,request ,render_template
from flask_cors import CORS
import os
from template import renderTemplate, getTemplates
from analytics import record
from random import randint

app = Flask('Guruji Backend')
CORS(app)
garbageList = []

@app.route('/')
def home():
	return render_template('index.html',temps=getTemplates())

@app.route('/api/generate/<templateId>')
def generateFromTemplate(templateId):
	templateId = templateId.lower().strip()
	args = request.args.to_dict()
	outputFileName = str(randint(1000,9999)) + args['name'].replace(" ",'') + templateId + '.docx'
	renderTemplate(templateId,args,outputFileName)
	record(args['name'])
	return outputFileName

@app.route('/<filecode>')
def sendFile(filecode):
	garbageList.append(filecode)
	return send_file('outputs/'+filecode)

@app.route('/admin/ping')
def ping():
  for file in os.listdir('outputs'):
    os.remove('outputs/'+file)
    

  return ''
app.run('0.0.0.0',port='8080')
