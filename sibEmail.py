from __future__ import print_function
import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException
import base64
from template import getTemplate

configuration = sib_api_v3_sdk.Configuration()
configuration.api_key['api-key'] = 'xkeysib-' + open('sibKey.txt').read().strip('\n')
api_instance = sib_api_v3_sdk.TransactionalEmailsApi(sib_api_v3_sdk.ApiClient(configuration))

def sendProjectEmail(email,name,template,file):
	sender = {"email":"guruji.chickengeek@gmail.com"}
	to = [{"email":email}]
	params = {"NAME":name,"TEMP":getTemplate(template)['name'],"SOURCE":f'https://guruji-dev.sachins5.repl.co/source/{template}'}
	with open('outputs/'+file,'rb') as j:
		attachments = [{'content':base64.b64encode(j.read()).decode(),'name':file}]
	send_smtp_email = sib_api_v3_sdk.SendSmtpEmail(to=to, template_id=3, sender=sender,params=params,attachment=attachments)
	api_response = api_instance.send_transac_email(send_smtp_email)
	print(api_response)
