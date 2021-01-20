
__module__     = 'tmp_storage.py'
__maintainer__ = 'Rob Mitchell <rob.mitchell@objectstream.com>,<rlmitchell@gmail.com>'
__tested__     = 'Python 3.5.2'
__version__    = '2021.01.20.1318'


import os
import subprocess


class TmpStorage():
	def __init__(self,config={}):
		self.config = config
		self._check_user_id()
		self._check_local_dir()

	def __call__(self):
		self.mount()

	def mount(self):
		if not self.is_mounted():
			if not subprocess.run('sshfs '+self.config['remote']+' '+self.config['local'],shell=True,check=True):
				raise Exception('mount error')

	def umount(self):
		if not subprocess.run('/usr/bin/fusermount -u '+self.config['local'],shell=True,check=True):
			raise Exception('umount error')

	def is_mounted(self):
		for line in subprocess.getoutput('/usr/bin/mount').split('\n'):
			if self.config['remote'] in line:
				return True
		return False

	def _check_user_id(self):
		if not os.getuid() == 0:
			raise Exception('SSHFS must be envoked by the roor user.')

	def _check_local_dir(self):
		if not os.path.isdir( self.config['local'] ):
			os.mkdir( self.config['local'], mode=0o700 )

