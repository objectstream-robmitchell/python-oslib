
__module__     = 'mysqldump.py'
__maintainer__ = 'Rob Mitchell <rob.mitchell@objectstream.com>,<rlmitchell@gmail.com>'
__tested__     = 'Python 3.6.8'
__version__    = '2021.01.21.1057'


import subprocess
import hashlib
import platform
from util.timestamp import Timestamp


class MySQLDump:
   def __init__(self,**kwargs):
      self.kwargs = kwargs
      self.kwargs['timestamp'] = Timestamp().epoch()
      self.kwargs['hostname'] = platform.node().split('.')[0]
      self.backup_name = self.kwargs['tmpdir']+'/'
      self.backup_name += self.kwargs['backup_prefix']+'.'+self.kwargs['hostname']
      self.backup_name += '.'+self.kwargs['database_name']+'.'+self.kwargs['timestamp']

   def __call__(self):
      self._run_checks()
      self._dump()
      return self.backup_name

   def _run_checks(self):
      self._check_aes_key()
      self._check_tmpdir_mounted()

   def _check_tmpdir_mounted(self):
      if self.kwargs['tmpdir'] not in subprocess.getoutput('/usr/bin/mount'):
         raise Exception('tmpdir not found')

   def _check_aes_key(self):
      with open(self.kwargs['gpg_keyfile'],'rb') as f:
         md5hash = hashlib.md5(f.read()).hexdigest()
      if md5hash != self.kwargs['gpg_keyfile_md5']:
         raise Exception('invalid gpgkey_md5')

   def _dump(self):
      command = 'mysqldump --single-transaction --routines ' + self.kwargs['database_name']
      command += ' | /usr/bin/gpg --batch -c --cipher-algo aes256 --compress-level 9 --passphrase-file '
      command += self.kwargs['gpg_keyfile'] + ' >' + self.backup_name
      print(command)
      subprocess.run(command,shell=True)


