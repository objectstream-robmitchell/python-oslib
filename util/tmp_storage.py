import os
import subprocess


class TmpStorage():

	def __init__(self):
		self.config = {'remote':'root@sslhelper.okc.objectstream.com:/mnt/backup_workspace','local':'/mnt/backup_workspace'}
		self._check_user_id()
		self._check_local_dir()

	def __call__(self):
		self.mount()

	def mount(self):
		pass

	def umount(self):
		if not subprocess.run('',shell=True,check=True):
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




