
__module__     = 's3purge.py'
__maintainer__ = 'Rob Mitchell <rob.mitchell@objectstream.com>,<rlmitchell@gmail.com>'
__tested__     = 'Python 3.5.2'
__version__    = '2021.01.20.1254'


import boto3


class PurgeS3:
	def __init__(self,backup_prefix=None,num_keep=0,bucket_name=None):
		self.backup_prefix = backup_prefix
		self.keep = num_keep
		self.bucket = boto3.resource('s3').Bucket( bucket_name )
		self.objects = [o for o in self.bucket.objects.all() if self.backup_prefix in o.key]

	def __call__(self):
		keys = sorted([o.key for o in self.objects])
		while len(self.objects) > self.keep:
			delete_object = self.objects.pop(0)
			response = delete_object.delete()

