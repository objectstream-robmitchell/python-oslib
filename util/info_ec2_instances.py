
__module__     = 'info_ec2_instances.py'
__maintainer__ = 'Rob Mitchell <rob.mitchell@objectstream.com>,<rlmitchell@gmail.com>'
__tested__     = 'Python 3.6.8'
__version__    = '2021.01.14.0909'


import boto3
import json
import os
from pprint import pprint


class InfoEC2Instances:
   """Collects id,name,state and public ip address of all instances in a region."""

   def __init__(self):
      self.region = os.getenv('AWS_REGION')
      self.access_key = os.getenv('AWS_ACCESS_KEY')
      self.secret_key = os.getenv('AWS_SECRET_KEY')
      self.session = boto3.Session(aws_access_key_id=self.access_key,
                                   aws_secret_access_key=self.secret_key,
                                   region_name=self.region)
      self.ec2client = self.session.client('ec2')
      self.reservations = self.ec2client.describe_instances()['Reservations']


   def __call__(self):
      info = []
      for resv in self.reservations:
         info.append((self.get_instance_id(resv), self.get_instance_name(resv),
                      self.get_instance_publicip(resv), self.get_instance_state(resv)))
      return info

   def get_instance_id(self, reservation):
      try:
         return reservation['Instances'][0]['InstanceId']
      except:
         return None

   def get_instance_name(self, reservation):
      try:
         for tag in reservation['Instances'][0]['Tags']:
            if tag['Key'] == 'Name':
               return tag['Value']
         return None
      except:
         return None

   def get_instance_publicip(self, reservation):
      try:
         return reservation['Instances'][0]['PublicIpAddress']
      except:
         return None

   def get_instance_state(self, reservation):
      try:
         return reservation['Instances'][0]['State']['Name']
      except:
         return None


if __name__ == '__main__':
   print(json.dumps(InfoEC2Instances()()))

