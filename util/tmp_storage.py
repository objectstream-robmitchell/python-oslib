import os

class SSHFS2():

	def __init__(self):
		self._check_user_id()
		self.config = {'remote':'root@sslhelper.okc.objectstream.com:/mnt/backup_workspace','local':'/mnt/backup_workspace'}

	def _check_user_id(self):
		if not os.getuid() == 0:
			raise Exception('SSHFS must be envoked by the roor user.')


SSHFS2()

