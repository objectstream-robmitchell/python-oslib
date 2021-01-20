
__module__     = 'mysqldump.py'
__maintainer__ = 'Rob Mitchell <rob.mitchell@objectstream.com>,<rlmitchell@gmail.com>'
__tested__     = 'Python 3.6.8'
__version__    = '2021.01.20.1625'


import subprocess
import hashlib
import platform
from util.tmp_storage import TmpStorage
from util.timestamp import Timestamp
from util.s3upload import S3Upload
from osprivate import osprivate


class MySQLDump:
   def __init__(self,database_name=None):
      TmpStorage(config=osprivate['tmpstore_config'])()
      self.database_name = database_name
      self.gpg_keyfile = osprivate['gpgkey']
      self.gpg_keyfile_md5 = osprivate['gpgkey_md5']

   def __call__(self):
      self._run_checks()
      self._dump()
      self._send_offsite()

   def _run_checks(self):
      self._check_aes_key()

   def _check_aes_key(self):
      with open(self.gpg_keyfile,'rb') as f:
         md5hash = hashlib.md5(f.read()).hexdigest()
      if md5hash != self.gpg_keyfile_md5:
         raise Exception('invalid gpgkey_md5')

   def _dump(self):
      local_tmpstore_dir = osprivate['tmpstore_config']['local']
      self.backup_name = local_tmpstore_dir + '/autobck.' + platform.node().split('.')[0]
      self.backup_name += '.' + self.database_name + '.' + Timestamp().epoch()
      command = 'mysqldump --single-transaction --routines ' + self.database_name
      command += ' | /usr/bin/gpg --batch -c --cipher-algo aes256 --compress-level 9 --passphrase-file '
      command += self.gpg_keyfile + ' >' + self.backup_name
      subprocess.run(command,shell=True)

   def _send_offsite(self):
      S3Upload(self.backup_name)()

