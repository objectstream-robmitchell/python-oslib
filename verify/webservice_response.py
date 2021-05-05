
__module__     = 'webservice_response.py'
__maintainer__ = 'Rob Mitchell <rob.mitchell@objectstream.com>,<rlmitchell@gmail.com>'
__tested_on__  = 'Python 3.6.8'
__version__    = '2021.01.20.1314'


import requests


class WebServiceResponse:
   def __init__(self,url,debug=False):
      self.debug = debug
      self.url = url

   def running(self):
      try:
         resp = requests.get(self.url)
         if self.debug: print('resp.status_code:'+str(resp.status_code))
         if resp.status_code != 200:
            return False
         return True
      except:
         return False

   def content(self,text):
      try:
         resp = requests.get(self.url)
         if self.debug: print(resp.content.decode())
         if text in resp.content.decode():
            return True
         return False
      except:
         return False



if __name__ == '__main__':
	if WebServiceResponse('https://www.python.org').running():
		print('running')
	
	if WebServiceResponse('https://www.python.org').content('Download'):
		print('content present')
	


