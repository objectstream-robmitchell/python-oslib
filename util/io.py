
__module__      = 'io.py'
__maintainer__  = 'rob.mitchell@objectstream.com'
__version__     = '0.1.0'
__status__      = 'development'


import requests 

class IO:
	def get_file(filename):
		with open(filename,'rb') as f:
			return f.read()

	def put_file(filename,data):
		with open(filename,'wb') as f:
			f.write(data)

	def get_resource(url,get_bytes=False):
		response = requests.get(url)
		if not str(response.status_code).startswith('2'):
			raise Exception(response.status_code,url)
		if get_bytes:
			return resp.content
		return resp.text
		
