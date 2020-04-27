
"""
__module__      = 'ostime.py'
__author__      = 'Rob Mitchell <rob.mitchell@objectstream.com>, <rlmitchell@gmail.com>'
__updated__     = '2020.04.27'
__version__     = '1.0.0'
__status__      = 'development'
__description__ = 'Objectstream Time Utilities' 

__history__     = '''
						2020.03.04 - initial development
						'''
"""

# ToDo:
# - needs class and method docs


import time
import datetime

class OSTime:
	"""
	OSTime class is used to get formatted time values.
	"""

	def epoch(self,string=False):
		"""Return current epoch.

		:param string: return type str
		:type  string: boolean 

		:returns: current epoch
		:rtype:   str or int
		"""
		
		if string:
			return str(time.time()).split('.')[0]
		else:
			return int(time.time())

	def hms(self):
		n = datetime.datetime.now()
		return ''.join( [x if len(x) > 1 else '0'+x for x in (str(n.year),str(n.month),
					str(n.day),str(n.hour),str(n.minute),str(n.second))] )

	def ymd(self):
		n = datetime.datetime.now()
		return ''.join( [x if len(x) > 1 else '0'+x for x in (str(n.year),str(n.month),str(n.day))] )




if __name__ == '__main__':
	ostime = OSTime()
	print 'epoch():'
	print ostime.epoch(), str(type(ostime.epoch())), '()'
	print ostime.epoch(string=False), str(type( ostime.epoch(string=False) )), ''
	print ostime.epoch(string=True), str(type( ostime.epoch(string=True) )), ''
	print ostime.epoch(False), str(type( ostime.epoch(False) )), ''
	print ostime.epoch(True), str(type( ostime.epoch(True) )), ''
		

