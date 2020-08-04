
__module__     = 'timestamp.py'
__maintainer__ = 'Rob Mitchell'
__email__      = 'rob.mitchell@objectstream.com'
__version__    = '1.2.0'
__status__     = 'production'

import datetime
import time


class TStamp:
   def __call__(self):
      n = datetime.datetime.now()
      return ''.join( [x if len(x) > 1 else '0'+x for x in (str(n.year),str(n.month),str(n.day),str(n.hour),str(n.minute),str(n.second))] )

class Timestamp:
   def timestamp(self):
      n = datetime.datetime.now()
      return ''.join( [x if len(x) > 1 else '0'+x for x in (str(n.year),str(n.month),str(n.day),str(n.hour),str(n.minute),str(n.second))] )

   def epoch(self):
      return str(time.time()).split('.')[0]


if __name__ == '__main__':
   print TStamp()()
   print Timestamp().timestamp()
   print Timestamp().epoch()


