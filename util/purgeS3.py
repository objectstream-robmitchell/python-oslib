
__module__     = 'purgeS3.py'
__maintainer__ = 'Rob Mitchell <rob.mitchell@objectstream.com>,<rlmitchell@gmail.com>'
__tested__     = 'Python 3.5.2'
__version__    = '2021.01.20.1217'


import boto3


class PurgeS3:
	def __init__(self,backup_prefix=None,num_keep=0,bucket_name=None):
		self.backup_prefix = backup_prefix
		self.keep = num_keep
		self.bucket = boto3.resource('s3').Bucket( bucket_name )
		self.objects = [o for o in self.bucket.objects.all() if self.backup_prefix in o.key]

		#self.objects = list( self.bucket.objects.all() )
		#self.keys = self._backup_object_keys()

	def __call__(self):
		print(self.objects)

	

if __name__ == '__main__':
	p = PurgeS3(backup_prefix='bck.container-data.xwiki9-mysql-db.',num_keep=10,bucket_name='backups.okc.objectstream.com')()

