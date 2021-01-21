
__module__     = 'ec2_info.py'
__maintainer__ = 'Rob Mitchell <rob.mitchell@objectstream.com>,<rlmitchell@gmail.com>'
__tested__     = 'Python 3.6.8'
__version__    = '2021.01.14.0909'


import boto3
import json
import pprint


class InstancesInfo:
   """Collects id,name,state and public ip address of all instances in a region."""

   def __init__(self):
      self.ec2 = boto3.session.Session().resource('ec2')
      self.ids = tuple(( i['InstanceId'] for i in [n['Instances'][0] for n in boto3.client('ec2').describe_instances()['Reservations']] ))

   def get_info(self):
      """
      Gets info for all instances.

      :return: tuples - one per instance (id,name,state,public_ip)
      :rtype:  tuple of tuples
      """
      info = []
      for i in self.ids:
         try:
            instance = self.ec2.Instance(i)
            name = self.get_name(instance.tags)
            state = instance.state['Name']
            public_ip = instance.public_ip_address
            info.append( (i,name,state,public_ip) )
         except Exception as e:
            info.append( () )
      return tuple(info)

   def get_name(self,tags):
      """
      Gets the value of the Name tag.

      :param tags: instance tags from AWS
      :type tags:  list of dicts

      :return: value of the Name tag
      :rtype:  str
      """
      for tag in tags:
         if tag['Key'] == 'Name':
            return tag['Value']
      return None


if __name__ == '__main__':
   pprint.pprint( InstancesInfo().get_info() )

