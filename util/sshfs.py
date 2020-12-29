import subprocess
import time

class SSHFS():
	def __init__(self):
		self.config = {'remote':'root@sslhelper.okc.objectstream.com:/mnt/backup_workspace','local':'/mnt/backup_workspace'}


