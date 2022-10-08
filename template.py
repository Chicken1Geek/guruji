from docx import Document
from globals import Templates

def renderTemplate(templateId,data,outputFileName):
		doc = Document('projectTemplates/'+templateId+'.docx')
		for para in doc.paragraphs:
			for key, value in data.items():
				para.text = para.text.replace(f'%{key}%',value)
		doc.save('outputs/'+outputFileName)