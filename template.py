from docx import Document
#from globals import Templates
from json import loads , dump


def renderTemplate(templateId,data,outputFileName):
		doc = Document('projectTemplates/'+templateId+'.docx')
		for para in doc.paragraphs:
			for key, value in data.items():
				if f'%{key}%' in para.text:
					para.text = para.text.replace(f'%{key}%',value)
		doc.save('outputs/'+outputFileName)
		
def getTemplates():
	templates = []
	with open('templateSchema.txt','rt') as file:
		temRaw = file.read().split('\n\n')
		for temp in temRaw:
			temp = temp.split('\n')
			templates.append({'id':temp[0],'name':temp[1],'author':temp[2],'pageCount':temp[3],'tag':temp[4]})
		return templates