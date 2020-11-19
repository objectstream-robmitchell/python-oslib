"""
__module__      = 'SSLExpiry.py'
__author__      = 'Rob Mitchell <rob.mitchell@objectstream.com>, <rlmitchell@gmail.com>'
__version__     = '2020.11.19.0949'
__status__      = 'development'
__description__ = 'Objectstream SSL Expiration Check Class' 
__tested_on__   = 'Python 3.6.8'
"""

import ssl
import OpenSSL
from datetime import datetime, timedelta


class SSLExpiry:
	def __init__(self,site,port=443):
		"""
		Initialize SSLExpiry with site and port.
	
		Parameters:
		- site (string):  Site to inspect.     Ex: 'www.objectstream.com'
		- port (int):     Port to connect to.  Default: 443
		"""

		#self.site = site
		#self.port = port
		self.cert = ssl.get_server_certificate((site, port))
		self.x509 = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, self.cert)


	def __call__(self):
		"""
		Default action; calls valid().
		"""

		return self.valid()


	def valid(self,warning_days=10):
		"""
		Determine if SSL certificate is expired.

		Parameters:
		- warning_days (int):  Number of days to subtract from actual expiry date.  Default: 10

		Returns:
		- (bool):  True if within warning window.
		"""

		expire_datetime = datetime.strptime(str(self.x509.get_notAfter())[2:10], '%Y%m%d')
		return datetime.now() < expire_datetime - timedelta(days=warning_days) 


	def expire_Ymd(self):
		"""
		Gets cert expire date.
		
		Returns:
		- (string): Expire date formatted %Y%m%d.
		"""

		return str(self.x509.get_notAfter())[2:10]


