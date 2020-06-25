
__module__      = 'ovirt/connection.py'
__author__      = 'Rob Mitchell <rob.mitchell@objectstream.com>'
__updated__     = '2020.06.25'
__version__     = '0.1.0'
__status__      = 'development'


import ovirtsdk4 as sdk
import os


class OVirtConnection:
    def __init__(self):
        self.engine_host = os.environ.get('OVIRT_HOST')
        self.engine_username = os.environ.get('OVIRT_USERNAME')
        self.engine_password = os.environ.get('OVIRT_PASSWORD')


def connect():
	try:
		connection = sdk.Connection(
 	 	  url='https://vhost1.okc.objectstream.com/ovirt-engine/api',
 	 	  username=creds['username'],
 	 	  password=creds['password'],
 	 	  ca_file='ovirt.ca.pem',
 	 	  debug=True,
		)
		return connection
	except:
		return None


