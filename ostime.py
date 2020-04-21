
__module__      = 'ostime.py'
__author__      = 'Rob Mitchell <rob.mitchell@objectstream.com>'
__last_update__ = '2020.03.04'
__version__     = '0.0.1'
__status__      = 'development'
__description__ = 'Objectstream Time Utilities' 


import time
import datetime

class OSTime:
	def epoch(self,string=False):
		if string:
			return str(time.time()).split('.')[0]
		else:
			return int(time.time())
		

