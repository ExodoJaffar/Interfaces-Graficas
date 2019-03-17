#coding:utf8
#py:3.6

from json import dumps
from json import loads

def readJson():
	try:
		json = None
		with open('contas.json','r+') as txt:
			json = txt.read()
		return loads(json)

	except:
		return None

def writeJson(newData):
	try:
		json = readJson()
		with open('contas.json','w') as txt:
			json['Contas'].update(newData)
			txt.write(dumps(json, sort_keys=True, indent=4))

	except Exception as e:
		print(e)
		pass
