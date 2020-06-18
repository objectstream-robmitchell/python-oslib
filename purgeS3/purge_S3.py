
__module__      = 'purge_s3.py'
__author__      = 'Rob Mitchell <rob.mitchell@objectstream.com>'
__updated__     = '2020.06.17'
__version__     = '0.5.0'
__status__      = 'development, final'

import boto3
from json_file import JSONFile

class S3BucketPurger(object):
	def __init__(self):
		self.config = JSONFile('config.json').load()
		self.bucket = boto3.resource('s3').Bucket( self.config['bucket'] )
		self.all_objects = list( self.bucket.objects.all() )

	def __call__(self):
		self._purge()

	def _purge(self):
		for backup_object_group in self.config['backup_object_groups']:
			backup_object_group_keys = self._get_backup_object_keys_in_group(backup_object_group)
			while len(backup_object_group_keys) > backup_object_group['keep_num']:
				self._remove_object( backup_object_group_keys.pop(0) )

	def _get_backup_object_keys_in_group(self,backup_object_group):
		backup_group_object_keys = []
		for backup_object in self.all_objects:
			if backup_object_group['key_component'] in backup_object.key:
				backup_group_object_keys.append(backup_object.key)
		backup_group_object_keys.sort()
		return backup_group_object_keys

	def _remove_object(self, object_key):
		for backup_object in self.all_objects:
			if object_key == backup_object.key:
				response = backup_object.delete()


if __name__ == '__main__':
	S3BucketPurger()()

