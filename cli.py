from rich.console import Console
from pastebin import generatePastebinMap ,getPastebinUrl
cli = Console()

cli.print('[green]Guruji Backend CLI')

def runChecks():
	import checks

commands = ['help',"check",'genpbm','getpb']
while True:
	com = cli.input('[yellow]\n≥≥≥  ')
	if com not in commands:
		cli.print('[red]Invalid Command')
		pass
	if com == 'help':
		for i in commands:
			cli.print(f'{i}')
	if com == 'check':
		runChecks()
		cli.print('[green]Checks completed')
	if com == 'genpbm':
		generatePastebinMap()
	if com == 'getpb':
		j = cli.input('Enter template id : ')
		print(j)
		cli.print(getPastebinUrl(j))