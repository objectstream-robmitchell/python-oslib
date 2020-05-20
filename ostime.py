
"""
__module__      = 'ostime.py'
__author__      = 'Rob Mitchell <rob.mitchell@objectstream.com>, <rlmitchell@gmail.com>'
__updated__     = '2020.05.20'
__version__     = '1.1.0'
__status__      = 'development'
__description__ = 'Objectstream Time Utilities' 

__history__     = '''
						2020.05.20 - added utc 
						2020.03.04 - initial development
						'''
"""


import time
import datetime


class OSTime:
	"""
	OSTime class is used to get formatted time values.
	"""

	EPOCH = datetime.datetime(1970, 1, 1, 0, 0)


	def __init__(self,utc=False):
		self.now = datetime.datetime.now()
		if utc:
			self.now = self.now.utcnow()


	def epoch(self):
		"""Return epoch.

		:returns: epoch
		:rtype:   int
		"""

		return int((self.now - OSTime.EPOCH).total_seconds())


	def hms(self):
		"""Return timestamp as YYYYMMDDHHMMSS

		"""

		n = self.now
		return ''.join( [x if len(x) > 1 else '0'+x for x in (str(n.year),str(n.month),
					str(n.day),str(n.hour),str(n.minute),str(n.second))] )


	def ymd(self):
		"""Return timestamp as YYYYMMDD

		"""

		n = self.now
		return ''.join( [x if len(x) > 1 else '0'+x for x in (str(n.year),str(n.month),str(n.day))] )


