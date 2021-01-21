
__module__     = 's3upload.py'
__maintainer__ = 'Rob Mitchell <rob.mitchell@objectstream.com>,<rlmitchell@gmail.com>'
__tested__     = 'Python 3.6.8'
__version__    = '2021.01.20.1550'


import boto3


class S3Upload:
   def __init__(self,filename,bucket_name):
      self.bucket_name = bucket_name
      self.filename = filename
      self.objectname = filename.split('/')[-1]
      self.s3 = boto3.resource('s3')

   def __call__(self):
      self.s3.Bucket(self.bucket_name).upload_file(self.filename,self.objectname)

