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
		site (string):  Site to inspect. ex: 'www.objectstream.com'
		port (int):     Port to connect to.  Default: 443
		"""

		self.site = site
		self.port = port


	def expired(self,warning_days=5):
		"""
		"""

		cert = ssl.get_server_certificate((self.site, self.port))
		x509 = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, cert)
		expire_datetime = datetime.strptime(str(x509.get_notAfter())[2:10], '%Y%m%d')
		return datetime.now() < expire_datetime - timedelta(days=warning_days) 



