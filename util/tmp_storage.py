import os
import subprocess


class TmpStorage():

	def __init__(self):
		self._check_user_id()
		self.config = {'remote':'root@sslhelper.okc.objectstream.com:/mnt/backup_workspace','local':'/mnt/backup_workspace'}

	def is_mounted(self):
		for line in subprocess.getoutput('/usr/bin/mount').split('\n'):
			if self.config['remote'] in line:
				return True
		return False

	def _check_user_id(self):
		if not os.getuid() == 0:
			raise Exception('SSHFS must be envoked by the roor user.')




