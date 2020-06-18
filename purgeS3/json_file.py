
"""
__module__      = 'jsonfile.py'
__author__      = 'Rob Mitchell <rlmitchell@gmail.com>,<rob.mitchell@objectstream.com>'
__updated__     = '2020.04.23'
__version__     = '0.0.1'
__status__      = 'development'
__github__      = 'https://github.com/rlmitchell/python-utils'
"""

import json

class JSONFile(object):
	"""
	JSONFile object used to read and write json file to disk.
	"""

	
	def __init__(self,filename):
		"""Instantiate JSONFile object.

		:param filename: path to json file
		:type  filename: str
		"""
		
		self.filename = filename


	def load(self):
		"""Loads json from file.

		:returns: data from json file
		:rtype:   dict
		"""

		with open(self.filename) as fp:
			return json.load(fp)


	def save(self,data):
		"""Saves json to file. 

		:param data: data to save as json
		:type  date: dict
		"""

		with open(self.filename,'w') as fp:
			json.dump(data,fp,indent=4)
