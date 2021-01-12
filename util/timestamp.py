
__module__     = 'timestamp.py'
__maintainer__ = 'Rob Mitchell <rob.mitchell@objectstream.com>,<rlmitchell@gmail.com>'
__tested__     = 'Python 3.6.8'
__version__    = '2021.01.12.1504'

import datetime
import time

class Timestamp:
   def __init__(self):
      self.now = datetime.datetime.now()

   def timestamp(self,zone=False):
      n = self.now
      stamp = ''.join( [x if len(x) > 1 else '0'+x for x in (str(n.year),str(n.month),str(n.day),str(n.hour),str(n.minute),str(n.second))] )
      if zone:
         return stamp+time.tzname[time.localtime().tm_isdst]
      return stamp

   def epoch(self):
      return str(time.time()).split('.')[0]


if __name__ == '__main__':
   print( Timestamp().timestamp() )
   print( Timestamp().timestamp(zone=True) )
   print( Timestamp().epoch() )

