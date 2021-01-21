
__module__      = 'io.py'
__maintainer__ = 'Rob Mitchell <rob.mitchell@objectstream.com>,<rlmitchell@gmail.com>'
__tested__     = 'Python 3.6.8'
__version__    = '2021.01.21.0858'


import requests


class IO:
	@classmethod
	def get_file(cls,filename):
		with open(filename,'rb') as f:
			return f.read()

	@classmethod
	def put_file(cls,filename,data):
		if not isinstance(data,bytes):
			raise Exception('data != bytes')
		with open(filename,'wb') as f:
			f.write(data)

	@classmethod
	def get_resource(cls,url,get_bytes=True):
		resp = response = requests.get(url)
		if not str(resp.status_code).startswith('2'):
			raise Exception(resp.status_code,url)
		if get_bytes:
			return resp.content
		return resp.text
		
