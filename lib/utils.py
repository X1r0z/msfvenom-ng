import os,sys

def check_env():
	if os.path.exists('tmp') and os.path.isfile('config.py') and os.path.isfile('rules.json'):
		return True
	else:
		return False

def initialization():
	cprint('Initializing','info')
	try:
		os.mkdir('tmp')
		with open('config.py','w+') as f:
			f.write(config_content)
		with open('rules.json','w+') as f:
			f.write(rules_content)
		cprint('Initialized successfully','succ')
	except:
		cprint('Initialized failed','err')
		sys.exit()

def cprint(message,level):
    if level == 'err':
        print('[-] ' + message)
    elif level == 'info':
        print('[*] ' + message)
    elif level == 'succ':
        print('[+] ' + message)
    else:
        raise Exception('LEVEL ERROR')

config_content = '''TODO
'''

rules_content = '''{
"x86": {
	"test_rule": "S1"
	}
}
'''