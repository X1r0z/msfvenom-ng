import json

class con(object):
	def __init__(self):
		pass

	def get_config(self):
		with open('config.json') as f:
			raw = f.read()
		jsondata = json.loads(raw)
		return jsondata

	def print_config(self, jsondata):
		for k,v in jsondata.items():
			print(k + ': ' + v)

	def save_config(self,jsondata):
		with open('config.json', 'w') as f:
			raw = json.dumps(jsondata)
			f.write(raw)