import json

class enc(object):
	def __init__(self):
		self.encoders = {
			'x64': {
				'X': 'x64/xor',
				'Z': 'x64/zutto_dekiru'
			},
			'x86': {
				'F': 'x86/add_sub',
				'H': 'x86/alpha_mixed',
				'E': 'x86/alpha_upper',
				'R': 'x86/avoid_underscore_tolower',
				'U': 'x86/avoid_utf8_tolower',
				'X': 'x86/bloxor',
				'B': 'x86/bmp_polyglot',
				'C': 'x86/call4_dword_xor',
				'P': 'x86/context_cpuid',
				'T': 'x86/context_stat',
				'I': 'x86/context_time',
				'D': 'x86/countdown',
				'M': 'x86/fnstenv_mov',
				'J': 'x86/jmp_call_additive',
				'K': 'x86/nonalpha',
				'L': 'x86/nonupper',
				'O': 'x86/opt_sub',
				'V': 'x86/service',
				'S': 'x86/shikata_ga_nai',
				'G': 'x86/single_static_bit',
				'Y': 'x86/unicode_mixed',
				'N': 'x86/unicode_upper'
			}
		}

	def parse_encs(self, arch, data):
		encs = ''
		e = data[::2]
		i = data[1::2]
		for c in e[:-1]:
			encs += '-e ' + self.encoders.get(arch).get(c) + ' -i ' + i[e.index(c)] + ' -a ' + arch + ' --platform windows -f raw | msfvenom -p - '
		encs += '-e ' + self.encoders.get(arch).get(e[-1]) + ' -i ' + i[e.index(e[-1])] + ' -a ' + arch + ' --platform windows  '
		return encs

	def get_encs(self):
		with open('rules.json') as f:
			raw = f.read()
		jsondata = json.loads(raw)
		return jsondata 

	def print_encs(self, jsondata, arch):
		rlist = list(jsondata.get(arch).keys())
		for r in rlist:
			print('(' + str(rlist.index(r)) + ') ' + r)

	def index_encs(self, jsondata, arch, i):

		rlist = list(jsondata.get(arch).keys())
		value = jsondata.get(arch).get(rlist[int(i)])
		return value